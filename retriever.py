"""
RAG Retrieval Engine for the R&D Tax Incentive Handbook.
Uses simple TF-IDF style keyword matching + semantic scoring — no external vector DB needed.
"""

import math
import re
from collections import Counter
from knowledge_base import get_all_chunks


def tokenize(text: str) -> list[str]:
    """Simple tokenizer: lowercase, remove punctuation, split on whitespace."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    return [t for t in text.split() if len(t) > 2]


def build_idf(chunks: list[dict]) -> dict[str, float]:
    """Build inverse document frequency from all chunks."""
    num_docs = len(chunks)
    doc_freq: dict[str, int] = {}
    for chunk in chunks:
        tokens = set(tokenize(chunk["title"] + " " + chunk["content"]))
        for token in tokens:
            doc_freq[token] = doc_freq.get(token, 0) + 1
    return {
        term: math.log(num_docs / (freq + 1)) + 1
        for term, freq in doc_freq.items()
    }


def tfidf_score(query_tokens: list[str], chunk: dict, idf: dict[str, float]) -> float:
    """Score a chunk against a query using TF-IDF."""
    text = (chunk["title"] + " " + chunk["content"]).lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    chunk_tokens = text.split()
    tf: dict[str, float] = Counter(chunk_tokens)
    total_tokens = len(chunk_tokens) or 1
    score = 0.0
    for token in query_tokens:
        if token in tf:
            tf_val = tf[token] / total_tokens
            idf_val = idf.get(token, 1.0)
            score += tf_val * idf_val
    # Boost for title matches
    title_tokens = set(tokenize(chunk["title"]))
    for token in query_tokens:
        if token in title_tokens:
            score += 0.5
    return score


# Build IDF index at module load time
_chunks = get_all_chunks()
_idf = build_idf(_chunks)

# Keyword-to-chunk mapping for common topics
TOPIC_KEYWORDS = {
    "eligible_entities": ["trust", "trustee", "pty ltd", "partnership", "sole trader", "who can claim", "eligible entity", "incorporated"],
    "three_limb_test": ["three limb", "three-limb", "core activity test", "qualify", "qualification criteria"],
    "excluded_activities": ["excluded", "not eligible", "ineligible", "cannot claim", "market research", "quality assurance"],
    "benefits_offset": ["refund", "refundable", "offset", "benefit", "how much", "percentage", "cash back", "tax offset"],
    "eligible_expenditure": ["wages", "salary", "contractor", "materials", "overhead", "depreciation", "what costs", "claimable"],
    "registration_process": ["register", "registration", "ausindustry", "deadline", "portal", "how to apply", "10 months"],
    "ato_claim": ["ato", "tax return", "claim", "lodge", "schedule", "how to claim"],
    "compliance_pitfalls": ["mistake", "pitfall", "avoid", "common error", "fail", "audit risk", "non-compliance"],
    "audit_process": ["audit", "review", "investigation", "regulator", "compliance review", "being audited"],
    "record_keeping": ["records", "documentation", "evidence", "timesheet", "lab notebook", "record keeping"],
    "software_ict": ["software", "algorithm", "coding", "ai", "machine learning", "ict", "app", "program", "saas"],
    "manufacturing": ["manufacturing", "engineering", "prototype", "material", "composite", "fabrication"],
    "agriculture": ["agriculture", "farming", "crop", "irrigation", "food processing", "agri"],
    "health_biotech": ["biotech", "pharmaceutical", "drug", "clinical trial", "medical device", "health", "lab"],
}


def retrieve(query: str, top_k: int = 4) -> list[dict]:
    """Retrieve the most relevant chunks for a query."""
    query_tokens = tokenize(query)
    query_lower = query.lower()

    scores = []
    for chunk in _chunks:
        score = tfidf_score(query_tokens, chunk, _idf)
        # Boost based on topic keyword mapping
        for chunk_id, keywords in TOPIC_KEYWORDS.items():
            if chunk["id"] == chunk_id:
                for kw in keywords:
                    if kw in query_lower:
                        score += 1.5
        scores.append((score, chunk))

    scores.sort(key=lambda x: x[0], reverse=True)
    return [chunk for score, chunk in scores[:top_k] if score > 0.01]


def format_context(chunks: list[dict]) -> str:
    """Format retrieved chunks into a context string for the LLM."""
    if not chunks:
        return "No specific content found. Please answer based on general R&D Tax Incentive knowledge."
    parts = []
    for i, chunk in enumerate(chunks, 1):
        parts.append(f"[Source {i}: {chunk['title']}]\n{chunk['content']}")
    return "\n\n---\n\n".join(parts)

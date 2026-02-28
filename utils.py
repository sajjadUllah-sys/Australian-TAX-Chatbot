import os
import fitz
import io
from typing import List
import tiktoken
from sentence_transformers import SentenceTransformer
from PIL import Image
from docx import Document
import base64
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract full text from uploaded PDF"""
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text


def extract_text_from_docx(file_bytes: bytes) -> str:
    doc = Document(io.BytesIO(file_bytes))
    text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    return text

def extract_text_from_image(file_bytes: bytes) -> str:
        client = get_openai_client()
        base64_image = base64.b64encode(file_bytes).decode("utf-8")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Extract all readable text from this image carefully and focus on the accuracy."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ]
        )

        return response.choices[0].message.content.strip()

def split_text(text: str, max_tokens=500) -> List[str]:
    enc = tiktoken.get_encoding("cl100k_base")
    words = text.split()
    chunks, chunk = [], []
    tokens = 0
    for word in words:
        word_tokens = len(enc.encode(word))
        if tokens + word_tokens > max_tokens:
            chunks.append(" ".join(chunk))
            chunk = []
            tokens = 0
        chunk.append(word)
        tokens += word_tokens
    if chunk:
        chunks.append(" ".join(chunk))
    return chunks


def create_embeddings(chunks: List[str], model_name: str = "all-MiniLM-L6-v2") -> List[dict]:
    model = SentenceTransformer(model_name)
    embeddings = []
    vectors = model.encode(chunks, show_progress_bar=True)
    for chunk, vector in zip(chunks, vectors):
        embeddings.append({"text": chunk, "embedding": vector.tolist()})
    return embeddings
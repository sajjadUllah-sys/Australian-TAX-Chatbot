# 🔬 Australian R&D Tax Incentive RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built from the **Australian R&D Tax Incentive Handbook** by Bruce Patten, Pattens Group Pty Ltd.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install streamlit openai
```

### 2. Run the App

```bash
cd rd_chatbot
streamlit run app.py
```

### 3. Enter Your OpenAI API Key
- Open the app in your browser (usually http://localhost:8501)
- Paste your OpenAI API key in the sidebar
- Start asking questions!

---

## 📁 Project Structure

```
rd_chatbot/
├── app.py              # Main Streamlit UI
├── retriever.py        # RAG retrieval engine (TF-IDF)
├── knowledge_base.py   # Pre-processed handbook content (24 sections)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🧠 How It Works (RAG Architecture)

```
User Question
     ↓
 [Retriever]
  TF-IDF scoring over 24 knowledge chunks
  + Topic keyword boosting
     ↓
 Top 4 Relevant Chunks Selected
     ↓
 [OpenAI GPT]
  System prompt + handbook context + question
     ↓
 Grounded, accurate answer
  + Source sections shown
```

### Why No Vector Database?
The handbook is ~50 pages — small enough that a well-implemented TF-IDF retriever gives excellent results without needing `faiss`, `chromadb`, or `pinecone`. This keeps the app dependency-free and fast.

---

## 📚 Knowledge Base Coverage

The 24 knowledge sections cover:

| Section | Topics |
|---------|--------|
| Overview & Legislation | RDTI purpose, IR&D Act 1986, Division 355 |
| Core Concepts | Three-Limb Test, technical uncertainty, hypothesis |
| Activities | Core activities, supporting activities, excluded activities |
| Entities | Who can claim, group structures, trustees |
| Benefits | Offset rates, refundable vs non-refundable, cash flow |
| Expenditure | Eligible costs, feedstock rule, apportionment |
| Application | Pre-registration, AusIndustry portal, ATO claim |
| Compliance | Top 10 pitfalls, audit process, record keeping |
| Industries | Software/ICT, Manufacturing, Agriculture, Health/Biotech |
| Strategy | Integration with business, working with advisors |
| Post-Claim | Record retention, ongoing obligations |
| Templates | Project summary sheet, timesheets, checklists |

---

## 💡 Example Questions

- *"What is the three-limb test for core R&D activities?"*
- *"My software startup has $200k in R&D — how much refund can I get?"*
- *"Does debugging count as R&D?"*
- *"What is the registration deadline for a 30 June balance date?"*
- *"What is the feedstock rule?"*
- *"What records do I need to keep for an audit?"*
- *"Can a trust claim the R&D Tax Incentive?"*
- *"What triggers an ATO audit of my R&D claim?"*
- *"How do I separate R&D from production in a manufacturing context?"*

---

## ⚙️ Configuration

| Option | Default | Notes |
|--------|---------|-------|
| Model | `gpt-4o-mini` | Also supports `gpt-4o`, `gpt-3.5-turbo` |
| Top-K chunks | 4 | Retrieved per query |
| Max response tokens | 1200 | Adjustable in `app.py` |
| Temperature | 0.2 | Low for factual accuracy |

---

## ⚠️ Disclaimer

This chatbot provides **general guidance only** based on the R&D Tax Incentive Handbook. It is not a substitute for professional tax advice. For specific situations, consult a qualified Grants Specialist or R&D Tax Advisor.

---

*Knowledge base: © Pattens Group Pty Ltd 2026. App built for educational and compliance assistance purposes.*

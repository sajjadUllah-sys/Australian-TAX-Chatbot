import os
import numpy as np
from dotenv import load_dotenv
from vectordb import VectorStore
from openai import OpenAI
from sentence_transformers import SentenceTransformer
from pathlib import Path
from utils import (
    extract_text_from_pdf,
    extract_text_from_docx,
    extract_text_from_image,
    split_text,
    create_embeddings
)

model = SentenceTransformer("all-MiniLM-L6-v2")

load_dotenv()
api_key = os.getenv("sk-NJumW62QgMYHHq9Y97zNmqGKhshPXHCcJS0Q7LUGO9VSSX80")

client = OpenAI(api_key=api_key)

vector_store = VectorStore(dim=384)

def process_file(uploaded_file):
    ext = Path(uploaded_file.name).suffix.lower()
    file_bytes = uploaded_file.read()

    if ext == ".pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif ext == ".docx":
        text = extract_text_from_docx(file_bytes)
    elif ext in [".png", ".jpg", ".jpeg"]:
        text = extract_text_from_image(file_bytes)
    else:
        raise ValueError("Unsupported file type")

    chunks = split_text(text)
    embeddings = create_embeddings(chunks)
    texts = [chunk["text"] for chunk in embeddings]
    vectors = [chunk["embedding"] for chunk in embeddings]
    vector_store.add(vectors, texts)
    return embeddings
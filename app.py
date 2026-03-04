"""
Australian R&D Tax Incentive RAG Chatbot
Built with Streamlit + OpenAI + custom RAG retrieval
"""

import streamlit as st
import openai
import sys
import os
from pathlib import Path

# ── Load .env file ────────────────────────────────────────────────────────────
def load_env_file():
    """Load environment variables from .env file if it exists."""
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                # Skip comments and empty lines
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip()
                    # Don't override existing environment variables
                    if key and value and key not in os.environ:
                        os.environ[key] = value

load_env_file()

sys.path.insert(0, os.path.dirname(__file__))
from retriever import retrieve, format_context

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="R&D Tax Incentive Assistant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #0f1724;
        color: #e8edf5;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a2744 0%, #0f1724 100%);
        border-right: 1px solid #2a3f6f;
    }

    /* Chat messages */
    .chat-message {
        padding: 16px 20px;
        border-radius: 12px;
        margin: 10px 0;
        max-width: 85%;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    .user-message {
        background: linear-gradient(135deg, #1e3a6e 0%, #163060 100%);
        border: 1px solid #2d5099;
        margin-left: auto;
        margin-right: 0;
        border-bottom-right-radius: 4px;
    }
    .assistant-message {
        background: linear-gradient(135deg, #1a2a1a 0%, #152215 100%);
        border: 1px solid #2d5c2d;
        border-bottom-left-radius: 4px;
    }
    .message-label {
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 6px;
        opacity: 0.7;
    }
    .user-label { color: #7eb8ff; }
    .assistant-label { color: #7eff9e; }

    /* Sources panel */
    .source-chip {
        display: inline-block;
        background: #1e2f50;
        border: 1px solid #2d4a7a;
        border-radius: 20px;
        padding: 3px 12px;
        font-size: 0.78rem;
        color: #89b4ff;
        margin: 3px 3px 3px 0;
    }

    /* Welcome card */
    .welcome-card {
        background: linear-gradient(135deg, #1a2744 0%, #1a2a1a 100%);
        border: 1px solid #2d4a7a;
        border-radius: 16px;
        padding: 28px 32px;
        margin: 20px 0;
    }
    .welcome-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #7eb8ff;
        margin-bottom: 12px;
    }
    .welcome-subtitle {
        color: #a8c4e0;
        font-size: 0.95rem;
        line-height: 1.7;
    }
    .capability-item {
        display: flex;
        align-items: flex-start;
        gap: 10px;
        margin: 8px 0;
        color: #c8dff0;
        font-size: 0.92rem;
    }
    .capability-dot {
        color: #7eff9e;
        font-weight: bold;
        margin-top: 2px;
    }

    /* Input */
    .stTextInput > div > div > input {
        background: #1a2744 !important;
        border: 1px solid #2d4a7a !important;
        color: #e8edf5 !important;
        border-radius: 10px !important;
        padding: 12px 16px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #5b8dee !important;
        box-shadow: 0 0 0 2px rgba(91,141,238,0.2) !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #2d5099 0%, #1e3a7a 100%);
        border: 1px solid #3d6bbf;
        color: white;
        border-radius: 8px;
        padding: 8px 20px;
        font-weight: 600;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #3d6bbf 0%, #2d5099 100%);
        border-color: #5b8dee;
        transform: translateY(-1px);
    }

    /* Divider */
    hr { border-color: #2a3f6f !important; }

    /* Sidebar items */
    .sidebar-section {
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        padding: 14px 16px;
        margin: 10px 0;
        border: 1px solid #2a3f6f;
    }
    .sidebar-title {
        font-size: 0.8rem;
        font-weight: 700;
        color: #7eb8ff;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 8px;
    }
    .quick-question {
        background: rgba(45,80,153,0.3);
        border: 1px solid #2d4a7a;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 0.83rem;
        color: #c8dff0;
        margin: 4px 0;
        cursor: pointer;
        transition: background 0.15s;
    }

    /* Spinner */
    .stSpinner > div { border-top-color: #5b8dee !important; }

    /* Selectbox */
    .stSelectbox > div > div {
        background: #1a2744 !important;
        border-color: #2d4a7a !important;
        color: #e8edf5 !important;
    }

    /* Hide Streamlit branding */
    #MainMenu, footer { visibility: hidden; }
    header { visibility: hidden; }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #0f1724; }
    ::-webkit-scrollbar-thumb { background: #2d4a7a; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)


# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

# Auto-load API key from .env / environment variable if not already set in session
if "api_key" not in st.session_state:
    env_key = os.environ.get("OPENAI_API_KEY", "")
    if env_key and not env_key.startswith("sk-your-"):
        st.session_state.api_key = env_key
        st.session_state.api_key_set = True
    else:
        st.session_state.api_key = ""
        st.session_state.api_key_set = False


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🔬 R&D Tax Assistant")
    st.markdown("---")

    # API Key input
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">🔑 OpenAI API Key</div>', unsafe_allow_html=True)

    if st.session_state.api_key_set:
        st.success("✓ API key loaded from .env", icon="✅")
        if st.button("🔄 Use a different key", use_container_width=True):
            st.session_state.api_key = ""
            st.session_state.api_key_set = False
            st.rerun()
    else:
        api_key_input = st.text_input(
            "Enter your OpenAI API key",
            type="password",
            placeholder="sk-...  (or add to .env file)",
            label_visibility="collapsed"
        )
        if api_key_input:
            st.session_state.api_key = api_key_input
            st.session_state.api_key_set = True
            st.success("✓ API key set", icon="✅")
            st.rerun()
        st.caption("💡 Add `OPENAI_API_KEY=sk-...` to the `.env` file to skip this step.")

    st.markdown('</div>', unsafe_allow_html=True)

    # Model selection
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">⚙️ Model</div>', unsafe_allow_html=True)
    model = st.selectbox(
        "Model",
        ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Quick questions
    st.markdown('<div class="sidebar-title">💡 Quick Questions</div>', unsafe_allow_html=True)

    quick_questions = [
        "What is technical uncertainty?",
        "Who is eligible to claim RDTI?",
        "What is the registration deadline?",
        "What costs are eligible?",
        "What is the feedstock rule?",
        "How does software qualify?",
        "What is a core R&D activity?",
        "What triggers an audit?",
        "How much refund can I get?",
        "What records do I need?",
    ]

    for q in quick_questions:
        if st.button(q, key=f"qq_{q}", use_container_width=True):
            st.session_state.pending_question = q

    st.markdown("---")

    # Stats
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">📚 Knowledge Base</div>', unsafe_allow_html=True)
    st.markdown(f"**24** topic sections")
    st.markdown(f"**50+** pages of content")
    st.markdown(f"**{len(st.session_state.messages)//2}** questions asked")
    st.markdown('</div>', unsafe_allow_html=True)

    # Clear chat
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ── Main area ─────────────────────────────────────────────────────────────────
# Header
col1, col2 = st.columns([8, 2])
with col1:
    st.markdown("# 🔬 Australian R&D Tax Incentive Assistant")
    st.markdown("*Powered by the R&D Tax Incentive Handbook by Bruce Patten, Pattens Group Pty Ltd*")

st.markdown("---")


def render_welcome():
    st.markdown("""
    <div class="welcome-card">
        <div class="welcome-title">👋 Hello! I am your R&D Compliance Assistant.</div>
        <div class="welcome-subtitle">
            I can help you navigate the Australian R&D Tax Incentive (RDTI) program.
            My knowledge is drawn directly from the official R&D Tax Incentive Handbook.
        </div>
        <br/>
        <div class="capability-item"><span class="capability-dot">•</span> Understanding Australian R&D tax incentive requirements</div>
        <div class="capability-item"><span class="capability-dot">•</span> Clarifying what qualifies as core R&D activities (the Three-Limb Test)</div>
        <div class="capability-item"><span class="capability-dot">•</span> Explaining eligible expenditure categories and the feedstock rule</div>
        <div class="capability-item"><span class="capability-dot">•</span> Answering questions about technical uncertainty</div>
        <div class="capability-item"><span class="capability-dot">•</span> Guidance on systematic experimentation and documentation</div>
        <div class="capability-item"><span class="capability-dot">•</span> Industry-specific guidance: Software, Manufacturing, Agriculture, Health/Biotech</div>
        <div class="capability-item"><span class="capability-dot">•</span> Registration process, deadlines and ATO claim procedures</div>
        <div class="capability-item"><span class="capability-dot">•</span> Audit preparation and compliance pitfalls to avoid</div>
        <br/>
        <div class="welcome-subtitle">
            💡 <strong>Tip:</strong> Use the quick questions in the sidebar, or ask anything in your own words below.
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_messages():
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <div class="message-label user-label">👤 You</div>
                {msg["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            content = msg["content"]
            sources_html = ""
            if "sources" in msg:
                chips = "".join(
                    f'<span class="source-chip">📄 {s}</span>'
                    for s in msg["sources"]
                )
                sources_html = f'<div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.1)">{chips}</div>'
            st.markdown(f"""
            <div class="chat-message assistant-message">
                <div class="message-label assistant-label">🔬 R&D Assistant</div>
                {content}{sources_html}
            </div>
            """, unsafe_allow_html=True)


def generate_response(user_query: str, api_key: str, model: str) -> tuple[str, list[str]]:
    """Run RAG: retrieve relevant chunks, then call OpenAI."""
    # Retrieve relevant context
    relevant_chunks = retrieve(user_query, top_k=4)
    context = format_context(relevant_chunks)
    source_titles = [c["title"] for c in relevant_chunks]

    # Build conversation history (last 6 exchanges for context)
    history = []
    for msg in st.session_state.messages[-12:]:
        if msg["role"] in ("user", "assistant"):
            history.append({"role": msg["role"], "content": msg["content"]})

    system_prompt = """You are an expert Australian R&D Tax Incentive (RDTI) compliance assistant. 
Your knowledge comes from the official R&D Tax Incentive Handbook by Bruce Patten of Pattens Group Pty Ltd.

INSTRUCTIONS:
- Answer questions accurately using the provided context from the handbook.
- Be specific and practical — give concrete guidance, not vague generalities.
- When quoting figures (e.g., offset rates, deadlines), be precise.
- Use Australian English spelling.
- Format your response clearly. Use bullet points and numbered lists where helpful.
- If the context doesn't fully cover the question, say so and provide general guidance.
- Always encourage professional advice for specific tax situations.
- Be concise but comprehensive.
- Do NOT make up information. If you're unsure, say so.

DISCLAIMER: Always note that this is general guidance only and specific situations should be reviewed by a qualified R&D tax specialist or Grants Specialist."""

    client = openai.OpenAI(api_key=api_key)

    messages = [{"role": "system", "content": system_prompt}]
    messages.append({
        "role": "user",
        "content": f"""HANDBOOK CONTEXT:
{context}

USER QUESTION: {user_query}

Please answer the question based on the handbook context above."""
    })

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2,
        max_tokens=1200,
    )

    answer = response.choices[0].message.content
    return answer, source_titles


# ── Chat interface ─────────────────────────────────────────────────────────────
if not st.session_state.messages:
    render_welcome()
else:
    render_messages()

# Chat input
st.markdown("<br/>", unsafe_allow_html=True)

with st.container():
    col_input, col_send = st.columns([9, 1])
    with col_input:
        user_input = st.text_input(
            "Ask a question...",
            placeholder="e.g. What qualifies as a core R&D activity?",
            label_visibility="collapsed",
            key="user_input"
        )
    with col_send:
        send_clicked = st.button("Send ➤", use_container_width=True)

# Handle pending question from sidebar
if st.session_state.pending_question:
    user_input = st.session_state.pending_question
    st.session_state.pending_question = None
    send_clicked = True

# Process the question
query = user_input if (send_clicked and user_input) else None

if query:
    if not st.session_state.api_key_set:
        st.error("⚠️ Please enter your OpenAI API key in the sidebar to continue.")
    else:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": query})

        # Generate response
        with st.spinner("🔍 Searching handbook and generating response..."):
            try:
                answer, sources = generate_response(
                    query,
                    st.session_state.api_key,
                    model
                )
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })
            except openai.AuthenticationError:
                st.error("❌ Invalid API key. Please check your OpenAI API key and try again.")
                st.session_state.messages.pop()
            except openai.RateLimitError:
                st.error("⚠️ OpenAI rate limit reached. Please wait a moment and try again.")
                st.session_state.messages.pop()
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.session_state.messages.pop()

        st.rerun()


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    """<div style="text-align:center; color:#4a6080; font-size:0.8rem; padding:10px 0">
    📚 Based on <em>The Australian R&D Tax Incentive Handbook</em> by Bruce Patten, Pattens Group Pty Ltd (2026) &nbsp;|&nbsp;
    ⚠️ This tool provides general guidance only — consult a qualified specialist for your specific situation.
    </div>""",
    unsafe_allow_html=True
)

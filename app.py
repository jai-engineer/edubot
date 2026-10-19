import streamlit as st
from PIL import Image

st.set_page_config(page_title="EduBot: Interactive Learning Lab", layout="wide", page_icon="🚀")

# Sleek style injection
st.markdown("""
    <style>
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #1E40AF, #3B82F6, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-top: 20px;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 40px;
    }
    .card-container {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 40px;
    }
    .feature-card {
        background: #F3F4F6;
        border-left: 5px solid #3B82F6;
        padding: 20px;
        border-radius: 8px;
        width: 280px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1F2937;
        margin-bottom: 8px;
    }
    .card-desc {
        font-size: 0.9rem;
        color: #6B7280;
    }
    .element-container div.stButton {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "messages" not in st.session_state:
    st.session_state.messages = []

# WELCOME LANDING PAGE DISPLAY
if st.session_state.page == "welcome":
    st.markdown('<div class="hero-title">🚀 Welcome to EduBot Pro</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">The Exhibition-Grade Intelligent Vision Tutor for Next-Gen Classrooms</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="card-container">
            <div class="feature-card">
                <div class="card-title">👁️ Computer Vision Matrix</div>
                <div class="card-desc">Snap a picture of raw mathematical equations, charts, or handwriting to instantly parse problems.</div>
            </div>
            <div class="feature-card">
                <div class="card-title">🛡️ Anti-Cheat Core</div>
                <div class="card-desc">Hides rapid copy-paste text values. Forces structural conceptual understanding through targeted hints.</div>
            </div>
            <div class="feature-card">
                <div class="card-title">🌍 Multilingual Synthesis</div>
                <div class="card-desc">Fluently switches entire reasoning transcripts into regional scripts like Hindi or Punjabi dynamically.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.write("### Ready to see it in action?")
    if st.button("✨ Launch Main AI Interface", type="primary"):
        st.session_state.page = "chat_interface"
        st.rerun()

# MAIN SIMULATED SOLVER INTERFACE
elif st.session_state.page == "chat_interface":
    if st.button("⬅️ Return to Main Welcome Page"):
        st.session_state.page = "welcome"
        st.rerun()
        
    st.markdown("### 💬 Interactive Solution Laboratory")
    st.sidebar.header("🎯 System Controllers")
    
    language = st.sidebar.selectbox(
        "Explanation Script Target",
        ["English", "Hindi (हिंदी)", "Punjabi (ਪੰਜਾਬੀ)", "Hinglish"]
    )
    
    learning_mode = st.sidebar.toggle("Activate Anti-Cheat Learning Mode", value=False)
    generate_practice = st.sidebar.toggle("Append Dynamic Practice Challenges", value=True)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("📷 Optical Lens Input")
    uploaded_file = st.sidebar.file_uploader("Drop equation screenshot here", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.sidebar.image(Image.open(uploaded_file), caption="Optical Lens Stream active", use_container_width=True)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_prompt := st.chat_input("Ask a question, or type 'Analyze upload'"):
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        # Static simulated response for flawless local exhibition presentation
        with st.chat_message("assistant"):
            with st.spinner("Analyzing data vectors..."):
                import time
                time.sleep(1.5)
                
                if learning_mode:
                    if language == "Hindi (हिंदी)":
                        ans = (
                            "### 📚 **ट्यूटोरियल गाइड: द्विघात बहुपद (Quadratic Polynomial)**\n\n"
                            "**चरण 1:** दिए गए बहुपद $f(x) = x^2 + x - 2$ के गुणांकों (coefficients) की तुलना $ax^2 + bx + c$ से करें।\n"
                            "यहाँ, $a = 1, b = 1, c = -2$ है।\n\n"
                            "**चरण 2:** मूलों का योग सूत्र लागू करें: $\\alpha + \\beta = -b/a = -1/1 = -1$।\n"
                            "मूलों का गुणनफल सूत्र लागू करें: $\\alpha\\beta = c/a = -2/1 = -2$।\n\n"
                            "**💡 संकेत (Hint):** व्यंजक $\\frac{1}{\\alpha} - \\frac{1}{\\beta}$ को $\\frac{\\beta - \\alpha}{\\alpha\\beta}$ के रूप में लिखा जा सकता है। "
                            "बीजगणितीय पहचान $(\\beta - \\alpha)^2 = (\\alpha + \\beta)^2 - 4\\alpha\\beta$ का उपयोग करके मान ज्ञात करें और अंतिम विभाजन स्वयं हल करें!"
                        )
                    else:
                        ans = (
                            "### 📚 **Tutorial Guide: Quadratic Polynomials**\n\n"
                            "**Step 1:** Formulate your coefficient matrix from $f(x) = x^2 + x - 2$. Here, $a = 1, b = 1, c = -2$.\n\n"
                            "**Step 2:** Calculate Sum ($\\alpha + \\beta = -b/a = -1$) and Product ($\\alpha\\beta = c/a = -2$).\n\n"
                            "**💡 Hint:** Rewrite the required expression $\\frac{1}{\\alpha} - \\frac{1}{\\beta}$ into $\\frac{\\beta - \\alpha}{\\alpha\\beta}$. "
                            "Use the algebraic identity $(\\beta - \\alpha)^2 = (\\alpha + \\beta)^2 - 4\\alpha\\beta$ to plug in the values and solve the final fractions!"
                        )
                else:
                    if language == "Hindi (हिंदी)":
                        ans = (
                            "### 📝 **पूर्ण समाधान (Complete Solution) - प्रश्न 6**\n\n"
                            "दिए गए बहुपद के लिए: $\\alpha + \\beta = -1$ और $\\alpha\\beta = -2$ है।\n\n"
                            "**गणना:**\n"
                            "$$\\frac{1}{\\alpha} - \\frac{1}{\\beta} = \\frac{\\beta - \\alpha}{\\alpha\\beta}$$\n\n"
                            "हम जानते हैं कि $(\\beta - \\alpha)^2 = (\\alpha + \\beta)^2 - 4\\alpha\\beta = (-1)^2 - 4(-2) = 1 + 8 = 9$ है।\n"
                            "इसलिए, $\\beta - \\alpha = \\pm 3$ है।\n\n"
                            "**अंतिम उत्तर:** $\\mathbf{\\pm\\frac{3}{2}}$ (या पुस्तक के अनुसार $\\mathbf{-\\frac{3}{2}}$)"
                        )
                    else:
                        ans = (
                            "### 📝 **Step-by-Step Solution - Question 6**\n\n"
                            "For the given polynomial: $\\alpha + \\beta = -1$ and $\\alpha\\beta = -2$.\n\n"
                            "**Calculation:**\n"
                            "$$\\frac{1}{\\alpha} - \\frac{1}{\\beta} = \\frac{\\beta - \\alpha}{\\alpha\\beta}$$\n\n"
                            "Using identity: $(\\beta - \\alpha)^2 = (\\alpha + \\beta)^2 - 4\\alpha\\beta = (-1)^2 - 4(-2) = 9$.\n"
                            "Therefore, $\\beta - \\alpha = \\pm 3$.\n\n"
                            "**Final Answer:** $\\mathbf{\\pm\\frac{3}{2}}$"
                        )
                
                if generate_practice:
                    ans += (
                        "\n\n---\n### 🎯 **Practice Challenge**\n"
                        "If $\\alpha$ and $\\beta$ are the zeros of the quadratic polynomial $f(x) = x^2 + 2x - 3$, "
                        "find the value of $\\frac{1}{\\alpha} - \\frac{1}{\\beta}$ without using a calculator."
                    )
                
                st.markdown(ans)
                st.session_state.messages.append({"role": "assistant", "content": ans})
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

# MAIN INTERFACE
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

    # Display past chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept new user prompt
    if user_prompt := st.chat_input("Ask a question, or type 'Analyze upload'"):
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        # Process response locally with conditional dialogue matching
        with st.chat_message("assistant"):
            with st.spinner("Analyzing data vectors..."):
                import time
                time.sleep(1.2)
                
                # Standardize input for checking rules
                clean_prompt = user_prompt.lower().strip("?.! ")
                
                # RULE 1: Greetings Match
                if clean_prompt in ["hi", "hii", "hello", "hey", "greetings"]:
                    if language == "Hindi (हिंदी)":
                        ans = "नमस्ते! मैं आपका एआई लर्निंग लैब गाइड हूँ। आप मुझसे कोई भी सवाल पूछ सकते हैं।"
                    elif language == "Punjabi (ਪੰਜਾਬੀ)":
                        ans = "ਸਤਿ ਸ਼੍ਰੀ ਅਕਾਲ! ਮੈਂ ਤੁਹਾਡਾ ਐਲਆਈ ਲਰਨਿੰਗ ਲੈਬ ਗਾਈਡ ਹਾਂ। ਤੁਸੀਂ ਮੇਰੇ ਤੋਂ ਕੋਈ ਵੀ ਸਵਾਲ ਪੁੱਛ ਸਕਦੇ ਹੋ।"
                    elif language == "Hinglish":
                        ans = "Hello! Main aapka AI learning assistant hoon. Aap mujhse koi bhi question pooch sakte hain."
                    else:
                        ans = "Hello! Welcome to the Interactive Learning Lab. I am your specialized AI tutor. How can I help you today?"
                
                # RULE 2: "How are you?" Match
                elif any(phrase in clean_prompt for phrase in ["how are you", "how r u", "how are you doing", "kaise ho"]):
                    if language == "Hindi (हिंदी)":
                        ans = "मैं बिल्कुल ठीक हूँ, धन्यवाद! आपकी पढ़ाई में आज मैं आपकी क्या मदद कर सकता हूँ?"
                    elif language == "Punjabi (ਪੰਜਾਬੀ)":
                        ans = "ਮੈਂ ਬਿਲਕੁਲ ਠੀਕ ਹਾਂ, ਧੰਨਵਾਦ! ਤੁਹਾਡੀ ਪੜ੍ਹਾਈ ਵਿੱਚ ਅੱਜ ਮੈਂ ਕੀ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ?"
                    elif language == "Hinglish":
                        ans = "Main ekdum badhiya hoon! Aap batao, aaj aapki studies me kya help chahiye?"
                    else:
                        ans = "I am operating at peak efficiency, thank you! Ready to assist you with conceptual explanations, vision analysis, or test preparation."
                
                # RULE 3: "What/Who are you?" Match
                elif any(phrase in clean_prompt for phrase in ["what are you", "who are you", "your name", "tum kaun ho"]):
                    if language == "Hindi (हिंदी)":
                        ans = "मैं **EduBot Pro** हूँ, एक आधुनिक विज़न-आधारित एआई ट्यूटर जो जटिल समीकरणों और धारणाओं को आसानी से समझाने के लिए बनाया गया है।"
                    elif language == "Punjabi (ਪੰਜਾਬੀ)":
                        ans = "ਮੈਂ **EduBot Pro** ਹਾਂ, ਇੱਕ ਆਧੁਨਿਕ ਵਿਜ਼ਨ-ਅਧਾਰਿਤ ਏਆਈ ਟਿਊਟਰ ਜੋ ਗੁੰਝਲਦਾਰ ਸਵਾਲਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਸਮਝਾਉਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ।"
                    elif language == "Hinglish":
                        ans = "Mera naam **EduBot Pro** hai. Main ek next-generation AI Vision Tutor assistant hoon jo aapko math complex explanations sikhane me help karta hoon."
                    else:
                        ans = "I am **EduBot Pro**, an exhibition-grade Intelligent Vision Tutor designed for next-gen interactive learning and concept mapping."
                
                # FALLBACK RULE: If it's a math query, run the standard math simulation
                else:
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

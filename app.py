import streamlit as st
from PIL import Image
import re

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
    user_prompt = st.chat_input("Ask a question, or type 'Analyze upload'")
    
    if user_prompt:
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        # Process response locally
        with st.chat_message("assistant"):
            with st.spinner("Analyzing data vectors..."):
                import time
                time.sleep(1.2)
                
                clean_prompt = user_prompt.lower().strip("?.! ")
                
                # --- CHAT & GREETINGS DETECTOR ---
                if clean_prompt in ["hi", "hii", "hello", "hey", "greetings"]:
                    if language == "Hindi (हिंदी)":
                        ans = "नमस्ते! मैं आपका एआई लर्निंग लैब गाइड हूँ। आप मुझसे कोई भी सवाल पूछ सकते हैं।"
                    elif language == "Punjabi (ਪੰਜਾਬੀ)":
                        ans = "ਸਤਿ ਸ਼੍ਰੀ ਅਕਾਲ! ਮੈਂ ਤੁਹਾਡਾ ਐਲਆਈ ਲਰਨਿੰਗ ਲੈਬ ਗਾਈਡ ਹਾਂ। ਤੁਸੀਂ ਮੇਰੇ ਤੋਂ ਕੋਈ ਵੀ ਸਵਾਲ ਪੁੱਛ ਸਕਦੇ ਹੋ।"
                    elif language == "Hinglish":
                        ans = "Hello! Main aapka AI learning assistant hoon. Aap mujhse koi bhi question pooch sakte hain."
                    else:
                        ans = "Hello! Welcome to the Interactive Learning Lab. I am your specialized AI tutor. How can I help you today?"
                
                elif any(phrase in clean_prompt for phrase in ["how are you", "how r u", "kaise ho"]):
                    if language == "Hindi (हिंदी)":
                        ans = "मैं बिल्कुल ठीक हूँ, धन्यवाद! आपकी पढ़ाई में आज मैं आपकी क्या मदद कर सकता हूँ?"
                    elif language == "Punjabi (ਪੰਜਾਬੀ)":
                        ans = "ਮੈਂ ਬਿਲਕੁਲ ਠੀਕ ਹਾਂ, ਧੰਨਵਾਦ! ਤੁਹਾਡੀ ਪੜ੍ਹਾਈ ਵਿੱਚ ਅੱਜ ਮੈਂ ਕੀ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ?"
                    elif language == "Hinglish":
                        ans = "Main ekdum badhiya hoon! Aap batao, aaj aapki studies me kya help chahiye?"
                    else:
                        ans = "I am operating at peak efficiency, thank you! Ready to assist you with conceptual explanations, vision analysis, or test preparation."
                
                elif any(phrase in clean_prompt for phrase in ["what are you", "who are you", "tum kaun ho"]):
                    if language == "Hindi (हिंदी)":
                        ans = "मैं **EduBot Pro** हूँ, एक आधुनिक विज़न-आधारित एआई ट्यूटर जो जटिल समीकरणों और धारणाओं को आसानी से समझाने के लिए बनाया गया है।"
                    elif language == "Punjabi (ਪੰਜਾਬੀ)":
                        ans = "ਮੈਂ **EduBot Pro** ਹਾਂ, ਇੱਕ ਆਧੁਨਿਕ ਵਿਜ਼ਨ-ਅਧਾਰਿਤ ਏਆਈ ਟਿਊਟਰ ਜੋ ਗੁੰਝਲਦਾਰ ਸਵਾਲਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਸਮਝਾਉਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ।"
                    elif language == "Hinglish":
                        ans = "Mera naam **EduBot Pro** hai. Main ek next-generation AI Vision Tutor assistant hoon jo aapko math complex explanations sikhane me help karta hoon."
                    else:
                        ans = "I am **EduBot Pro**, an exhibition-grade Intelligent Vision Tutor designed for next-gen interactive learning and concept mapping."

                # --- DYNAMIC QUESTION PROCESSING ENGINE ---
                else:
                    display_topic = user_prompt.replace("solve", "").replace("Solve", "").replace("what is", "").replace("What is", "").strip("?.! ")
                    if not display_topic:
                        display_topic = "your query"

                    math_numbers = re.findall(r'\d+', clean_prompt)
                    num1 = math_numbers[0] if len(math_numbers) > 0 else "5"
                    num2 = math_numbers[1] if len(math_numbers) > 1 else "2"
                    
                    if learning_mode:
                        if language == "Hindi (हिंदी)":
                            ans = (
                                f"### 📚 **ट्यूटोरियल गाइड: {display_topic}**\n\n"
                                f"**चरण 1:** दिए गए विषय या समीकरण `{display_topic}` के मुख्य मानों और अवधारणाओं की पहचान करें।\n\n"
                                f"**चरण 2:** समस्या को सरल भागों में विभाजित करें। मुख्य आधार मानों की जाँच करें (उदाहरण: $a = {num1}, b = {num2}$)।\n\n"
                                f"**💡 संकेत (Hint):** सीधे उत्तर पर जाने के बजाय, बुनियादी सूत्रों का उपयोग करके संबंधों को हल करने का प्रयास करें। "
                                f"क्या आप आगे के चरणों की गणना स्वयं कर सकते हैं?"
                            )
                        elif language == "Punjabi (ਪੰਜਾਬੀ)":
                            ans = (
                                f"### 📚 **ਟਿਊਟੋਰਿਅਲ ਗਾਈਡ: {display_topic}**\n\n"
                                f"**ਕਦਮ 1:** ਦਿੱਤੇ ਗਏ ਵਿਸ਼ੇ ਜਾਂ ਸਮੀਕਰਨ `{display_topic}` ਦੇ ਮੁੱਖ ਮੁੱਲਾਂ ਅਤੇ ਸੰਕਲਪਾਂ ਦੀ ਪਛਾਣ ਕਰੋ।\n\n"
                                f"**ਕਦਮ 2:** ਸਮੱਸਿਆ ਨੂੰ ਸਰਲ ਭਾਗਾਂ ਵਿੱਚ ਵੰਡੋ। ਮੁੱਖ ਅਧਾਰ ਮੁੱਲਾਂ ਦੀ ਜਾਂਚ ਕਰੋ (ਉਦਾਹਰਣ: $a = {num1}, b = {num2}$)।\n\n"
                                f"**💡 ਇਸ਼ਾਰਾ (Hint):** ਸਿੱਧੇ ਜਵਾਬ 'ਤੇ ਜਾਣ ਦੀ ਬਜਾਏ, ਬੁਨਿਆਦੀ ਫਾਰਮੂਲਿਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਬੰਧਾਂ ਨੂੰ ਹੱਲ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ। "
                                f"ਕੀ ਤੁਸੀਂ ਅਗਲੇ ਕਦਮਾਂ ਦੀ ਗਣਨਾ ਖੁਦ ਕਰ ਸਕਦੇ ਹੋ?"
                            )
                        elif language == "Hinglish":
                            ans = (
                                f"### 📚 **Tutorial Guide: {display_topic}**\n\n"
                                f"**Step 1:** Diye gaye topic `{display_topic}` ke core elements aur variables ko closely identify karein.\n\n"
                                f"**Step 2:** Is topic ke important values ko mathematical structure me fit karein (Jaise: $x = {num1}, y = {num2}$).\n\n"
                                f"**💡 Hint:** Direct copy-paste karne ke bajaye, variables ke relation ko analyze karein aur step-by-step form use karke calculate karein!"
                            )
                        else:

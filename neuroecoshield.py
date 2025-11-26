import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time


st.set_page_config(
    page_title="NeuroEcoShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .st-emotion-cache-1y4p8pa {
        padding: 2rem;
    }
    h1 {
        color: #2c3e50;
    }
    h2 {
        color: #34495e;
    }
    .highlight-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .threat-text {
        color: #e74c3c;
        font-weight: bold;
    }
    .goal-text {
        color: #27ae60;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🛡️ NeuroEcoShield: Emotional Cybersecurity")
st.markdown("### A New Defence Against Digital Manipulation")
st.divider()


col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.header("⚠️ The Threat: Cognitive Hacking")
    st.markdown("""
    **Cognitive Hacking** involves attackers manipulating users' emotions to bypass technical security controls.
    
    *   **Attack Vector:** Emotional triggers (fear, urgency, greed).
    *   **Target:** The human mind, not just the device.
    *   **Mechanism:** Overwhelming critical thinking with physiological stress.
    """)
    st.image("https://img.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_138676-2387.jpg", caption="Cognitive Hacking Concept", width=300)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.header("⚙️ How It Works: Real-Time Biometric Correlation")
    st.markdown("""
    1.  **Browser Shield:** Analyses messages for risky cues (e.g., "Urgent action required!").
    2.  **Sensor Monitor:** Tracks physiological stress (Heart Rate Variability, Galvanic Skin Response).
    3.  **Correlation Engine:** Checks if a stress spike aligns with a risky message.
    """)
    st.info("💡 An alert is triggered ONLY when stress spikes correlate with a risky message.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.header("📉 The Reality: Critical Risks & Challenges")
    
    tab1, tab2, tab3 = st.tabs(["Technical Hurdle", "Efficacy Hurdle", "Ethical Hurdle"])
    
    with tab1:
        st.subheader("High Accuracy is Elusive")
        st.write("Reliably detecting stress (>98% accuracy) requires complex neuro-signals (EEG), not just simple wearables.")
        st.progress(60, text="Current Wearable Accuracy (~60%)")
        
    with tab2:
        st.subheader("Outsmarted by Modern AI")
        st.write("Static, rule-based systems cannot adapt to AI-generated, evolving social engineering attacks.")
        
    with tab3:
        st.subheader("A High-Risk Technology")
        st.write("Regulators warn that Emotion AI is 'immature' and poses risks to fairness and cognitive liberty.")
        st.warning("⚠️ Privacy Concern: Who owns your emotional data?")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.header("🎯 The Goal: Proactive Protection")
    st.markdown("""
    To prompt **critical evaluation** before a user falls victim to a manipulation attempt.
    
    > "The best firewall is a well-informed and calm mind."
    """)
    st.markdown('</div>', unsafe_allow_html=True)


st.divider()
st.header("🕹️ Live Simulation: Stress & Threat Detection")

sim_col1, sim_col2 = st.columns([2, 1])

with sim_col1:
    st.subheader("Real-time Biometric Data Stream")
  
    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame(columns=['Time', 'Stress Level'])
    
   
    new_time = len(st.session_state.data)
    new_stress = np.random.normal(50, 15) 
    

    is_attack = st.checkbox("Simulate Phishing Attack", value=False)
    if is_attack:
        new_stress += 40 
        new_stress = min(new_stress, 100)
        
    new_row = pd.DataFrame({'Time': [new_time], 'Stress Level': [new_stress]})
    st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)
    
    
    if len(st.session_state.data) > 50:
        st.session_state.data = st.session_state.data.iloc[1:]
        
    fig = px.line(st.session_state.data, x='Time', y='Stress Level', range_y=[0, 120], title="User Stress Level (HRV Proxy)")
    
 
    fig.add_hline(y=80, line_dash="dash", line_color="red", annotation_text="Stress Threshold")
    
    st.plotly_chart(fig, use_container_width=True)

with sim_col2:
    st.subheader("System Status")
    
    current_stress = st.session_state.data.iloc[-1]['Stress Level'] if not st.session_state.data.empty else 0
    
    st.metric(label="Current Stress Level", value=f"{current_stress:.1f}", delta=f"{current_stress - 50:.1f}")
    
    if current_stress > 80 and is_attack:
        st.error("🚨 ALERT: High Stress + Risky Content Detected!")
        st.markdown("**Action:** Pausing interaction. Please take a deep breath.")
    elif current_stress > 80:
        st.warning("⚠️ High Stress Detected. No external threat found.")
    else:
        st.success("✅ System Normal. User is calm.")

    if st.button("Reset Simulation"):
        st.session_state.data = pd.DataFrame(columns=['Time', 'Stress Level'])
        st.rerun()

st.divider()
st.caption("© 2024 NeuroEcoShield Prototype | Concept based on Emotional Cybersecurity Research")

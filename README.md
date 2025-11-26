# NeuroEcoShield & Chatbot Dashboard

This repository contains Streamlit-based applications for Emotional Cybersecurity visualization and an AI-powered Chatbot.

## 🛡️ NeuroEcoShield

**NeuroEcoShield** is a dashboard designed to visualize the concept of "Emotional Cybersecurity" - a new defence against digital manipulation and cognitive hacking.

### Features

- **The Threat**: Educational section on Cognitive Hacking and how attackers manipulate emotions.
- **The Reality**: Analysis of technical, efficacy, and ethical hurdles in detecting emotional manipulation.
- **How It Works**: Visual explanation of Real-Time Biometric Correlation.
- **Live Simulation**: An interactive module to simulate user stress levels and "Phishing Attacks" to demonstrate how the system triggers alerts based on physiological stress correlation.

### How to Run

```bash
streamlit run neuroecoshield.py
```

---

## 🤖 Chatbot Dashboard

A Streamlit-based dashboard integrated with Google's Gemini AI for real-time conversational capabilities.

### Features

- **Gemini AI Integration**: Powered by Google's Gemini 2.0 Flash model.
- **Chat Interface**: Clean, chat-like interface for interacting with the AI.
- **History**: Maintains session history for the conversation.

### How to Run

```bash
streamlit run chatbot.py
# OR
streamlit run DASHBOARD.py
```

---

## 🛠️ Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/CREATORRADHEY/NEURO_ECO_SHIELD.git
    cd NEURO_ECO_SHIELD
    ```

2.  **Install dependencies:**

    ```bash
    pip install streamlit google-generativeai pandas plotly
    ```

3.  **API Key Configuration:**
    - For the Chatbot, ensure you have a valid Google Gemini API key configured in the script or environment variables.

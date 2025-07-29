# medAce-analyzer
“Web-based medical report analyzer using rule‑based parsing and AI for clinical insights”
# 🩺 MedAce – Smart Medical Report Analyzer

A smart AI-powered web app that analyzes and summarizes medical reports, extracts health metrics, and answers health-related questions — all from a simple upload.

---

## 🧠 Problem Summary

Many patients receive their lab reports but struggle to interpret the medical jargon, metrics, or implications. Traditional healthcare systems don’t always provide personalized, instant explanations.

**MedAce bridges this gap** by:
- Automatically extracting key lab results (e.g., Hemoglobin, WBC, Glucose)
- Summarizing and flagging abnormalities
- Providing chatbot-style explanations using LLMs (Groq's LLaMA 3)
- Supporting multiple input formats (PDF, CSV, TXT, Images)

---

## ⚙️ Approach & Features

### ✅ Upload Any Medical Report
- Formats supported: PDF, CSV, PNG, JPG, TXT
- Text is parsed using `PyPDF2`, `Pandas`, and `Pillow`

### ✅ Auto-Metric Extraction
- Regex-based rule engine extracts key clinical metrics
- Flags abnormal values with colored indicators (🔴 / 🟢)

### ✅ Clinical Summary Generator
- Summary panel highlights health status in plain English
- Example: “Hemoglobin slightly below normal → consider iron panel.”

### ✅ AI Chatbot for Explanations (via **Groq + LLaMA3**)
- Ask questions like:
  - "What does a high creatinine mean?"
  - "Is my glucose level concerning?"
- Backed by Groq's lightning-fast `llama3-8b-8192` model

### ✅ Trends Section (Future Scope)
- Placeholder for tracking health over time with multiple uploads

---

## 🧪 Tech Stack

| Layer         | Tools/Libs Used                         |
|---------------|------------------------------------------|
| Frontend      | Streamlit                               |
| Parsing       | PyPDF2, Pillow, Pandas, regex            |
| AI Chatbot    | Groq SDK with LLaMA3                     |
| DevOps        | Git, GitHub                              |

---

## 📦 Project Structure

<img width="513" height="441" alt="image" src="https://github.com/user-attachments/assets/85831cbd-7f44-417e-a90c-eb4c9342dd57" />

# Future Scope
🚀 
Add patient authentication + profile history

Enable direct WhatsApp or PDF summary sharing

Add symptom-based chatbot (HuggingFace + health prompts)

Support 100+ labs with JSON mapping and ontology


# Final Thoughts
MedAce bridges the gap between medical jargon and patient understanding. We believe health data should be transparent, AI-interpretable, and user-friendly.
This project isn't just a hackathon submission — it’s a prototype with real-world potential.

# Streamlit-App-link:
https://medace-analyzer-jnlwcmpexmkknhgg2e86we.streamlit.app/

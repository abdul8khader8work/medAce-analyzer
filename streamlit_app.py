# import streamlit as st
# import PyPDF2
# import pandas as pd
# from PIL import Image
# import io
# import matplotlib.pyplot as plt
# import re

# # Page settings
# st.set_page_config(page_title="MedAce", layout="wide")
# st.title("🩺 MedAce - Smart Medical Report Analyzer")
# st.write("Welcome! Upload your Medical Report to begin.")

# # Parsing helper (inline, no report_parser.py)
# def extract_metrics_from_text(text: str) -> dict:
#     patterns = {
#         "Hemoglobin":       r"hemoglobin[:\s]*([\d.]+)",
#         "WBC":              r"wbc[:\s]*([\d,]+)",
#         "Platelets":        r"platelets[:\s]*([\d,]+)",
#         "RBC":              r"rbc[:\s]*([\d.]+)",
#         "Blood Pressure":   r"blood pressure[:\s]*([\d/]+)",
#         "Glucose":          r"glucose[:\s]*([\d.]+)",
#         "Creatinine":       r"creatinine[:\s]*([\d.]+)",
#         "Cholesterol":      r"cholesterol[:\s]*([\d.]+)",
#         "Anti‑CCP":         r"anti[-\s]?ccp[:\s]*([\d.]+)"
#     }
#     results = {}
#     for name, pat in patterns.items():
#         m = re.search(pat, text, re.IGNORECASE)
#         if m:
#             results[name] = m.group(1)
#     return results

# # Layout
# left_col, right_col = st.columns([1, 2])

# with left_col:
#     st.header("Upload Report")
#     uploaded_file = st.file_uploader(
#         "Choose a Medical Report",
#         type=["pdf", "csv", "png", "jpg", "jpeg", "txt"],
#         help="Upload your medical report here (PDF, Image, or Text)."
#     )
#     if uploaded_file:
#         st.success("File Uploaded Successfully.")
#         st.markdown(f"**Filename:** `{uploaded_file.name}`")

# with right_col:
#     st.header("Report Summary")
#     if uploaded_file:
#         # read raw text
#         text = ""
#         name = uploaded_file.name.lower()
#         if name.endswith(".pdf"):
#             reader = PyPDF2.PdfReader(uploaded_file)
#             for page in reader.pages:
#                 text += page.extract_text() or ""
#         elif name.endswith(".csv"):
#             df = pd.read_csv(uploaded_file)
#         elif name.endswith((".png", ".jpg", ".jpeg")):
#             image = Image.open(uploaded_file)
#         else:
#             text = uploaded_file.read().decode("utf-8", errors="ignore")

#         # show extracted text/csv/image
#         if name.endswith(".csv"):
#             st.markdown("### Report Table")
#             st.dataframe(df)
#         elif name.endswith((".png", ".jpg", ".jpeg")):
#             st.markdown("### Uploaded Image")
#             st.image(image, use_column_width=True)
#         else:
#             if text:
#                 st.markdown("### Extracted Text")
#                 st.text_area("", text, height=200)
#             else:
#                 st.warning("No text could be extracted.")

#         # extract metrics
#         metrics = extract_metrics_from_text(text)
#         if metrics:
#             st.markdown("### 🔍 Key Findings")
#             for k, v in metrics.items():
#                 # simple normal/abnormal check for demo
#                 abnormal = False
#                 if k == "Hemoglobin" and float(v) < 12:
#                     abnormal = True
#                 cls = "🔴" if abnormal else "🟢"
#                 st.write(f"{cls} **{k}:** {v}")
#         else:
#             st.info("No classic labs found—check your report format.")

#         # dummy summary and alerts
#         st.markdown("### Summary")
#         if metrics.get("Hemoglobin") and float(metrics["Hemoglobin"]) < 12:
#             st.warning("Hemoglobin slightly below normal → consider iron panel.")
#         else:
#             st.success("All observed values within normal ranges.")

#         # trends placeholder
#         st.markdown("### Trends Over Time")
#         st.info("Upload more reports to see trends here.")

#         # Download
#         st.markdown("### Download Your Summary")
#         summary_txt = "MedAce Summary\n" + "\n".join(f"{k}: {v}" for k, v in metrics.items())
#         st.download_button("Download .txt", data=summary_txt, file_name="medace_summary.txt")

#     else:
#         st.info("Analysis and visualizations will appear here once a file is uploaded.")




















































import streamlit as st
import openai
import pandas as pd
import PyPDF2
from PIL import Image
import io

st.set_page_config(page_title="Smart Medical Report Upload", layout="wide")

# Load OpenAI key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🩺 Smart Medical Report Upload & Analysis")

uploaded_file = st.file_uploader("📤 Upload Medical Report", type=["pdf"], key="fileUploader")

if uploaded_file:
    # Display uploaded PDF file
    st.success(f"✅ File uploaded: {uploaded_file.name}")

    # Extract text from the PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("📄 Report Summary")
    st.text_area("Extracted Text", text, height=300)

    # AI Chatbot below the extracted summary
    st.markdown("### 💬 Ask MedAce (AI Chatbot)")
    user_query = st.text_input("Ask something about this report...")

    if user_query:
        with st.spinner("Thinking..."):
            try:
                st.write("API key loaded:", bool(openai.api_key))

                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful medical assistant who explains lab reports in simple language."},
                        {"role": "user", "content": f"The report contains:\n{text}\n\nUser asks: {user_query}"}
                    ]
                )
                answer = response.choices[0].message.content.strip()
                st.success(answer)
            except Exception as e:
                st.error(f"❌ Error: {e}")

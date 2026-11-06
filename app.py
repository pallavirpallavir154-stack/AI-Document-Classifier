import streamlit as st
import joblib
from pypdf import PdfReader

# Load trained ML model and TF-IDF vectorizer
model = joblib.load("document_classifier/model.pkl")
vectorizer = joblib.load("document_classifier/vectorizer.pkl")

# Document categories
categories = [
    'comp.graphics',
    'rec.sport.baseball',
    'sci.med',
    'talk.politics.misc'
]

# Page configuration
st.set_page_config(
    page_title="AI Document Classifier",
    page_icon="📄",
    layout="centered"
)

# Application title
st.title("📄 AI Document Classifier")

st.write(
    "Upload your document and let Machine Learning "
    "automatically identify its category."
)

st.divider()

# File uploader
uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "txt"],
    help="Supported formats: PDF and TXT"
)

if uploaded_file is not None:

    st.info(f"Uploaded File: {uploaded_file.name}")

    # Extract document text
    try:
        if uploaded_file.name.lower().endswith(".pdf"):
            reader = PdfReader(uploaded_file)

            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        else:
            text = uploaded_file.read().decode(
                "utf-8", errors="ignore"
            )

        if not text.strip():
            st.error("No readable text found in this document.")

        else:

            # Document preview
            with st.expander("View Document Preview"):
                st.text(text[:1500])

            # Classification button
            if st.button("🔍 Classify Document", use_container_width=True):

                # Convert text into TF-IDF features
                features = vectorizer.transform([text])

                # Predict category
                prediction = model.predict(features)

                probabilities = model.predict_proba(features)

                # FIX: Display category name instead of numeric label
                category = categories[int(prediction[0])]

                confidence = max(probabilities[0]) * 100

                # Display results
                st.success("Classification Completed!")

                st.subheader("📊 Prediction Result")

                st.metric(
                    label="Predicted Category",
                    value=category
                )

                st.metric(
                    label="Prediction Confidence",
                    value=f"{confidence:.2f}%"
                )

                st.progress(float(confidence / 100))

                # Display all category probabilities
                st.subheader("Category-wise Confidence")

                for i, name in enumerate(categories):
                    st.write(
                        f"**{name}:** {probabilities[0][i] * 100:.2f}%"
                    )

    except Exception as e:
        st.error(f"Error processing document: {e}")

st.divider()

st.caption(
    "AI Document Classifier | Built using Python, "
    "Machine Learning, NLP and Streamlit"
)
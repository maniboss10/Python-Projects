
import streamlit as st

from api_client import check_backend_health


st.set_page_config(
    page_title="Hybrid RAG Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("Hybrid RAG Assistant")

st.subheader("FAISS + Neo4j Knowledge Graph")

st.info("Stage 1 — Foundation and API Connectivity")

st.divider()

st.header("Backend Connection")

if st.button("Check Backend Connection"):

    result = check_backend_health()

    if result["success"]:

        backend_data = result["data"]

        st.success("Backend Connected Successfully!")

        st.write(
            "Status:",
            backend_data["status"]
        )

        st.write(
            "Service:",
            backend_data["service"]
        )

        st.write(
            "Version:",
            backend_data["version"]
        )

    else:
        st.error("Unable to connect to backend.")
        st.warning(
            "Make sure FastAPI is running on port 8000."
        )

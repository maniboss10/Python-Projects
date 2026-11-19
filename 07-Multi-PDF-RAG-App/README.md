# Multi-PDF RAG Application

Upload several text-based PDFs, ask a question across them, and see the original filename, page number, and supporting excerpt for each cited passage.

## Setup and launch

From the repository root, enter the project folder. Create the virtual environment and install dependencies when setting up a fresh checkout.

```powershell
Set-Location .\07-Multi-PDF-RAG-App
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --only-binary=:all: -r requirements.txt
```

Set `OPENAI_API_KEY` in the project's ignored `.env` file using `.env.example` as a template. The app loads `.env` from the same folder as `rag_app.py`. An existing PowerShell environment value takes precedence. Restart Streamlit after changing the key.

To set the key in PowerShell instead, use this prompt to hide it as you enter it:

```powershell
$env:OPENAI_API_KEY = [System.Net.NetworkCredential]::new('', (Read-Host 'OpenAI API key' -AsSecureString)).Password
```

Start Streamlit:

```powershell
python -m streamlit run rag_app.py
```

If activation is unavailable, use `.\.venv\Scripts\python.exe -m streamlit run rag_app.py`.

## How the app works

1. **PDF loading.** LangChain's `PyPDFLoader` uses pypdf to extract pages from each upload. The app uses temporary paths, removes them after extraction, and replaces those paths in metadata with the original filenames. It keeps the original zero-based page index even when a blank page is skipped.
2. **Chunking.** `RecursiveCharacterTextSplitter` creates chunks of up to 1,000 characters with a target overlap of 150. It prefers natural text boundaries, and overlap helps preserve context around splits. Each chunk inherits its page metadata.
3. **Embeddings and indexing.** An embedding is a numeric representation of text that supports comparison by meaning. `OpenAIEmbeddings` embeds every chunk and FAISS stores the vectors in one in-memory index, alongside links back to the text and metadata. A vector database makes those representations searchable.
4. **Similarity search.** When you click **Ask**, the app embeds the question and retrieves up to eight nearby chunks across the combined collection. Similarity ranks candidates. A high rank alone does not establish that a passage supports an answer.
5. **Generation and citations.** Traditional LLM question answering sends a question directly to a model. Retrieval-augmented generation (RAG) also supplies relevant excerpts. The app asks `ChatOpenAI` for an answer, an evidence status, and verbatim excerpts. It validates each excerpt against the selected passage and uses the original metadata to render deduplicated filename and one-based page citations. The model is instructed to report insufficient evidence or explain conflicting accounts. Excerpt matching verifies provenance. Judging whether those excerpts support every claim still depends on the model and the retrieved context.

The index and latest answer stay in Streamlit session state across reruns. Click **Process PDFs** to build an index. Changing the uploaded filenames or contents clears it and the previous answer. Starting a new session requires indexing again.

The app uses `gpt-4o-mini` for chat and the pinned `langchain-openai` default `text-embedding-ada-002` for embeddings. Your OpenAI project needs access to both. To use a different chat model that supports function calling, set `OPENAI_CHAT_MODEL` in `.env` and restart Streamlit.

## Errors and verification

Unreadable and textless PDFs are reported and skipped. Scanned pages need OCR before upload. The app handles missing credentials, authentication failures, quota limits, rate limits, network failures, indexing failures, and questions submitted before indexing. API errors are summarized in the interface.

```powershell
python -m py_compile rag_app.py
python -m pip check
python -c "import streamlit, faiss, pypdf; from langchain_community.document_loaders import PyPDFLoader; from langchain_openai import ChatOpenAI, OpenAIEmbeddings"
```

For a live check, use two small PDFs with different answers to the same question. Confirm that both filenames appear in the index summary, then ask about the discrepancy and compare both quoted excerpts against the original pages. Processing uploads sends extracted chunks to OpenAI for embedding. Asking a question sends a query for embedding and retrieved excerpts to the chat model. Both operations can incur charges.

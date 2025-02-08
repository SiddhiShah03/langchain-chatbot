from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings  # ✅ Updated import


def create_vector_store(documents):
    # Extract text from documents
    texts = [doc.page_content for doc in documents]

    # Initialize embeddings model
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings_model = HuggingFaceEmbeddings(model_name=model_name)

    # Generate embeddings
    embeddings = embeddings_model.embed_documents(texts)

    # Debug: Print shapes to check if they match
    print(f"Texts Count: {len(texts)}, Embeddings Count: {len(embeddings)}")

    # Ensure `texts` and `embeddings` have the same length
    if len(texts) != len(embeddings):
        raise ValueError("Mismatch between texts and embeddings")

    # Create FAISS index
    faiss_index = FAISS.from_texts(texts, embeddings_model)

    return faiss_index

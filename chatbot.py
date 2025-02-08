from sentence_transformers import SentenceTransformer


def get_answer(vector_store, query):
    print("Query received:", query)  # Debugging
    print("Vector store:", vector_store)  # Debugging

    # Ensure vector store is valid
    if vector_store is None:
        return "Error: Vector store not initialized."

    try:
        response = vector_store.similarity_search(query, k=1)  # Adjust k if needed
        print("Response:", response)  # Debugging
        return response[0].page_content if response else "No relevant answer found."
    except Exception as e:
        print("Error in get_answer:", str(e))
        return "Error processing the request."

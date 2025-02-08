from langchain_community.document_loaders import WebBaseLoader
import os

def extract_data(url):
    url = "https://brainlox.com/courses/category/technical"
    
    os.environ["USER_AGENT"] = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    
    loader = WebBaseLoader(url)
    documents = loader.load()  # Extract text
    return documents

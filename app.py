from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from extractor import extract_data
from vector_store import create_vector_store
from chatbot import get_answer

app = Flask(__name__)
api = Api(app)

# ✅ Home route to check if the app is running
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the LangChain Chatbot!"})

# ✅ Try to load data and create the vector store safely
try:
    url = "https://brainlox.com/courses/category/technical"
    documents = extract_data(url)
    vector_store = create_vector_store(documents)
    print("✅ Vector store created successfully!")  # Debugging message
except Exception as e:
    print(f"❌ Error initializing vector store: {e}")
    vector_store = None  # Ensure the app still runs

# ✅ Define the Chatbot API route
class Chatbot(Resource):
    def post(self):
        global vector_store  # Use the global vector store variable
        if vector_store is None:
            url = "https://brainlox.com/courses/category/technical"
            documents = extract_data(url)
            vector_store = create_vector_store(documents)  # Recreate if needed
        
        data = request.get_json()
        query = data.get("question")
        
        if not query:
            return jsonify({"error": "No question provided"}), 400

        answer = get_answer(vector_store, query)  # Might be failing here
        return jsonify({"response": answer})
    
api.add_resource(Chatbot, "/chat")

# ✅ Print all registered routes for debugging
print("Registered Routes:", app.url_map)

if __name__ == "__main__":
    app.run(debug=True)

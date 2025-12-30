from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app, origins=[
    "http://127.0.0.1:5500",
    "https://michischwarz.github.io"
])

@app.get("/") 
def home(): 
    return "Backend is running!"

@app.get("/api/random")
def random_number():
    number = random.randint(0, 100)
    return jsonify({"number": number})

if __name__ == "__main__":
    app.run(debug=True)


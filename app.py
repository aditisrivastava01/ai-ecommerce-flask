from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

products = [
    {"id": 1, "name": "Smart Watch", "price": 2999, "img": "https://m.media-amazon.com/images/I/71x5aYkz7KL._SX679_.jpg"},
    {"id": 2, "name": "Laptop", "price": 45999, "img": "https://m.media-amazon.com/images/I/71k3N8j7mIL._SX679_.jpg"},
    {"id": 3, "name": "Headphones", "price": 1999, "img": "https://m.media-amazon.com/images/I/61CGHv6kmWL._SX679_.jpg"},
    {"id": 4, "name": "Mobile Phone", "price": 14999, "img": "https://m.media-amazon.com/images/I/71xb2xkN5qL._SX679_.jpg"},
    {"id": 5, "name": "Keyboard", "price": 999, "img": "https://m.media-amazon.com/images/I/61l9ppRIiqL._SX679_.jpg"},
    {"id": 6, "name": "Mouse", "price": 499, "img": "https://m.media-amazon.com/images/I/61UxfXTUyvL._SX679_.jpg"},
    {"id": 7, "name": "Bluetooth Speaker", "price": 2499, "img": "https://m.media-amazon.com/images/I/71rZ0P6I4JL._SX679_.jpg"},
    {"id": 8, "name": "Power Bank", "price": 1799, "img": "https://m.media-amazon.com/images/I/71lVwl3q-kL._SX679_.jpg"}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower()

    if "price" in user_msg:
        reply = "All prices are shown below each product."
    elif "delivery" in user_msg:
        reply = "Delivery takes 3-5 working days 🚚"
    elif "return" in user_msg:
        reply = "7-day easy return policy ✅"
    elif "hello" in user_msg or "hi" in user_msg:
        reply = "Hello 👋 How can I help you?"
    else:
        reply = "Sorry, I can answer about price, delivery & return."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

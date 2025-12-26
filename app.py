from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

products = [
    {"id": 1, "name": "Smart Watch", "price": 2999, "img": "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b"},
    {"id": 2, "name": "Laptop", "price": 45999, "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8"},
    {"id": 3, "name": "Headphones", "price": 1999, "img": "https://images.unsplash.com/photo-1518444028785-8f6a2a0c4b3e"},
    {"id": 4, "name": "Mobile Phone", "price": 14999, "img": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"},
    {"id": 5, "name": "Keyboard", "price": 899, "img": "https://images.unsplash.com/photo-1587829741301-dc798b83add3"},
    {"id": 6, "name": "Mouse", "price": 499, "img": "https://images.unsplash.com/photo-1586810724476-c294fb7ac01b"},
    {"id": 7, "name": "Bluetooth Speaker", "price": 2499, "img": "https://images.unsplash.com/photo-1585386959984-a41552231693"},
    {"id": 8, "name": "Power Bank", "price": 1799, "img": "https://images.unsplash.com/photo-1609592064493-1aa6f07b9a2e"}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message", "").lower()

    if "price" in msg:
        return jsonify({"reply": "All prices are mentioned below each product 🙂"})
    elif "delivery" in msg:
        return jsonify({"reply": "Delivery takes 3–5 working days 🚚"})
    elif "return" in msg:
        return jsonify({"reply": "7 days easy return policy 🔁"})
    else:
        return jsonify({"reply": "I can help with prices, delivery and return policy 💬"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

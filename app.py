from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Home page – products
@app.route("/")
def index():
    products = [
        {
            "name": "Phone",
            "price": "₹15,000",
            "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
        },
        {
            "name": "Laptop",
            "price": "₹55,000",
            "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8"
        },
        {
            "name": "Headphones",
            "price": "₹2,000",
            "image": "https://images.unsplash.com/photo-1518441986440-e0d88c70a3a7"
        }
    ]
    return render_template("index.html", products=products)


# Chatbot API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    if "price" in user_message:
        reply = "Prices are mentioned below each product."
    elif "delivery" in user_message:
        reply = "Delivery takes 3-5 business days."
    elif "return" in user_message:
        reply = "7 days easy return policy available."
    elif "hello" in user_message or "hi" in user_message:
        reply = "Hello! How can I help you today?"
    else:
        reply = "I can help with price, delivery, and return policy."

    return jsonify({"reply": reply})


# Render port binding (VERY IMPORTANT)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

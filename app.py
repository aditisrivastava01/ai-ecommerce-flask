from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

products = {
    "phone": {
        "price": 15000,
        "image": "https://tse2.mm.bing.net/th/id/OIP.HbHLWFcUM4Cl5htyeWe7zAHaFJ?pid=Api&P=0&h=180"
    },
    "laptop": {
        "price": 55000,
        "image": "https://tse4.mm.bing.net/th/id/OIP.AkmVpbepWUKtdZEo8m7ilwHaFW?pid=Api&P=0&h=180"
    },
    "headphones": {
        "price": 2000,
        "image": "https://tse1.mm.bing.net/th/id/OIP.H8rRfXMFSfNuV1sHkU9cLAHaHa?pid=Api&P=0&h=180"
    },
    "watch": {
        "price": 3000,
        "image": "https://images.macrumors.com/t/5qniIh0ci_t8vWfp7RjUzVXQI2I=/2500x/article-new/2023/08/Apple-Watch-Series-9-Pink-Aluminum-Feature.jpg"
    }
}

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"].lower()

    if "hi" in msg or "hello" in msg:
        reply = "Hello 😊 How can I help you?"

    elif "price" in msg:
        for name in products:
            if name in msg:
                reply = f"{name.capitalize()} price is ₹{products[name]['price']}"
                break
        else:
            reply = "Please ask like: phone price, watch price"

    elif "delivery" in msg:
        reply = "Delivery takes 3–5 working days 🚚"

    elif "return" in msg:
        reply = "7 days easy return policy."

    else:
        reply = "Ask me about product price, delivery or return."

    return jsonify({"reply": reply})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




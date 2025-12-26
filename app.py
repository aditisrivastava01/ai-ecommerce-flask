from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

products = [
    {"id": 1, "name": "Smart Watch", "price": 2999, "img": "https://tse2.mm.bing.net/th/id/OIP.Cgg7x4IfpiNhCdalpA8DOQHaHc?rs=1&pid=ImgDetMain&o=7&rm=3"},
    {"id": 2, "name": "Laptop", "price": 45999, "img": "https://th.bing.com/th/id/OIP.gnT4D66Rj_LIWsmehIDxzgHaGS?o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3"},
    {"id": 3, "name": "Headphones", "price": 1999, "img": "https://tse3.mm.bing.net/th/id/OIP.pgzU33CxcqL3NvDutVnJTgHaI0?rs=1&pid=ImgDetMain&o=7&rm=3"},
    {"id": 4, "name": "Mobile Phone", "price": 14999, "img": "https://tse2.mm.bing.net/th/id/OIP.6sZV_t2bmKn_yeuegDnKYwHaEL?rs=1&pid=ImgDetMain&o=7&rm=3"},
    {"id": 5, "name": "Keyboard", "price": 899, "img": "https://th.bing.com/th/id/OIP.rOPB8zwx14GQjoe9sURbcwHaEK?o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3"},
    {"id": 6, "name": "Mouse", "price": 499, "img": "https://tse2.mm.bing.net/th/id/OIP.0-KIptBohQtxzXbKAKqUFAHaFM?rs=1&pid=ImgDetMain&o=7&rm=3"},
    {"id": 7, "name": "Bluetooth Speaker", "price": 2499, "img": "https://m.media-amazon.com/images/I/71pECjS2piL._AC_SL1500_.jpg"},
    {"id": 8, "name": "Power Bank", "price": 1799, "img": "https://m.media-amazon.com/images/I/61sautq2miL._AC_SL1500_.jpg"}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message", "").lower()

    if "price" in msg:
        return jsonify({"reply": "All prices are mentioned below each product "})
    elif "delivery" in msg:
        return jsonify({"reply": "Delivery takes 3–5 working days "})
    elif "return" in msg:
        return jsonify({"reply": "7 days easy return policy "})
    else:
        return jsonify({"reply": "I can help with prices, delivery and return policy "})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


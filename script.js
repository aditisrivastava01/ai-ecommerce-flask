let cart = [];

function addToCart(item) {
    cart.push(item);
    renderCart();
}

function renderCart() {
    let list = document.getElementById("cartList");
    list.innerHTML = "";
    cart.forEach(i => {
        let li = document.createElement("li");
        li.innerText = i;
        list.appendChild(li);
    });
}

function sendMsg() {
    let msgInput = document.getElementById("msg");
    let msg = msgInput.value;
    if (msg === "") return;

    let chat = document.getElementById("chat");
    chat.innerHTML += "<p><b>You:</b> " + msg + "</p>";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        chat.innerHTML += "<p><b>Bot:</b> " + data.reply + "</p>";
        chat.scrollTop = chat.scrollHeight;
    });

    msgInput.value = "";
}

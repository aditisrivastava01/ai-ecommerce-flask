let cartCount = 0;

function addToCart() {
    cartCount++;
    document.getElementById("cart-count").innerText = cartCount;
}

function sendMessage() {
    const input = document.getElementById("chat-input");
    const message = input.value.trim();
    if (message === "") return;

    const chatBox = document.getElementById("chat-messages");
    chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        chatBox.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    input.value = "";
}

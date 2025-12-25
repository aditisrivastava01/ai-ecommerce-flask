document.addEventListener("DOMContentLoaded", function () {
    const sendBtn = document.getElementById("sendBtn");
    const userInput = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");

    if (!sendBtn || !userInput || !chatBox) {
        console.error("Chat elements not found in HTML");
        return;
    }

    sendBtn.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = userInput.value.trim();
        if (message === "") return;

        // Show user message
        chatBox.innerHTML += `
            <div class="user-msg">
                <b>You:</b> ${message}
            </div>
        `;

        userInput.value = "";

        // Send message to Flask backend
        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `
                <div class="bot-msg">
                    <b>Bot:</b> ${data.reply}
                </div>
            `;
            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch(error => {
            console.error("Error:", error);
            chatBox.innerHTML += `
                <div class="bot-msg">
                    <b>Bot:</b> Sorry, something went wrong.
                </div>
            `;
        });
    }
});

var stompClient = null;

function connect() {
    let name = $("#name-value").val();
    localStorage.setItem("name", name);
    let socket = new SockJS("/server");
    stompClient = Stomp.over(socket);
    stompClient.connect({}, function (frame) {
        console.log("connected: " + frame);
        $("#name-from").addClass('d-none');
        $("#chat-room").removeClass('d-none');
        $("#name-title").html(`Welcome, <b>${name}</b>`);
        stompClient.subscribe("/topic/return", function (response) {
            showMessage(JSON.parse(response.body));
        });
    });
}

function showMessage(message) {
    let messageContainer = $(".message-container");
    let messageClass = message.name === localStorage.getItem("name") ? "right" : "left";
    let messageBubble = `
        <div class="message-bubble ${messageClass} ${messageClass === 'left' ? 'left-align' : ''}">
            <b>${message.name}:</b> ${message.messageContent}
        </div><br>`; // Add a <br> tag to ensure each message is on a new line
    messageContainer.append(messageBubble);
    messageContainer.append("<br>"); // Add a <br> tag to separate messages
}




function sendMessage() {
    let name = $("#name-value").val(); // Get the user's name from the input field
    let messageContent = $("#message-value").val();
    let jsonObj = {
        name: name,
        messageContent: messageContent
    };
    stompClient.send("/app/message", {}, JSON.stringify(jsonObj));

    // Clear the input field after sending the message
    $("#message-value").val("");
}



$(document).ready((e) => {
    $("#login").click(() => {
        let name = $("#name-value").val()
        localStorage.setItem("name", name)
        $("#name-title").html(`Welcome , <b>${name} </b>`)
        connect();
    })
    $("#send-btn").click(() => {
        sendMessage()
    })

    $("#logout").click(() => {

        localStorage.removeItem("name")
        if (stompClient !== null) {
            stompClient.disconnect()

            $("#name-from").removeClass('d-none')
            $("#chat-room").addClass('d-none')
            console.log(stompClient)
        }

    })

})

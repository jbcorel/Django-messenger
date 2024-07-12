    const roomName = JSON.parse(document.getElementById('json-roomslug').textContent);
    const userName = JSON.parse(document.getElementById('json-username').textContent);
    const startConvoHTML = '<div id="start-conversation" class="p-4 bg-gray-200 rounded-xl">' +
                            '<p class="font-semibold">You</p>' + 
                            '<p class="">Start conversation...<p></div>';


    const chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/'
        + roomName
        + '/'
    );

    chatSocket.onmessage = (e) => {
        console.log(e)

        const data = JSON.parse(e.data);
        if (data.message) {
            let html = '<div class="p-4 bg-gray-200 rounded-xl">';
                html += '<p class="font-semibold">' + data.username + '</p>';
                html += '<p>' + data.message + '</p></div>';
                document.querySelector('#chat-messages').innerHTML += html;
        } else {
            alert('Empty message');
        };
    };

    chatSocket.onclose = (e) => {
        console.log('onclose triggered!')
    };

    document.getElementById('input-btn-send').onclick = (e) => {
        e.preventDefault();
        const messageInput = document.getElementById('chat-message-input');
        const message = messageInput.value;

        chatSocket.send(JSON.stringify ({
            'message': message,
            'room': roomName,
            'username': userName,
        }));

        messageInput.value = '';
        return false;
    };

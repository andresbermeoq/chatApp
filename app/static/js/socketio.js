document.addEventListener('DOMContentLoaded', () => {
  const socket = io();

  let room = "Publico";
  joinRoom("Publico");


  socket.on('message', data => {
    const p = document.createElement('p');
    const span_username = document.createElement('h4');
    const span_timestamp = document.createElement('h6');
    const span_message = document.createElement('p');
    const br = document.createElement('br');

    if(data.username){
      p.setAttribute("class", "my-msg card bg-light mb-3");
      p.setAttribute("style", "width: 18rem;");

      span_username.setAttribute("class", "card-header");
      span_username.innerHTML = data.username;

      span_timestamp.setAttribute("class","card-title");
      span_timestamp.innerHTML = data.time_stamp;

      span_message.setAttribute("class", "card-text");
      span_message.innerHTML = data.msg;


      p.innerHTML = span_username.outerHTML + span_timestamp.outerHTML + br.outerHTML + span_message.outerHTML;

      document.querySelector('#display-messages').append(p);
    } else if (typeof data.username != 'undefined') {
      p.setAttribute("class", "my-msg bg-info mb-3");
      p.setAttribute("style", "width: 18rem;");

      span_username.setAttribute("class", "card-header");
      span_username.innerHTML = data.username;

      span_timestamp.setAttribute("class","card-title");
      span_timestamp.innerHTML = data.time_stamp;

      span_message.setAttribute("class", "card-text");
      span_message.innerHTML = data.msg;


      p.innerHTML = span_username.outerHTML + span_timestamp.outerHTML + br.outerHTML + span_message.outerHTML;

      document.querySelector('#display-messages').append(p);
    } else {
      printSysMsg(data.msg);
    }

  });

  document.querySelector('#sendButton').onclick = () => {
    var myObject = {'msg': document.querySelector('#message').value,
                    'username': user, 'room': room}
    socket.send(myObject);

    document.querySelector('#message').value = '';
  }

  document.querySelectorAll('.select-room').forEach(p => {
    p.onclick = () => {
        let newRoom = p.innerHTML;
        // Check if user already in the room
        if (newRoom === room) {
            msg = `Usted ya se Encuentra chateando con ${room}.`;
            printSysMsg(msg);
        } else {
            leaveRoom(room);
            joinRoom(newRoom);
            room = newRoom;
        }
    };
  });

  function leaveRoom(room) {
    var objectLeave = {'username': user, 'room': room}
    socket.emit('leave', objectLeave);
  }


  function joinRoom(room) {
    var objectJoin = {'username': user, 'room': room}
    socket.emit('join', objectJoin);

    document.querySelector('#display-messages').innerHTML = '';

    document.querySelector('#message').focus();
  }

  function printSysMsg(msg) {
    const p = document.createElement('p');
    p.setAttribute("class", "h6");
    p.innerHTML = msg;
    document.querySelector('#display-messages').append(p);
  }

})



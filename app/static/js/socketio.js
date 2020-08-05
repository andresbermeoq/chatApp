document.addEventListener('DOMContentLoaded', () => {
  const socket = io();

  let room = "Publico";
  joinRoom("Publico");


  socket.on('message', data => {
    const p = document.createElement('div');
    const span_username = document.createElement('strong');
    const span_timestamp = document.createElement('span');
    const br = document.createElement('br');

    if(data.username){
      p.setAttribute("class", "my-msg");
      span_username.setAttribute("class", "my-username");
      span_username.innerHTML = data.username;
      span_timestamp.setAttribute("class", "timestamp");
      span_timestamp.innerHTML = data.time_stamp;
      p.innerHTML = span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML;
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
    p.innerHTML = msg;
    document.querySelector('#display-messages').append(p);
  }

})



document.addEventListener('DOMContentLoaded', () => {
  const socket = io();

  socket.on('message', data => {
    const p = document.createElement('p');
    const span_username = document.createElement('span');
    const span_timestamp = document.createElement('span');
    const br = document.createElement('br');
    span_username.innerHTML = data.username;
    span_timestamp.innerHTML = data.time_stamp;
    p.innerHTML = span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML;
    document.querySelector('#display-messages').append(p);

  });

  document.querySelector('#sendButton').onclick = () => {

    var myObject = {'msg': document.querySelector('#message').value,
                    'username': user}
    socket.send(myObject);
  }

})



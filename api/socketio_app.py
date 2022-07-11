from room import Room
from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'please_do_not_steal_it'

socketio = SocketIO(app, cors_allowed_origins="*", logger=False, engineio_logger=False)

active_rooms = {}

@socketio.on('connect')
def connect(auth):
    if auth == app.secret_key:
        emit('connect', 'Connected')
    else:
        emit('connect', 'Unauthorized')


@socketio.on('joinGame')
def on_join(data):
    nickname = data['nickname']
    sid = request.sid
    requested_room_name = data['room']

    if active_rooms.get(requested_room_name):
        active_room = active_rooms[requested_room_name]
        if active_room.is_room_available():
            if active_room.is_nickname_available(nickname):
                join_room(active_room.room_name)
                active_room.add_user(nickname)
                room_data = active_room.to_dict()
                emit('joinGameSelf', {'status': 'success', 'nickname': nickname }, to=sid)
                emit('joinGame', {'status': 'success', 'room': room_data, 'message': f'{nickname} has entered the room!'} , to=active_room.room_name)
            else:
                emit('joinGameSelf', {'status': 'nick-taken', 'message': 'Nickname already taken'})
        else:
            emit('joinGameSelf', {'status': 'room-taken', 'message': 'Room already taken'})
    else:
        room = Room(requested_room_name)
        join_room(room.room_name)
        room.add_user(nickname)
        active_rooms[room.room_name] = room
        room_data = room.to_dict()
        emit('joinGameSelf', {'status': 'success', 'nickname': nickname }, to=sid)
        emit('joinGame', {'status': 'success','room': room_data, 'message': f'{nickname} has entered the room!'} , to=room.room_name)


@socketio.on('chooseSquare')
def on_choose_square(data):
    user = data['user']
    room_name = data['roomName']
    index = data['index']

    room = active_rooms[room_name]
    end_result = room.update_board(index, user)
    room_data = room.to_dict()
    return_data = {'status': 'success','room': room_data}
    if (end_result):
        return_data['end'] = end_result
    emit('updateGame', return_data , to=room.room_name)


@socketio.on('message')
def on_message(data):
    nickname = data['nickname']
    room_name = data['room']
    message = data['message']

    new_message = { 'nickname': nickname, 'message': message }

    room = active_rooms[room_name]

    room.add_message(new_message)
    emit('message', {'status': 'success', 'message': new_message}, to=room.room_name)


if __name__ == '__main__':
    socketio.run(app)
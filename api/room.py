from helpers import validate_tic_tac_toe

class Room:
    def __init__(self, room_name, users = None, messages = None, turn = None, games = 0, board = ['' for i in range(9)]):
        self.room_name = room_name
        self.users = users or {}
        self.messages = messages or []
        self.turn = turn
        self.games = games
        self.board = board


    def __str__(self):
        return self.room_name


    def to_dict(self):
        return self.__dict__


    def is_room_available(self):
        return len(self.users.keys()) < 2


    def is_nickname_available(self, nickname):
        return not bool(self.users.get(nickname))


    def is_first_user(self):
        return len(self.users.keys()) == 0


    def add_user(self, nickname):
        symbol = 'O'
        if self.is_first_user():
            symbol = 'X'
            self.turn = nickname
        self.users[nickname] = { 'symbol': symbol, 'games_won': 0 }


    def update_board(self, index, user):
        self.board[index] = user['symbol']
        result = validate_tic_tac_toe(self.board)
        players = list(self.users.keys())
        x_player = players[0]
        o_player = players[1]

        self.turn = x_player if user['name'] != x_player else o_player
        if result == 'X':
            self.users[x_player]['games_won'] += 1
            self.games += 1
            self.board = ['' for i in range(9)]
            return f'{x_player} wins!'
        elif result == 'O':
            self.users[o_player]['games_won'] += 1
            self.games += 1
            self.board = ['' for i in range(9)]
            return f'{o_player} wins!'
        elif result == 'stalemate':
            self.games += 1
            self.board = ['' for i in range(9)]
            return 'Stalemate!'
        return None



    def add_message(self, message):
        self.messages.append(message)

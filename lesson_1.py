class Phone:
    number = '111111111'
    __count = 0

    def set_phone_number(self, number):
        self.number = number

    def get_number_of_call(self):
        return self.__count

    def call(self):
        self.__count += 1


def amount_of_calls(phones: list) -> int:
    total_count = 0
    for phone in phones:
        total_count += phone.get_number_of_call()
    return total_count


phone_1 = Phone()
phone_2 = Phone()
phone_3 = Phone()

phone_1.number = '22222222'
phone_2.number = '33333333'
phone_3.number = '44444444'

phone_1.call()
phone_1.call()
phone_1.call()
phone_2.call()
phone_2.call()
phone_2.call()
phone_3.call()
phone_3.call()
phone_3.call()

phones = [phone_1, phone_2, phone_3]
t_count = amount_of_calls(phones)
print("Amount of calls:", t_count)


2.

class ChessPiece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
    
    def __repr__(self):
        return f'{self.color} {self.__class__.__name__} at {self.position}'
    
    def change_color(self):
        self.color = 'black' if self.color == 'white' else 'white'
    
    def change_position(self, x, y):
        if 0 <= x <= 7 and 0 <= y <= 7:
            self.position = (x, y)
        else:
            raise ValueError('Invalid position')

    def move_possible(self, x, y):
        raise NotImplementedError('move_possible method must be implemented in subclasses')


class Pawn(ChessPiece):
    def move_possible(self, x, y):
        if self.color == 'white':
            return x == self.position[0] and y == self.position[1] + 1
        else:
            return x == self.position[0] and y == self.position[1] - 1


class Knight(ChessPiece):
    def move_possible(self, x, y):
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


class Bishop(ChessPiece):
    def move_possible(self, x, y):
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return dx == dy


class Rook(ChessPiece):
    def move_possible(self, x, y):
        return x == self.position[0] or y == self.position[1]


class Queen(ChessPiece):
    def move_possible(self, x, y):
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return (dx == dy) or (x == self.position[0] or y == self.position[1])


class King(ChessPiece):
    def move_possible(self, x, y):
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return dx <= 1 and dy <= 1


def get_reachable_pieces(pieces, new_position):
    reachable_pieces = []
    for piece in pieces:
        if piece.move_possible(*new_position):
            reachable_pieces.append(piece)
    return reachable_pieces
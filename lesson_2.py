1.

class Phone:
    def __init__(self, number):
        self.number = number
        self._incoming_calls = 0

    def set_number(self, number):
        self.number = number

    def get_incoming_calls(self):
        return self._incoming_calls

    def receive_call(self):
        self._incoming_calls += 1


# Створення трьох об'єктів телефону
phone1 = Phone("123456789")
phone2 = Phone("987654321")
phone3 = Phone("555555555")

# Зміна номера для всіх телефонів
phone1.set_number("111111111")
phone2.set_number("222222222")
phone3.set_number("333333333")

# Прийом декількох дзвінків на кожному телефоні
phone1.receive_call()
phone1.receive_call()
phone2.receive_call()
phone2.receive_call()
phone2.receive_call()
phone3.receive_call()


# Функція для обчислення загальної кількості прийнятих дзвінків
def total_incoming_calls(phones):
    total_calls = 0
    for phone in phones:
        total_calls += phone.get_incoming_calls()
    return total_calls


# Створення списку з об'єктів телефонів
phones = [phone1, phone2, phone3]

# Виведення загальної кількості прийнятих дзвінків з усіх телефонів
print("Total incoming calls:", total_incoming_calls(phones))


2.
from typing import List, Tuple


class ChessPiece:
    def __init__(self, color: str, position: Tuple[int, int]):
        self.color = color
        self.position = position
    
    def change_color(self):
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'
    
    def change_position(self, x: int, y: int):
        if 0 <= x <= 7 and 0 <= y <= 7:
            self.position = (x, y)
        else:
            print("Invalid position. The position should be within the board.")
    
    def potential_move(self, x: int, y: int) -> bool:
        raise NotImplementedError("Subclasses must implement the potential_move method.")


class Pawn(ChessPiece):
    def potential_move(self, x: int, y: int) -> bool:
        # Pawns can move forward by one step in their own color direction
        if self.color == 'white' and self.position[1] + 1 == y:
            return True
        elif self.color == 'black' and self.position[1] - 1 == y:
            return True
        else:
            return False


class Knight(ChessPiece):
    def potential_move(self, x: int, y: int) -> bool:
        # Knights can move in an L-shape: 2 steps in one direction and 1 step in a perpendicular direction
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            return True
        else:
            return False


class Bishop(ChessPiece):
    def potential_move(self, x: int, y: int) -> bool:
        # Bishops can move diagonally
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        if dx == dy:
            return True
        else:
            return False


class Rook(ChessPiece):
    def potential_move(self, x: int, y: int) -> bool:
        # Rooks can move horizontally or vertically
        if x == self.position[0] or y == self.position[1]:
            return True
        else:
            return False


class Queen(ChessPiece):
    def potential_move(self, x: int, y: int) -> bool:
        # Queens can move horizontally, vertically, or diagonally
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        if x == self.position[0] or y == self.position[1] or dx == dy:
            return True
        else:
            return False


class King(ChessPiece):
    def potential_move(self, x: int, y: int) -> bool:
        # Kings can move one step in any direction
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        if dx <= 1 and dy <= 1:
            return True
        else:
            return False


def get_possible_moves(chess_pieces: List[ChessPiece], x: int, y: int) -> List[ChessPiece]:
    possible_moves = []
    for piece in chess_pieces:
        if piece.potential_move(x, y):
            possible_moves.append(piece)
    return possible_moves
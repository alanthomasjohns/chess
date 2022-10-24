import os




class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color

        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign #AI identifies black and white pieces
        self.moves = []
        self.moved = False

        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect


    def set_texture(self, size=80): #path to the image of piece(image url)
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png') #the path is specified the same way it is in assets folder


    def add_moves(self, move):
        self.moves.append(move)

#building the pieces

class Pawn(Piece): #inherits Piece()
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1 #as y-axis is downwards in pygame. dir given as pawn moves in one direction.
        super().__init__('pawn', color, 1.0) #the value is super important as the AI unserstands the piece with this value.


class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0) #the values being passed are legit values


class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.001)

class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)


class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)


class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, 10000.0)

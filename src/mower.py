class Turn:
    LEFT = 'L'
    RIGHT = 'R'


class Coordinates:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def __repr__(self):
        return f'{self.__x} {self.__y}'

class CardinalPoint:

    def if_turning(self, side):
        raise NotImplementedError()

    def if_moving_forward_from(self, coordinates: Coordinates) -> Coordinates:
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def __eq__(self, other):
        return str(self) == str(other)

    @staticmethod
    def create(cardinal_point: str):
        cardinal_points = {
            'N': North(),
            'S': South(),
            'E': East(),
            'W': West()
        }

        return cardinal_points[cardinal_point]


class North(CardinalPoint):
    def if_moving_forward_from(self, coordinates: Coordinates) -> Coordinates:
        return Coordinates(coordinates.x, coordinates.y + 1)

    def if_turning(self, side: str):
        if side == Turn.LEFT:
            return West()

        return East()


    def __repr__(self):
        return 'N'


class West(CardinalPoint):
    def if_moving_forward_from(self, coordinates: Coordinates) -> Coordinates:
        return Coordinates(coordinates.x - 1, coordinates.y)

    def if_turning(self, side):
        if side == Turn.LEFT:
            return South()

        return North()

    def __repr__(self):
        return 'W'


class South(CardinalPoint):
    def if_moving_forward_from(self, coordinates: Coordinates) -> Coordinates:
        return Coordinates(coordinates.x, coordinates.y - 1)

    def if_turning(self, side):
        if side == Turn.LEFT:
            return East()

        return West()

    def __repr__(self):
        return 'S'


class East(CardinalPoint):
    def if_moving_forward_from(self, coordinates: Coordinates) -> Coordinates:
        return Coordinates(coordinates.x + 1, coordinates.y)

    def if_turning(self, side):
        if side == Turn.LEFT:
            return North()

        return South()

    def __repr__(self):
        return 'E'


class Navigator:
    def __init__(self, initial_cardinal_point: str):
        self.__cardinal_point = CardinalPoint.create(initial_cardinal_point)

    def where_is_it_currently_facing(self):
        return str(self.__cardinal_point)

    def move_forward_from(self, position: Coordinates) -> Coordinates:
        return self.__cardinal_point.if_moving_forward_from(position)

    def turn(self, side: str) -> 'Navigator':
        self.__cardinal_point = self.__cardinal_point.if_turning(side)

        return self


class Mower:

    MOVE_FORWARD = 'M'

    def __init__(self, initial_position: Coordinates, navigator: Navigator):
        self.__navigator = navigator
        self.__position = initial_position

    @classmethod
    def deploy(cls, coordinate_x: int, coordinate_y: int, facing: str):
        return cls(Coordinates(coordinate_x, coordinate_y), Navigator(facing))

    def execute(self, commands: str) -> 'Mower':
        for command in commands:
            if command == self.MOVE_FORWARD:
                new_position = self.__navigator.move_forward_from(self.__position)
                self.__position = new_position
            else:
                self.__navigator.turn(command)

        return self

    def report(self) -> str:
        return f'{self.__position} {self.__navigator.where_is_it_currently_facing()}'

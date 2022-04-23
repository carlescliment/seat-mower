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

    def if_turning_left(self):
        raise NotImplementedError()

    def if_turning_right(self):
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

    def if_turning_left(self) -> CardinalPoint:
        return West()

    def if_turning_right(self) -> CardinalPoint:
        return East()

    def __repr__(self):
        return 'N'


class West(CardinalPoint):
    def if_moving_forward_from(self, coordinates: Coordinates) -> Coordinates:
        return Coordinates(coordinates.x - 1, coordinates.y)

    def if_turning_left(self) -> CardinalPoint:
        return South()

    def if_turning_right(self) -> CardinalPoint:
        return North()

    def __repr__(self):
        return 'W'


class South(CardinalPoint):
    def if_moving_forward_from(self, coordinates: Coordinates) -> Coordinates:
        return Coordinates(coordinates.x, coordinates.y - 1)

    def if_turning_left(self) -> CardinalPoint:
        return East()

    def if_turning_right(self) -> CardinalPoint:
        return West()

    def __repr__(self):
        return 'S'


class East(CardinalPoint):
    def if_moving_forward_from(self, coordinates: Coordinates) -> Coordinates:
        return Coordinates(coordinates.x + 1, coordinates.y)

    def if_turning_left(self) -> CardinalPoint:
        return North()

    def if_turning_right(self) -> CardinalPoint:
        return South()

    def __repr__(self):
        return 'E'


class Navigator:
    LEFT = 'L'

    def __init__(self, initial_position: Coordinates, initially_facing: str):
        self.__facing = CardinalPoint.create(initially_facing)
        self.__position = initial_position

    def move_forward(self) -> 'Navigator':
        self.__position = self.__facing.if_moving_forward_from(self.__position)

        return self

    def turn(self, side: str) -> 'Navigator':
        if side == self.LEFT:
            self.__facing = self.__facing.if_turning_left()
        else:
            self.__facing = self.__facing.if_turning_right()

        return self

    def __repr__(self):
        return f'{self.__position} {self.__facing}'


class Mower:

    MOVE_FORWARD = 'M'

    def __init__(self, navigator: Navigator):
        self.__navigator = navigator

    @classmethod
    def deploy(cls, coordinate_x: int, coordinate_y: int, facing: str):
        return cls(Navigator(Coordinates(coordinate_x, coordinate_y), facing))

    def execute(self, commands: list) -> 'Mower':
        for command in commands:
            if command == self.MOVE_FORWARD:
                self.__navigator.move_forward()
            else:
                self.__navigator.turn(command)

        return self

    def report(self) -> str:
        return str(self.__navigator)

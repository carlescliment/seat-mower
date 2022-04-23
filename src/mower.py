class CannotGoOutOfThePlateauError(Exception):
    pass

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
    def __init__(self, initial_position: Coordinates, initially_facing: str, plateau_limits: Coordinates):
        self.__facing = CardinalPoint.create(initially_facing)
        self.__position = initial_position
        self.__plateau_limits = plateau_limits

    def move_forward(self) -> 'Navigator':
        new_position = self.__facing.if_moving_forward_from(self.__position)
        if (
            new_position.y > self.__plateau_limits.y
            or new_position.x > self.__plateau_limits.x
            or new_position.y < 0
            or new_position.x < 0
        ):
            raise CannotGoOutOfThePlateauError()

        self.__position = new_position

        return self

    def turn_left(self) -> 'Navigator':
        self.__facing = self.__facing.if_turning_left()

        return self

    def turn_right(self) -> 'Navigator':
        self.__facing = self.__facing.if_turning_right()

        return self

    def __repr__(self):
        return f'{self.__position} {self.__facing}'


class Mower:

    MOVE_FORWARD = 'M'
    TURN_LEFT = 'L'
    TURN_RIGHT = 'R'

    def __init__(self, navigator: Navigator):
        self.__navigator = navigator

    @classmethod
    def deploy(cls, coordinate_x: int, coordinate_y: int, facing: str, plateau_max_x: int = 5, plateau_max_y: int = 5):
        return cls(Navigator(
            Coordinates(coordinate_x, coordinate_y),
            facing,
            Coordinates(plateau_max_x, plateau_max_y)
        ))

    def execute(self, commands: list) -> 'Mower':
        procedures = {
            self.MOVE_FORWARD: lambda: self.__navigator.move_forward(),
            self.TURN_LEFT: lambda: self.__navigator.turn_left(),
            self.TURN_RIGHT: lambda: self.__navigator.turn_right(),
        }
        for command in commands:
            procedures[command]()

        return self

    def report(self) -> str:
        return str(self.__navigator)

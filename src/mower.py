class Turn:
    LEFT = 'L'
    RIGHT = 'R'


class CardinalPoint:

    def if_turning(self, side):
        raise NotImplementedError()

    def if_moving_forward_from(self, coordinate_x: int, coordinate_y: int) -> tuple:
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
    def if_moving_forward_from(self, coordinate_x: int, coordinate_y: int) -> tuple:
        return coordinate_x, coordinate_y + 1

    def if_turning(self, side: str):
        if side == Turn.LEFT:
            return West()

        return East()


    def __repr__(self):
        return 'N'


class West(CardinalPoint):
    def if_moving_forward_from(self, coordinate_x: int, coordinate_y: int) -> tuple:
        return coordinate_x - 1, coordinate_y

    def if_turning(self, side):
        if side == Turn.LEFT:
            return South()

        return North()

    def __repr__(self):
        return 'W'


class South(CardinalPoint):
    def if_moving_forward_from(self, coordinate_x: int, coordinate_y: int) -> tuple:
        return coordinate_x, coordinate_y - 1

    def if_turning(self, side):
        if side == Turn.LEFT:
            return East()

        return West()

    def __repr__(self):
        return 'S'


class East(CardinalPoint):
    def if_moving_forward_from(self, coordinate_x: int, coordinate_y: int) -> tuple:
        return coordinate_x + 1, coordinate_y

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

    def move_forward_from(self, coordinate_x, coordinate_y):
        return self.__cardinal_point.if_moving_forward_from(coordinate_x, coordinate_y)

    def turn(self, side: str) -> 'Navigator':
        self.__cardinal_point = self.__cardinal_point.if_turning(side)

        return self


class Mower:

    MOVE_FORWARD = 'M'

    def __init__(self, coordinate_x: int, coordinate_y: int, navigator: Navigator):
        self.__navigator = navigator
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y

    @classmethod
    def deploy(cls, coordinate_x: int, coordinate_y: int, facing: str):
        return cls(coordinate_x, coordinate_y, Navigator(facing))

    def execute(self, commands: str) -> 'Mower':
        if commands == self.MOVE_FORWARD:
            new_position = self.__navigator.move_forward_from(self.__coordinate_x, self.__coordinate_y)
            self.__coordinate_x, self.__coordinate_y = new_position
        else:
            self.__navigator.turn(commands)


        return self

    def report(self) -> str:
        return f'{self.__coordinate_x} {self.__coordinate_y} {self.__navigator.where_is_it_currently_facing()}'

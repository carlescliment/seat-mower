class Compass:
    NORTH = 'N'
    WEST = 'W'
    SOUTH = 'S'
    EAST = 'E'

    LEFT = 'L'
    RIGHT = 'R'

    def __init__(self, facing: str):
        self.__facing = facing

    def turn(self, side: str) -> str:
        facings_when_turning = {
            self.NORTH: {
                self.LEFT: self.WEST,
                self.RIGHT: self.EAST,
            },
            self.WEST: {
                self.LEFT: self.SOUTH,
                self.RIGHT: self.NORTH,
            },
            self.SOUTH: {
                self.LEFT: self.EAST,
                self.RIGHT: self.WEST,
            },
            self.EAST: {
                self.LEFT: self.NORTH,
                self.RIGHT: self.SOUTH,
            },
        }

        return facings_when_turning[self.__facing][side]


class Mower:

    def __init__(self, coordinate_x: int, coordinate_y: int, facing: str):
        self.__facing = facing
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y

    @classmethod
    def deploy(cls, coordinate_x: int, coordinate_y: int, facing: str):
        return cls(coordinate_x, coordinate_y, facing)

    def execute(self, commands: str) -> 'Mower':
        self.__facing = Compass(self.__facing).turn(commands)

        return self

    def report(self) -> str:
        return f'{self.__coordinate_x} {self.__coordinate_y} {self.__facing}'

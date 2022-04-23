class Compass:
    NORTH = 'N'
    WEST = 'W'
    SOUTH = 'S'
    EAST = 'E'

    LEFT = 'L'
    RIGHT = 'R'

    def __init__(self, cardinal_point: str):
        self.__cardinal_point = cardinal_point

    def where_is_it_pointing_to(self):
        return self.__cardinal_point

    def turn(self, side: str) -> 'Compass':
        cardinal_point_when_turning = {
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

        self.__cardinal_point = cardinal_point_when_turning[self.__cardinal_point][side]

        return self


class Mower:

    def __init__(self, coordinate_x: int, coordinate_y: int, compass: Compass):
        self.__compass = compass
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y

    @classmethod
    def deploy(cls, coordinate_x: int, coordinate_y: int, facing: str):
        return cls(coordinate_x, coordinate_y, Compass(facing))

    def execute(self, commands: str) -> 'Mower':
        self.__compass.turn(commands)

        return self

    def report(self) -> str:
        return f'{self.__coordinate_x} {self.__coordinate_y} {self.__compass.where_is_it_pointing_to()}'

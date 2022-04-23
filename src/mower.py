class Mower:
    NORTH = 'N'
    WEST = 'W'
    SOUTH = 'S'
    EAST = 'E'

    LEFT = 'L'
    RIGHT = 'R'

    def __init__(self, coordinate_x: int, coordinate_y: int, facing: str):
        self.__facing = facing
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y

    @classmethod
    def deploy(cls, coordinate_x: int, coordinate_y: int, facing: str):
        return cls(coordinate_x, coordinate_y, facing)

    def execute(self, commands: str) -> 'Mower':
        facings_when_spinning = {
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
        self.__facing = facings_when_spinning[self.__facing][commands]

        return self

    def report(self) -> str:
        return f'{self.__coordinate_x} {self.__coordinate_y} {self.__facing}'

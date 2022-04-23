class Mower:
    def __init__(self, coordinate_x: int, coordinate_y: int, facing: str):
        self.__facing = facing
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y

    @classmethod
    def deploy(cls, coordinate_x: int, coordinate_y: int, facing: str):
        return cls(coordinate_x, coordinate_y, facing)

    def execute(self, commands: str) -> 'Mower':
        facings_when_spinning = {
            'N': {
                'L': 'W',
                'R': 'E',
            },
            'W': {
                'L': 'S',
                'R': 'N',
            }
        }
        self.__facing = facings_when_spinning[self.__facing][commands]

        return self

    def report(self) -> str:
        return f'{self.__coordinate_x} {self.__coordinate_y} {self.__facing}'

class Mower:
    def __init__(self, coordinate_x: int, coordinate_y: int, facing: str):
        self.__facing = facing
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y

    @classmethod
    def deploy(cls, coordinate_x: int, coordinate_y: int, facing: str):
        return cls(coordinate_x, coordinate_y, facing)

    def report(self) -> str:
        return f'{self.__coordinate_x} {self.__coordinate_y} {self.__facing}'

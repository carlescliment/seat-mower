class Mower:
    def __init__(self, coordinate_x, facing):
        self._facing = facing
        self._coordinate_x = coordinate_x

    @classmethod
    def deploy(cls, coordinate_x, facing: str):
        return cls(coordinate_x, facing)

    def report(self) -> str:
        return f'{self._coordinate_x} {self._facing}'

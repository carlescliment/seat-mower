class Mower:
    def __init__(self, facing):
        self._facing = facing

    @classmethod
    def deploy(cls, facing: str):
        return cls(facing)

    def report(self) -> str:
        return self._facing

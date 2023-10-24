from PoligonalModel import PoligonalModel
from Flash import Flash


class Scene:
    def __init__(self, id: int, models: PoligonalModel, flashes: Flash) -> None:
        self.id = id
        self.models = models
        self.flashes = flashes

    def method_1(self, data: None) -> None:
        pass

    def method_2(self, data1: None, data2: None) -> None:
        pass
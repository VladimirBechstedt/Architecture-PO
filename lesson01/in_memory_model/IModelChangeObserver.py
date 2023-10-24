from abc import ABC, abstractmethod


class IModelChangeObserver(ABC):
    @abstractmethod
    def aplly_update_model(self) -> None:
        pass
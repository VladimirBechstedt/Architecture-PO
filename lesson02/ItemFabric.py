from abc import ABCMeta, abstractmethod

class ItemFabric:
    __metaclass__ = ABCMeta

    def open_rewgard(self):
        gameItem = self.create_item()

        gameItem.open()

    @abstractmethod
    def create_item(self):
        '''metod'''

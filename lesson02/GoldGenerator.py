from ItemFabric import ItemFabric
from GoldReward import GoldReward
from abc import ABC, abstractmethod


class GoldGenerator(ABC, ItemFabric):

    def create_item(self):
        print("Создал новый сундук")
        return GoldReward()

# from abc import ABC, abstractmethod
#
#
# class IGameItem(ABC):
#
#     @abstractmethod
#     def fabric_open(self):
#         pass
import zope.interface


class IGameItem(zope.interface.Interface):

    def fabric_open():
        '''pass'''

import zope.interface
from iGameItem import IGameItem


#@zope.interface.implements(IGameItem)
class GoldReward(object):
    zope.interface.implementer(IGameItem)

    def fabric_open(self):
        print('gold')
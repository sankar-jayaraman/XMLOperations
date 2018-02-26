from abc import ABCMeta, abstractmethod

class XMLFormChecker(object):
    __metaclass__ = ABCMeta

    @abstractmethod 
    def IsValidOperationXML(self,root):
        raise NotImplementedError('Check must be defined by users to  use this base class')




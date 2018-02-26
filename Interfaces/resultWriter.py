from abc import ABCMeta, abstractmethod

class ResultWriter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Write(self, resultDict):
        raise NotImplementedError('Write must be defined by users to use this basse class')



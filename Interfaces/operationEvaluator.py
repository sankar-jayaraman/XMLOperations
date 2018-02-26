from abc import ABCMeta, abstractmethod


class OperationEvaluator(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def Addition(self, items):
        raise NotImplementedError('Addition must be defined by users to use this base class')
    @abstractmethod
    def Division(self, child):
        raise NotImplementedError('Division must be defined by users to use this base class')
    @abstractmethod
    def Subtraction(self, child):
        raise NotImplementedError('Subtraction must be defined by users to use this base class')
    @abstractmethod
    def Multiplication(self, items):
        raise NotImplementedError('Multiplication must be defined by users to use this base class')

    
    def Evaluate(self, child):
        return self.OperationSelector(child.tag, child)

    def OperationSelector(self, tag, child):
        if tag == 'addition':
             return self.Addition(list(child.findall("item")))
        elif tag == 'subtraction': 
             return self.Subtraction(child)
        elif tag == 'division': 
             return self.Division(child)
        elif tag == 'multiplication':
             return self.Multiplication(list(child.findall("factor")))   



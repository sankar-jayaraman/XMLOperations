from simpleOperationEvaluator import SimpleOperationEvaluator
from complexOperationEvaluator import ComplexOperationEvaluator

class OperationTypeSelector(object):
    """description of class"""
    def Select(self, child):
        if 'complex' in child.attrib and child.get('complex') == 'true':
            return ComplexOperationEvaluator()
        else:
            return SimpleOperationEvaluator()
            




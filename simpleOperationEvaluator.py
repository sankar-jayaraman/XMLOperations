import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'Interfaces'))
from operationEvaluator import OperationEvaluator

class SimpleOperationEvaluator(OperationEvaluator):
    
    def Addition(self, items):
        nums = []
        for item in items:
            nums.append(int(item.text))
        return sum(nums)

    def Division(self, child):
        dividend = int(child.find('dividend').text)
        divisor = int(child.find('divisor').text)
        return dividend / divisor

    
    def Subtraction(self, child):
        minuend = int(child.find('minuend').text)
        subtrahend = int(child.find('subtrahend').text)
        return minuend - subtrahend

    def Multiplication(self, items):
        result =1
        for item in items:
            result = result * int(item.text)
        return result
    
    
    
    
        
    


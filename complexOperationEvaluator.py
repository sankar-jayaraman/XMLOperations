import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'Interfaces'))
from operationEvaluator import OperationEvaluator


class ComplexOperationEvaluator(OperationEvaluator):
        
    def Addition(self, items):
        nums = []
        for item in items:
            if(len(item) == 0):
                nums.append(int(item.text))
            else:
                nums.append(self.OperationSelector(item[0].tag, item[0]))
        return sum(nums)

    def Subtraction(self, child):
        minuendElem = child.find('minuend')
        if len(minuendElem) == 0:
            minuend = int(minuendElem.text)
        else:
            minuend = self.OperationSelector(minuendElem[0].tag, minuendElem[0])
        
        subtrahendElem = child.find('subtrahend')
        
        if len(subtrahendElem) == 0:
            subtrahend = int(subtrahendElem.text)
        else:
            subtrahend = self.OperationSelector(subtrahendElem[0].tag, subtrahendElem[0])
        return minuend - subtrahend

    def Division(self, child):
        dividendElem = child.find('dividend')
        if len(dividendElem) == 0:
            dividend = int(dividendElem.text)
        else:
            dividend = self.OperationSelector(dividendElem[0].tag, dividendElem[0])
        
        divisorElem = child.find('divisor')
        
        if len(divisorElem) == 0:
            divisor = int(divisorElem.text)
        else:
            divisor = self.OperationSelector(divisorElem[0].tag, divisorElem[0])
        return dividend / divisor


    def Multiplication(self, items):
        nums = []
        for item in items:
            if(len(item) == 0):
                nums.append(int(item.text))
            else:
                nums.append(self.OperationSelector(item[0].tag, item[0]))
        result =1
        for num in nums:
            result = result * num
        return result
              

    
    

    


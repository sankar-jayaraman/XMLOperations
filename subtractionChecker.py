import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'Interfaces'))

from xmlFormChecker import XMLFormChecker


class SubtractionChecker(XMLFormChecker):
    def IsValidOperationXML(self,child):
        
        if len(child) == 2 and child[0].tag == 'minuend' and child[1].tag == 'subtrahend':
            return True
        else:
            raise SyntaxError('XML must contain exactly one minuend and subtrahend')




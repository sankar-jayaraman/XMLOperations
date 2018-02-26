import unittest
import xml.etree.ElementTree  as ET
from operationCheckSelector import OperationCheckSelector
from additionChecker import AdditionChecker
from subtractionChecker import SubtractionChecker
from divisionChecker import DivisionChecker
from multiplicationChecker import MultiplicationChecker

class OperationCheckSelectorTest(unittest.TestCase):
    
    def test_WhenAdditionTagIsPresentAdditionCheckerIsReturned(self):
        input = """<expressions> 
                    <addition id="1" complex="true"> 
                        <item>2</item>
                        <item>3</item>
                        <item>4</item> 
                    </addition>
               </expressions>"""
        root = ET.fromstring(input)
        self.assertIsInstance(OperationCheckSelector().Select(root[0]), AdditionChecker)

    def test_WhenSubtractionTagIsPresentSubtractionCheckerIsReturned(self):
        input = """<expressions> 
                    <subtraction id="1" complex="true"> 
                        <item>2</item>
                        <item>3</item>
                        <item>4</item> 
                    </subtraction>
               </expressions>"""
        root = ET.fromstring(input)
        self.assertIsInstance(OperationCheckSelector().Select(root[0]), SubtractionChecker)

    def test_WhenMultiplicationTagIsPresentMultiplicationCheckerIsReturned(self):
        input = """<expressions> 
                    <multiplication id="1" complex="true"> 
                        <item>2</item>
                        <item>3</item>
                        <item>4</item> 
                    </multiplication>
               </expressions>"""
        root = ET.fromstring(input)
        self.assertIsInstance(OperationCheckSelector().Select(root[0]), MultiplicationChecker)

    def test_WhenDivisionTagIsPresentDivisionCheckerIsReturned(self):
        input = """<expressions> 
                    <division id="1" complex="true"> 
                        <item>2</item>
                        <item>3</item>
                        <item>4</item> 
                    </division>
               </expressions>"""
        root = ET.fromstring(input)
        self.assertIsInstance(OperationCheckSelector().Select(root[0]), DivisionChecker)

    
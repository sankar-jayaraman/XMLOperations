import unittest
from subtractionChecker import SubtractionChecker
import xml.etree.ElementTree  as ET


class Test_SubtractionCheckerTest(unittest.TestCase):
    def test_WhenNoMatchingMinuendAndSubtrahendFound_RaisesError(self):
        input = """<expressions> 
                    <subtraction id="4">
                       <minuend>0</minuend>
                    </subtraction>
               </expressions>
               """

        root = ET.fromstring(input)
        checker = SubtractionChecker()
        with self.assertRaises(SyntaxError):
            checker.IsValidOperationXML(root[0]) 

    def test_WhenMatchingMinuendAndSubtrahendFound_ReturnsTrue(self):
        input = """<expressions> 
                    <subtraction id="4">
                       <minuend>0</minuend>
                       <subtrahend>1</subtrahend>
                    </subtraction>
               </expressions>
               """

        root = ET.fromstring(input)
        checker = SubtractionChecker()
        self.assertTrue(checker.IsValidOperationXML(root[0]))
    
import unittest
from divisionChecker import DivisionChecker
import xml.etree.ElementTree  as ET


class Test_DivisionCheckerTest(unittest.TestCase):
    def test_WhenNoMatchingDividendAndDivisorFound_RaisesError(self):
        input = """<expressions> 
                    <division id="4">
                       <divisor>0</divisor>
                    </division>
               </expressions>
               """

        root = ET.fromstring(input)
        checker = DivisionChecker()
        with self.assertRaises(SyntaxError):
            checker.IsValidOperationXML(root[0]) 

    
    def test_WhenNoMatchingDividendAndDivisorFoundInComplexExpression_RaisesError(self):
        input = """<expressions > 
                        <division id="14" complex="true">
                            <dividend>54</dividend>
                            
                                <addition>
                                    <item>3</item>
                                    <item>6</item>
                                </addition>
                            
                         </division>

               </expressions>
               """

        root = ET.fromstring(input)
        checker = DivisionChecker()
        with self.assertRaises(SyntaxError):
            checker.IsValidOperationXML(root[0]) 

    def test_WhenDividendAndDivisorIsPresent_ReturnsTrue(self):
        input = """<expressions> 
                    <division id="4">
                       <dividend>54</dividend> 
                       <divisor>9</divisor>
                    </division>
               </expressions>
               """

        root = ET.fromstring(input)
        checker = DivisionChecker()
        self.assertTrue(checker.IsValidOperationXML(root[0]))
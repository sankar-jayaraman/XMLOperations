import unittest
import xml.etree.ElementTree  as ET
from complexOperationEvaluator import ComplexOperationEvaluator
from simpleOperationEvaluator import SimpleOperationEvaluator
from operationTypeSelector import OperationTypeSelector

class OperationTypeSelectorTest(unittest.TestCase):
    
    def test_WhenComplexTagIsPresentAndTrue_ComplexOperationEvaluatorIsReturned(self):
        input = """<expressions> 
                    <addition id="1" complex="true"> 
                        <item>2</item>
                        <item>3</item>
                        <item>4</item> 
                    </addition>
               </expressions>"""
        root = ET.fromstring(input)
        self.assertIsInstance(OperationTypeSelector().Select(root[0]),ComplexOperationEvaluator)

    def test_WhenComplexTagIsNotPresent_SimpleOperationEvaluatorIsReturned(self):
        input = """<expressions> 
                    <addition id="1"> 
                        <item>2</item>
                        <item>3</item>
                        <item>4</item> 
                    </addition>
               </expressions>"""
        root = ET.fromstring(input)
        self.assertIsInstance(OperationTypeSelector().Select(root[0]),SimpleOperationEvaluator)

    def test_WhenComplexTagIsPresentAndFalse_SimpleOperationEvaluatorIsReturned(self):
        input = """<expressions> 
                    <addition id="1" complex="false"> 
                        <item>2</item>
                        <item>3</item>
                        <item>4</item> 
                    </addition>
               </expressions>"""
        root = ET.fromstring(input)
        self.assertIsInstance(OperationTypeSelector().Select(root[0]),SimpleOperationEvaluator)

import unittest
import xml.etree.ElementTree  as ET
from simpleOperationEvaluator import SimpleOperationEvaluator
import collections

all_operations =  """<expressions>
                <addition id="1">
                <item>2</item>
                <item>3</item>
                <item>4</item>
                </addition>
                <subtraction id="2">
                <minuend>3</minuend>
                <subtrahend>2</subtrahend>
                </subtraction>
                <multiplication id="3">
                <factor>5</factor>
                <factor>6</factor>
                <factor>8</factor>
                </multiplication>
                <division id="4">
                <dividend>54</dividend>
                <divisor>9</divisor>
                </division>
                </expressions>
                """

class SimpleOperationevaluatorTest(unittest.TestCase):
    def test_WhenTagIsAddition_AdditionOperationIsEvaluated(self):
        
        input = """<expressions> 
                    <addition id="1"> 
                        <item>2</item>
                        <item>3</item>
                        <item>4</item> 
                    </addition>
               </expressions>"""

        root = ET.fromstring(input)
        expected = collections.OrderedDict()
        expected['1'] = 9
        evaluator = SimpleOperationEvaluator()
        results  = collections.OrderedDict()
        results[root[0].attrib['id']] = evaluator.Evaluate(root[0])
        self.assertEqual(expected,results)

        

    def test_WhenTagIsSubtraction_SubtractionOperationIsEvaluated(self):
        
        input = """<expressions> 
                    <subtraction id="2">
                        <minuend>3</minuend>
                        <subtrahend>2</subtrahend>
                    </subtraction>
               </expressions>"""

        root = ET.fromstring(input)
        expected = collections.OrderedDict()
        expected['2'] = 1
        evaluator = SimpleOperationEvaluator()
        results  = collections.OrderedDict()
        results[root[0].attrib['id']] = evaluator.Evaluate(root[0])
        self.assertEqual(expected,results)


    def test_WhenTagIsDivision_DivisionOperationIsEvaluated(self):
        
        input = """<expressions> 
                    <division id="4">
                        <dividend>54</dividend>
                        <divisor>9</divisor>
                    </division>
               </expressions>"""

        root = ET.fromstring(input)
        expected = collections.OrderedDict()
        expected['4'] = 6
        evaluator = SimpleOperationEvaluator()
        results  = collections.OrderedDict()
        results[root[0].attrib['id']] = evaluator.Evaluate(root[0])
        self.assertEqual(expected,results)


    def test_WhenTagIsMultiplication_MultiplicationOperationIsEvaluated(self):
        
        input = """<expressions> 
                    <multiplication id="3">
                           <factor>5</factor>
                           <factor>6</factor>
                           <factor>8</factor>
                    </multiplication>
                   </expressions>"""

        root = ET.fromstring(input)
        expected = collections.OrderedDict()
        expected['3'] = 240
        evaluator = SimpleOperationEvaluator()
        results  = collections.OrderedDict()
        results[root[0].attrib['id']] = evaluator.Evaluate(root[0])
        self.assertEqual(expected,results)

    
    def test_When_MultipleOperationsAreInput_AllOperationsAreEvaluated(self):
         
        input = all_operations 
        root = ET.fromstring(input)
        expected = collections.OrderedDict()
        expected['1'] = 9
        expected['2'] = 1
        expected['3'] = 240
        expected['4'] = 6
        
        results = collections.OrderedDict()
        evaluator = SimpleOperationEvaluator()
        for child in root:
            results[child.attrib['id']] = evaluator.Evaluate(child)

        self.assertEqual(expected, results)
      
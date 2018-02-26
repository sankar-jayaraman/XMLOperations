import xml.etree.ElementTree  as ET
import unittest
from complexOperationEvaluator import ComplexOperationEvaluator
import collections

all_operations = """<expressions> 
                        <addition id="10" complex="true">
                            <item>2</item>
                            <item>3</item>
                            <item>
                                <subtraction>
                                    <minuend>7</minuend>
                                    <subtrahend>3</subtrahend>
                                </subtraction>
                            </item>
                        </addition>
                        <subtraction id="11">
                            <minuend>3</minuend>
                            <subtrahend>2</subtrahend>
                        </subtraction>
                        <multiplication id="12">
                            <factor>5</factor>
                            <factor>6</factor>
                            <factor>8</factor>
                        </multiplication>
                        <multiplication id="13" complex="true">
                            <factor>
                                <addition>
                                    <item>2</item>
                                    <item>3</item>
                                    <item>4</item>
                                </addition>
                            </factor>
                            <factor>6</factor>
                            <factor>
                                <multiplication>
                                    <factor>3</factor>
                                    <factor>4</factor>
                                    <factor>5</factor>
                                    <factor>10</factor>
                                    <factor>56</factor>
                                </multiplication>
                            </factor>
                        </multiplication>
                        <division id="14" complex="true">
                            <dividend>54</dividend>
                            <divisor>
                                <addition>
                                    <item>3</item>
                                    <item>6</item>
                                </addition>
                             </divisor>
                         </division>
                    </expressions>
                    
                 """

class ComplexOperationEvaluatorTest(unittest.TestCase):
    def test_WhenSubtractionIsNestedUnderAddition_EvaluatesCorrectly(self):
        input = """ <expressions> 
                        <addition id="10" complex="true">
                            <item>2</item>
                            <item>3</item>
                            <item>
                                <subtraction>
                                    <minuend>7</minuend>
                                    <subtrahend>3</subtrahend>
                                </subtraction>
                            </item>
                        </addition>
                    </expressions> 
                """
        root = ET.fromstring(input)
        expected = collections.OrderedDict()
        expected['10'] = 9
        evaluator = ComplexOperationEvaluator()

        results  = collections.OrderedDict()
        results[root[0].attrib['id']] = evaluator.Evaluate(root[0])
        self.assertEqual(expected,results)



    def test_WhenAdditionIsNestedUnderMultiplication_EvaluatesCorrectly(self):
        input = """ <expressions> 
                        <multiplication id="13" complex="true">
                            <factor>
                                <addition>
                                    <item>2</item>
                                    <item>3</item>
                                    <item>4</item>
                                </addition>
                            </factor>
                            <factor>6</factor>
                            <factor>
                                <multiplication>
                                    <factor>3</factor>
                                    <factor>4</factor>
                                    <factor>5</factor>
                                    <factor>10</factor>
                                    <factor>56</factor>
                                </multiplication>
                            </factor>
                    </multiplication>
               </expressions> 
                """
        root = ET.fromstring(input)
        expected = collections.OrderedDict()
        expected['13'] = 1814400
        evaluator = ComplexOperationEvaluator()
        results  = collections.OrderedDict()
        results[root[0].attrib['id']] = evaluator.Evaluate(root[0])
        self.assertEqual(expected,results)

    def test_WhenAdditionIsNestedUnderSubtraction_EvaluatesCorrectly(self):
        input = """ <expressions> 
                        <subtraction id="13" complex="true">
                            <minuend>
                                <addition>
                                    <item>2</item>
                                    <item>3</item>
                                    <item>4</item>
                                </addition>
                            </minuend>
                            <subtrahend>6</subtrahend>
                       </subtraction>
               </expressions> 
                """
        root = ET.fromstring(input)
        expected = collections.OrderedDict()
        expected['13'] = 3
                
        evaluator = ComplexOperationEvaluator()
        results  = collections.OrderedDict()
        results[root[0].attrib['id']] = evaluator.Evaluate(root[0])
        self.assertEqual(expected,results)

    def test_WhenMultiplcationIsNestedUnderDivision_EvaluatesCorrectly(self):
        input = """ <expressions> 
                        <division id="13" complex="true">
                            <dividend>54</dividend>
                            <divisor>
                                <multiplication>
                                    <factor>3</factor>
                                    <factor>2</factor>
                                </multiplication>
                            </divisor>
                       </division>
               </expressions> 
                """
        root = ET.fromstring(input)
        expected = collections.OrderedDict()
        expected['13'] = 9
        evaluator = ComplexOperationEvaluator()

        results  = collections.OrderedDict()
        results[root[0].attrib['id']] = evaluator.Evaluate(root[0])
        self.assertEqual(expected,results)

        

    def test_When_MultipleComplexOperationsAreInput_AllOperationsAreEvaluated(self):
         
        input = all_operations 
        root = ET.fromstring(input)
        expected = collections.OrderedDict()
        expected['10'] = 9
        expected['11'] = 1
        expected['12'] = 240
        expected['13'] = 1814400
        expected['14'] = 6
        
        evaluator = ComplexOperationEvaluator()
        results = collections.OrderedDict()
        for child in root:
            results[child.attrib['id']] = evaluator.Evaluate(child)

        self.assertEqual(expected, results)
    
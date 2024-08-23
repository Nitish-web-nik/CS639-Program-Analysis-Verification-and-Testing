from kast import kachuaAST
import sys
import random
import struct
import uuid
from z3 import *
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *
sys.path.insert(0, '../KachuaCore/')
coverage_percentage  = []
# Each input is of this type.
class InputObject():
    def __init__(self, data):
        self.id = str(uuid.uuid4())
        self.data = data
#        # Flag to check if ever picked
#        # for mutation or not.
        self.pickedOnce = False
        
class CustomCoverageMetric(CoverageMetricBase):
    # Statements covered is used for
    # coverage information.
    def __init__(self):
        super().__init__()

    # TODO : Implement this
    def compareCoverage(self, curr_metric, total_metric):
        # must compare curr_metric and total_metric
        # True if Improved Coverage else False
        return not any(all(curr == total[i] for curr, total in zip(curr_metric, total_metric))
                   for i in range(len(total_metric)) if len(total_metric[i]) == len(curr_metric))

    # TODO : Implement this
    def updateTotalCoverage(self, curr_metric, total_metric):
        # Compute the total_metric coverage and return it (list)
        # this changes if new coverage is seen for a
        # given input.
        
        if curr_metric not in total_metric and self.compareCoverage(curr_metric, total_metric):
            total_metric.append(curr_metric)
        return total_metric

class CustomMutator(MutatorBase):
    def __init__(self):
        pass

    # TODO : Implement this
    def mutate(self, input_data, coverageInfo, irList):
        # Mutate the input data and return it
        # coverageInfo is of type CoverageMetricBase
        # Don't mutate coverageInfo
        # irList : List of IR Statments (Don't Modify)
        # input_data.data -> type dict() with {key : variable(str), value : int}
        m_data = input_data.data.copy()

        if m_data:
            variable_to_mutate = random.choice(list(m_data.keys()))
            new_value = random.randint(-20, 20)

            m_data[variable_to_mutate] = new_value

        mutated_input = InputObject(data=m_data)
        return mutated_input

# Reuse code and imports from
# earlier submissions (if any).

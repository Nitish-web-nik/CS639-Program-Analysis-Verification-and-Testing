from z3 import *
import argparse
import json
import sys
import os 
import ast

def example(s):
    # To add symbolic variable x to solver
    s.addSymbVar('x')
    s.addSymbVar('y')
    # To add constraint in form of string
    s.addConstraint('x==5+y')
    s.addConstraint('And(x==y,x>5)')
    # s.addConstraint('Implies(x==4,y==x+8')
    # To access solvers directly use s.s.<function of z3>()
    print("constraints added till now",s.s.assertions())
    # To assign z=x+y
    s.addAssignment('z','x+y')
    # To get any variable assigned
    print("variable assignment of z =",s.getVar('z'))


sys.path.insert(0, '../KachuaCore/')
from sExecutionInterface import *
import z3solver as zs
from irgen import *
from interpreter import *

def checkEq(args, ir):
    # Opening the first JSON file for reading and parsing
    with open("../Submission/testData4.json", "r+") as filewoholes:
        fwoholes = json.load(filewoholes)  # Loading JSON data into fwoholes dictionary

    # Opening the second JSON file for reading and parsing
    with open("../Submission/testData3.json", "r+") as filewholes:
        fwholes = json.load(filewholes)  # Loading JSON data into fwholes dictionary

    # Creating an instance of a Z3 solver and assign it to the variable s
    s = zs.z3Solver()

    # Iterating through pairs of keys (key1 and key2) where key1 is from fwoholes and key2 is from fwholes
    for key1, key2 in [(k1, k2) for k1 in fwoholes.keys() for k2 in fwholes.keys() if fwoholes[k1]['params'] == fwholes[k2]['params']]:
        # Printing various data from both JSON files on the output console
        print(fwholes[key2]['params'])
        print(fwoholes[key1]['params'])
        print(fwholes[key2]['symbEnc'])
        print(fwoholes[key1]['symbEnc'])

        # Extracting parameter values and symbolic encodings from the JSON data
        j_params_s1 = fwoholes[key1]['params']
        j_params_s2 = fwholes[key2]['params']
        j_s1 = fwoholes[key1]['symbEnc']
        j_s2 = fwholes[key2]['symbEnc']

        # Replacing single quotes with double quotes and parse the JSON strings into dictionaries
        dict1 = json.loads(j_s1.replace("'", "\""))
        dict2 = json.loads(j_s2.replace("'", "\""))
        dict3 = json.loads(j_params_s1.replace("'", "\""))
        dict4 = json.loads(j_params_s2.replace("'", "\""))

        # Adding symbolic variables to the Z3 solver
        [s.addSymbVar(t) for t in dict3.keys()]

        # Adding constraints to the Z3 solver for each symbolic variable
        [s.addConstraint(f"{dict1[t]}=={dict2[t]}") for t in dict3.keys()]

    # Checking if the constraints are satisfiable
    res = s.s.check()
    print(res)

    # If the constraints are satisfiable (sat), print the model obtained from the solver
    if str(res) == "sat":
        m = s.s.model()
        print(m)

# Printing a message indicating the successful end of the program
print("---Program Ended Successfully---")

if __name__ == '__main__':
    cmdparser = argparse.ArgumentParser(
        description='symbSubmission for assignment Program Synthesis using Symbolic Execution')
    cmdparser.add_argument('progfl')
    cmdparser.add_argument('-b', '--bin', action='store_true', help='load binary IR')
    cmdparser.add_argument('-e', '--output', default=list(), type=ast.literal_eval,
                           help="pass variables to kachua program in python dictionary format")
    args = cmdparser.parse_args()
    ir = loadIR(args.progfl)
    checkEq(args, ir)
    exit()

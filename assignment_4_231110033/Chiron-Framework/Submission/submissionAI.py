import copy
import math
import sys
from typing import overload
# Libraries added by me
from xmlrpc.client import MAXINT, MININT
import cfg
from collections import namedtuple
import json

sys.path.insert(0, "../KachuaCore/")

import cfg.kachuaCFG as cfgK
import cfg.cfgBuilder as cfgB
from interfaces.abstractInterpretationInterface import  *
import kast.kachuaAST as kachuaAST
import abstractInterpretation as AI

'''
    Class for interval domain
    
'''

INPUT_VAR_RANGE = [-1000,1000]
INI_X = [0,0]
INI_Y = [0,0]
DIRECTION = ['+x', '-x' , '+y' , '-y']
class Interval(abstractValueBase):

    '''Initialize abstract value'''
    def __init__(self, data):
        pass

    '''To display abstract values'''
    def __str__(self):
        pass

    '''To check whether abstract value is bot or not'''
    def isBot(self):
        pass

    '''To check whether abstract value is Top or not'''
    def isTop(self):
        pass

    '''Implement the meet operator'''
    def meet(self, other):
        pass

    '''Implement the join operator'''
    def join(self, other):
        pass

    '''partial order with the other abstract value'''
    def __le__(self, other):
        pass

    '''equality check with other abstract value'''
    def __eq__(self, other):
        pass

    '''
        Add here required abstract transformers
    '''
    pass

assgn_dict = {}

def operator_range(var, op, val):
    value1 = assgn_dict.get(var, {'left': MININT, 'right': MAXINT})
    value2 = int(val)

    if op in {'<', '<='}:
        true_range = {'left': MININT, 'right': value2 - (op == '<')}
        false_range = {'left': value2 + (op == '<'), 'right': MAXINT}
    elif op in {'>', '>='}:
        true_range = {'left': value2 + (op == '>'), 'right': MAXINT}
        false_range = {'left': MININT, 'right': value2 - (op == '>')}
    elif op == '==':
        true_range = false_range = {'left': value2, 'right': value2, 'except': value2}
    else:
        raise ValueError(f"Unsupported operator: {op}")

    
    final_true_range = {'left': max(true_range['left'], value1['left']), 'right': min(true_range['right'], value1['right'])}
    # This represents the intersection of the current range (value1) and the calculated true range.
    # It ensures that the new range doesn't exceed the bounds of the current range.
    final_false_range = {'left': max(false_range['left'], value1['left']), 'right': min(false_range['right'], value1['right'])}

    return [final_true_range, final_false_range]
  

    

def area(a, b):  
    # print(a.xmax, b.xmax)
    # print(a.xmin, b.xmin)
    # print(a.ymax, b.ymax)
    # print(a.ymin, b.ymin)
    dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
    '''
    dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin) calculates the horizontal overlap
    between the rectangles. It finds the minimum right x-coordinate (xmax) among the two rectangles
    and subtracts the maximum left x-coordinate (xmin) among the two rectangles.
    '''
    dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
    # If either of dx or dy will become negative means the area will 
    # be negative but it can't be so, in this case the answer will be safe 
    if (dx>=0) and (dy>=0):
        return dx*dy 

class ForwardAnalysis():
    def __init__(self):
        pass

    '''
        This function is to initialize in of the basic block currBB
        Returns a dictinary {varName -> abstractValues}
        isStartNode is a flag for stating whether currBB is start basic block or not
    '''
    def initialize(self, currBB, isStartNode):
        val = {}
        #Your additional initialisation code if any
        if(isStartNode):
            val = { 'IN' : {'X' : {'left' : INI_X[0] , 'right' : INI_X[1]} , 'Y' : {'left' : INI_Y[0] , 'right' : INI_Y[1]} , 'D' : DIRECTION[0] , 'is_bot' : False}}
        return val

    #just a dummy equallity check function for dictionary
    def isEqual(self, dA, dB):
        for i in dA.keys():
            if i not in dB.keys():
                return False
            if dA[i] != dB[i]:
                return False
        return True

    '''
        Transfer function for basic block 'currBB' 
        args: In val for currBB, currBB
        Returns newly calculated values in a form of list
    '''
    def transferFunction(self, currBBIN, currBB):
        #implement your transfer function here
        current_out = copy.deepcopy(currBBIN)
        if(currBB.__str__() != 'END'):
            if(type(currBB.instrlist[0][0]) == kachuaAST.MoveCommand):
                flag = 0
                list = str.split(str(currBB.instrlist[0][0]))
                if(type(currBB.instrlist[0][0].expr) == kachuaAST.Num):
                    mov = {'left' : int(currBB.instrlist[0][0].expr.__str__()),'right' : int(currBB.instrlist[0][0].expr.__str__())}

                elif(str(currBB.instrlist[0][0].expr) in assgn_dict.keys()):
                    mov = assgn_dict[list[1]]
                else:
                    assgn_dict[str(currBB.instrlist[0][0].expr)] = {'left' : INPUT_VAR_RANGE[0], 'right' : INPUT_VAR_RANGE[1]}
                    mov = (assgn_dict[list[1]])

                if(list[0] == "left"):
                    if(currBBIN['IN']['D'] == '+x'):
                        current_out['IN']['D'] = '+y'
                    elif(currBBIN['IN']['D'] == '-x'):
                        current_out['IN']['D'] = '-y'
                    elif(currBBIN['IN']['D'] == '+y'):
                        current_out['IN']['D'] = '-x'
                    elif(currBBIN['IN']['D'] == '-y'):
                        current_out['IN']['D'] = '+x'
                if(list[0] == "right"):
                    if(currBBIN['IN']['D'] == '+x'):
                        current_out['IN']['D'] = '-y'
                    elif(currBBIN['IN']['D'] == '-x'):
                        current_out['IN']['D'] = '+y'
                    elif(currBBIN['IN']['D'] == '+y'):
                        current_out['IN']['D'] = '+x'
                    elif(currBBIN['IN']['D'] == '-y'):
                        current_out['IN']['D'] = '-x'
                if(flag == 0):
                    if(list[0] == "forward"):
                        if(currBBIN['IN']['D'] == '+x'):
                            if(int(mov['left']) + currBBIN['IN']['X']['left'] < currBBIN['IN']['X']['left']):
                                current_out['IN']['X']['left'] = int(mov['left']) + currBBIN['IN']['X']['left']
                            if(int(mov['right']) + currBBIN['IN']['X']['right'] > currBBIN['IN']['X']['right']):
                                current_out['IN']['X']['right'] = int(mov['right']) + currBBIN['IN']['X']['right'] 
                        if(currBBIN['IN']['D'] == '-x'):
                            if(-1*int(mov['left']) + currBBIN['IN']['X']['left'] < currBBIN['IN']['X']['left']):
                                current_out['IN']['X']['left'] = -1*int(mov['left']) + currBBIN['IN']['X']['left']
                            if(-1*int(mov['right']) + currBBIN['IN']['X']['right'] > currBBIN['IN']['X']['right']):
                                current_out['IN']['X']['right'] = -1*int(mov['right']) + currBBIN['IN']['X']['right']
                        if(currBBIN['IN']['D'] == '+y'):
                            if(int(mov['left']) + currBBIN['IN']['Y']['left'] < currBBIN['IN']['Y']['left']):
                                current_out['IN']['Y']['left'] = int(mov['left']) + currBBIN['IN']['Y']['left']
                            if(int(mov['right']) + currBBIN['IN']['Y']['right'] > currBBIN['IN']['Y']['right']):
                                current_out['IN']['Y']['right'] = int(mov['right']) + currBBIN['IN']['Y']['right'] 
                        if(currBBIN['IN']['D'] == '-y'):
                            if(-1*int(mov['left']) + currBBIN['IN']['Y']['left'] < currBBIN['IN']['Y']['left']):
                                current_out['IN']['Y']['left'] = -1*int(mov['left']) + currBBIN['IN']['Y']['left']
                            if(-1*int(mov['right']) + currBBIN['IN']['Y']['right'] > currBBIN['IN']['Y']['right']):
                                current_out['IN']['Y']['right'] = -1*int(mov['right']) + currBBIN['IN']['Y']['right'] 

                         

                    if(list[0] == "backward"):
                        if(currBBIN['IN']['D'] == '-x'):
                            if(int(mov['left']) + currBBIN['IN']['X']['left'] < currBBIN['IN']['X']['left']):
                                current_out['IN']['X']['left'] = int(mov['left']) + currBBIN['IN']['X']['left']
                            if(int(mov['right']) + currBBIN['IN']['X']['right'] > currBBIN['IN']['X']['right']):
                                current_out['IN']['X']['right'] = int(mov['right']) + currBBIN['IN']['X']['right'] 
                        if(currBBIN['IN']['D'] == '+x'):
                            if(-1*int(mov['left']) + currBBIN['IN']['X']['left'] < currBBIN['IN']['X']['left']):
                                current_out['IN']['X']['left'] = -1*int(mov['left']) + currBBIN['IN']['X']['left']
                            if(-1*int(mov['right']) + currBBIN['IN']['X']['right'] > currBBIN['IN']['X']['right']):
                                current_out['IN']['X']['right'] = -1*int(mov['right']) + currBBIN['IN']['X']['right']
                        if(currBBIN['IN']['D'] == '-y'):
                            if(int(mov['left']) + currBBIN['IN']['Y']['left'] < currBBIN['IN']['Y']['left']):
                                current_out['IN']['Y']['left'] = int(mov['left']) + currBBIN['IN']['Y']['left']
                            if(int(mov['right']) + currBBIN['IN']['Y']['right'] > currBBIN['IN']['Y']['right']):
                                current_out['IN']['Y']['right'] = int(mov['right']) + currBBIN['IN']['Y']['right'] 
                        if(currBBIN['IN']['D'] == '+y'):
                            if(-1*int(mov['left']) + currBBIN['IN']['Y']['left'] < currBBIN['IN']['Y']['left']):
                                current_out['IN']['Y']['left'] = -1*int(mov['left']) + currBBIN['IN']['Y']['left']
                            if(-1*int(mov['right']) + currBBIN['IN']['Y']['right'] > currBBIN['IN']['Y']['right']):
                                current_out['IN']['Y']['right'] = -1*int(mov['right']) + currBBIN['IN']['Y']['right'] 

            
            elif(type(currBB.instrlist[0][0]) == kachuaAST.ConditionCommand):
                if(str(currBB.instrlist[0][0]) != 'False'):
                    l = len(currBB.instrlist[0][0].__str__())
                    var,op,val = str.split(currBB.instrlist[0][0].__str__()[1:l-1])
                    [true_range,false_range] = operator_range(var,op,val)
                    current_out1 = copy.deepcopy(current_out)
                    current_out2 = copy.deepcopy(current_out)
                    current_out1['IN'][var] = {'left' : true_range['left'] , 'right' : true_range['right']} 
                    current_out2['IN'][var] = {'left' : false_range['left'] , 'right' : false_range['right']} 
                    outVal = [{'OUT' : current_out1['IN']},{'OUT' : current_out2['IN']}]
                    return outVal
                else:
                    outVal = [{'OUT' : current_out['IN']},{'OUT' : current_out['IN']}]
                    return outVal
        outVal = [{'OUT' : current_out['IN']}]
        return outVal

    '''
        Define the meet operation
        Returns a dictionary {varName -> abstractValues}
    '''

    
    def meet(self, predList):
        assert isinstance(predList, list)

        final_x_left = [i['OUT']['X']['left'] for i in predList]
        final_x_right = [i['OUT']['X']['right'] for i in predList]
        final_y_left = [i['OUT']['Y']['left'] for i in predList]
        final_y_right = [i['OUT']['Y']['right'] for i in predList]
        is_bot = any(i['OUT']['is_bot'] for i in predList)

        not_bot_pred = next((i for i, pred in enumerate(predList) if not pred['OUT']['is_bot']), None)
        dir = [predList[not_bot_pred]['OUT']['D']] if not_bot_pred is not None else []

        if len(predList) == 1:
            meetVal = {'IN': predList[0]['OUT'], 'is_bot': is_bot}
        elif len(set(pred['OUT']['is_bot'] for pred in predList)) == 2:
            meetVal = {'IN': predList[not_bot_pred]['OUT'], 'is_bot': False}
        elif len(set(dir)) == 1:
            meetVal = {
                'IN': {
                    'X': {'left': min(final_x_left), 'right': max(final_x_right)},
                    'Y': {'left': min(final_y_left), 'right': max(final_y_right)},
                    'D': dir[0],
                    'is_bot': is_bot
            }
        }
        else:
            print("\n\"KACHUA IS UNSAFE\" :: SINCE AT MEET DIRECTIONS OF BOTH THE PATHS ARE DIFFERENT")
            sys.exit()

        return meetVal


def analyzeUsingAI(ir, filename):
    '''
        get the cfg outof IR
        each basic block consists of single statement
    '''
    cfg = cfgB.buildCFG(ir, "cfg", True)
    cfgB.dumpCFG(cfg, "x")
    print(filename)
    # file = open("../KachuaCore" + filename.replace(".tl", ".json")[1:],"r+")
    file = open("../KachuaCore/"+filename.replace(".tl" , ".json"),"r+")
    
    d = json.loads(file.read())
    
    #implement your analysis according to the questions on each basic blocks
    Magarmach_point_1 = d['reg'][0]
    Magarmach_point_2 = d['reg'][1]

    for i in ir:
        if('__rep_counter_1' in str(i[0])):
            print("\n\"KACHUA IS UNSAFE\" :: KACHUA CAN BE INSIDE MAGARMACH'S REGION ")
            sys.exit()
        if(type(i[0]) == kachuaAST.AssignmentCommand):
            if(':' in (i[0].rexpr.__str__())):
                print("\n\"KACHUA IS UNSAFE\" :: KACHUA CAN BE INSIDE MAGARMACH'S REGION ")
                sys.exit()
            assgn_dict[i[0].lvar.__str__()] = {'left' : int(i[0].rexpr.__str__()), 'right' : int(i[0].rexpr.__str__())}
    # call worklist and get the in/out values of each basic block
    bbIn, bbOut = AI.worklistAlgorithm(cfg)
    # print('\nIN of all basic blocks are :\n\n ',bbIn)
    # print('\nOUT of all basic blocks are :\n\n ',bbOut)
    final_turtle_X_pos = bbOut['END'][0]['OUT']['X']
    final_turtle_Y_pos = bbOut['END'][0]['OUT']['Y']

    Kachua_point_1 = [final_turtle_X_pos['left'], final_turtle_Y_pos['left']]
    Kachua_point_2 = [final_turtle_X_pos['right'], final_turtle_Y_pos['right']]

    Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')

    ra = Rectangle(min(Magarmach_point_1[0], Magarmach_point_2[0]), 
               min(Magarmach_point_1[1], Magarmach_point_2[1]),
               max(Magarmach_point_1[0], Magarmach_point_2[0]),
               max(Magarmach_point_1[1], Magarmach_point_2[1]))

    rb = Rectangle(min(Kachua_point_1[0], Kachua_point_2[0]), 
               min(Kachua_point_1[1], Kachua_point_2[1]),
               max(Kachua_point_1[0], Kachua_point_2[0]),
               max(Kachua_point_1[1], Kachua_point_2[1]))

    print("\nMAGARMACH region is from: " , Magarmach_point_1 ," TO " , Magarmach_point_2)
    print("\nKACHUA expected region is from: " , Kachua_point_1 ," TO " , Kachua_point_2)
    print ("\nOverlapping area of KACHUA and MAGARMACH regions   = ",area(ra, rb))
    if(area(ra,rb) == None):
        print("\n\"{VERIFIED} KACHUA IS SAFE :)\"  IMPLIES It won't lie in the MAGARMACH's region if started at X & Y AS : ",INI_X,"&",INI_Y , "respectively.")
    else:
        print("\n\"KACHUA IS UNSAFE :(\"  IMPLIES It will lie in the MAGARMACH's region if started at X & Y AS : ",INI_X,"&",INI_Y,"respectively.")
    
    pass

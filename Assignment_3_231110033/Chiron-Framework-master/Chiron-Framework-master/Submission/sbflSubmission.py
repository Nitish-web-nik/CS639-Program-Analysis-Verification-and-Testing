#!/usr/bin/env python3

import argparse
from collections import Counter
import math
import sys
import numpy as np

sys.path.insert(0, "../ChironCore/")
from irhandler import *
from ChironAST.builder import astGenPass
import csv


def fitnessScore(IndividualObject):
    """
    Parameters
    ----------
    IndividualObject : Individual (definition of this class is in ChironCore/sbfl.py)
        This is a object of class Individual. The Object has 3 elements
        1. IndividualObject.individual : activity matrix.
                                    type : list, row implies a test
                                    and element of rows are components.
        2. IndividualObject.fitness : fitness of activity matix.
                                    type : float
        3. Indivisual.fitness_valid : a flag used by Genetic Algorithm.
                                    type : boolean
    Returns
    -------
    fitness_score : flaot
        returns the fitness-score of the activity matrix.
        Note : No need to set/change fitness and fitness_valid attributes.
    """
    # Design the fitness function
    """
    Parameters
    ----------
    IndividualObject : Individual (definition of this class is in ChironCore/sbfl.py)
        This is a object of class Individual. The Object has 3 elements
        1. IndividualObject.individual : activity matrix.
                                    type : list, row implies a test
                                    and element of rows are components.
        2. IndividualObject.fitness : fitness of activity matix.
                                    type : float
        3. Indivisual.fitness_valid : a flag used by Genetic Algorithm.
                                    type : boolean
    Returns
    -------
    fitness_score : flaot
        returns the fitness-score of the activity matrix.
        Note : No need to set/change fitness and fitness_valid attributes.
    """
    # Design the fitness function
    fitness_score = 0
    activity_mat = np.array(IndividualObject.individual, dtype="int")
    activity_mat = activity_mat[:, : activity_mat.shape[1] - 1]
    # Use 'activity_mat' to compute fitness of it.
    # ToDo : Write your code here to compute fitness of test-suite
    unique_columns = {}

    for col in range(activity_mat.shape[1]):
        col_tuple = tuple(activity_mat[:, col])

        if col_tuple in unique_columns:
            unique_columns[col_tuple] += 1
        else:
            unique_columns[col_tuple] = 1

    cols = len(unique_columns)
    
    total_sum = np.sum(activity_mat)

    # Get the number of rows and columns
    r,c = activity_mat.shape

    # Calculate the density
    density = total_sum / (r * c)
        
    rows_as_tuples = [tuple(row) for row in activity_mat]

    # Use Counter to count the occurrences of each row
    row_counts = Counter(rows_as_tuples)

    # Convert the Counter object to a list of unique rows and their counts
    unique_rows_and_counts = list(row_counts.items())
    print(activity_mat)
    i=0
    for row, count in unique_rows_and_counts:
        i+=count*(count-1)
    if r*(r-1) !=0:
        div=1 - i/(r*(r-1))
    else:
        div = 1
    
    fitness_score = -1*(1-abs(1-2*density))*cols*div
    
    return fitness_score
# This class takes a spectrum and generates ranks of each components.
# finish implementation of this class.
class SpectrumBugs:
    def __init__(self, spectrum):
        self.spectrum = np.array(spectrum, dtype="int")
        self.comps = self.spectrum.shape[1] - 1
        self.tests = self.spectrum.shape[0]
        self.activity_mat = self.spectrum[:, : self.comps]
        self.errorVec = self.spectrum[:, -1]

    def getActivity(self, comp_index):
        """
        get activity of component 'comp_index'
        Parameters
        ----------
        comp_index : int
        """
        return self.activity_mat[:, comp_index]

    def suspiciousness(self, comp_index):
        """
        Parameters
        ----------
        comp_index : int
            component number/index of which you want to compute how suspicious
            the component is. assumption: if a program has 3 components then
            they are denoted as c0,c1,c2 i.e 0,1,2
        Returns
        -------
        sus_score : float
            suspiciousness value/score of component 'comp_index'
        """
        sus_score = 0
        # ToDo : implement the suspiciousness score function.
        comp_activity = self.getActivity(comp_index)
        total_failures = np.sum(self.errorVec)
        comp_failures = np.sum(self.errorVec * comp_activity)
        total_passes = self.tests - total_failures
        comp_passes = np.sum(comp_activity) - comp_failures
        cf=cp=0
        for n in range(0,len(self.activity_mat)):
            if self.activity_mat[n][comp_index]==1 and self.errorVec[n]==1:
                cf+=1
            if self.activity_mat[n][comp_index]==1 and self.errorVec[n]==0:
                cp+=1
        if total_failures > 0:
            # Calculate the Ochiai metric
            sus_score = comp_failures / np.sqrt(total_failures * (cf + cp))
        return sus_score

    def getRankList(self):
        """
        find ranks of each components according to their suspeciousness score.

        Returns
        -------
        rankList : list
            ranList will contain data in this format:
                suppose c1,c2,c3,c4 are components and their ranks are
                1,2,3,4 then rankList will be :
                    [[c1,1],
                     [c2,2],
                     [c3,3],
                     [c4,4]]
        """
        rankList = []
        # ToDo : implement rankList
        for i in range(len(self.activity_mat[0])):
            rankList.append([f"c{i+1}", self.suspiciousness(i)])
        rankList=sorted(rankList,key=lambda x:x[1],reverse=True)
        rank = 1
        rl=[[rankList[0][0],1]]
        for i in range(1, len(rankList)):
            if rankList[i][1] != rankList[i-1][1]:
                rank += 1
            rl.append([rankList[i][0],rank])
            
        print(rl)
        return rl


# do not modify this function.
def computeRanks(spectrum, outfilename):
    """
    Parameters
    ----------
    spectrum : list
        spectrum
    outfilename : str
        components and their ranks.
    """
    S = SpectrumBugs(spectrum)
    rankList = S.getRankList()
    with open(outfilename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(rankList)

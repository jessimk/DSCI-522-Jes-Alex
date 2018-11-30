#!/usr/bin/env python
# 02_EDA.py
# Jes Simkin and Alex Hope Nov, 2018
#
# This script produces histograms for each decision tree feature.
#
# Usage: Python src/02_EDA.py data/tidy_data_lebron_james.csv results/figs/EDA "lebron_james"


import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
parser.add_argument('player')
args = parser.parse_args()

def main():
    #read in data and set up feature list for iterating
    data = pd.read_csv(args.input_file).drop(['Unnamed: 0'], axis=1)
    features = list(data)
    #add an under score for file slug
    name_underscored= args.player.replace(" ", "_")

    #create histogram for each feature and save png
    for feature in features:

        missed = data[data.SHOT_RESULT == "missed"][feature]
        made = data[data.SHOT_RESULT == "made"][feature]

        fig, share = plt.subplots()

        plt.hist([missed, made], color=['darkorange', 'royalblue'], label=['Missed','Made'], bins = 15)
        plt.legend(title= "Shot Result")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.savefig(args.output_file+"_"+feature+"_"+name_underscored)

main()

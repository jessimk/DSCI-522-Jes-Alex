#!/usr/bin/env python
# 02_EDA.py
# Jes Simkin and Alex Hope Nov, 2018
#
# This script loads the raw shot log data, performs data cleaning and wrangling,
# and outputs a csv file for a specified player into the data folder.
#
# Usage: Rscript 01_loading_wrangling_data.R "lebron james" data/tidy_data_lebron_james.csv


import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

def main():
    data = pd.read_csv(args.input_file).drop(['Unnamed: 0'], axis=1)
    features = list(data)

    for feature in features:

        missed = data[data.SHOT_RESULT == "missed"][feature]
        made = data[data.SHOT_RESULT == "made"][feature]

        fig, share = plt.subplots()

        plt.hist([missed, made], color=['red', 'blue'], label=['Missed','Made'], bins = 15)
        plt.legend(title= "Shot Result")
        plt.title(feature.title())
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.savefig(args.output_file)

if __name__ == "__main__":
    main()

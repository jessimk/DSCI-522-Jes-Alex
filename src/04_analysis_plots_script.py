#!/usr/bin/env python
# 04_EDA.py
# Alex Hope and Jes Simkin, Nov, 2018
#
# This script produces a plot showing best decision tree depth and a plot
#   showing feature importances. It takes two csvs from sript 3, and produces
#   two plots.
#
# Usage:
#Python src/04_analysis_plots_script.py data/accuracies_lebron_james.csv data/features_lebron_james.csv results/figs/train-test-acc_lebron_james.png results/figs/best_features_lebron_james.png

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('input_file1')
parser.add_argument('input_file2')
parser.add_argument('output_file1')
parser.add_argument('output_file2')


args = parser.parse_args()

def main():

    #read in data and plot train and test accuracies
    accuracy_df = pd.read_csv(args.input_file1)
    plt.plot(accuracy_df[['depths']],accuracy_df[['train_accuracy']],label='Training Set')
    plt.plot(accuracy_df[['depths']],accuracy_df[['test_accuracy']],label='Test Set')
    plt.xlabel('Max Depth')
    plt.ylabel('Accuracy')
    plt.legend(title= "Analysis Data Sets")
    plt.savefig(args.output_file1)
    #clear plt canvas for next plot
    plt.clf()

    #read in data and plot feature importances
    feature_df= pd.read_csv(args.input_file2)
    feature_df = feature_df.sort_values('importances', ascending = False).reset_index(drop=True)
    features=feature_df['feature names']
    importances=feature_df['importances']
    plt.bar(feature_df['feature names'],feature_df['importances'])
    plt.xticks(feature_df['feature names'], rotation= 45)
    plt.ylabel('Feature Importance')
    plt.tight_layout()
    plt.savefig(args.output_file2)

main()

#!/usr/bin/env python
# 02_EDA.py
# Alex Hope and Jes Simkin, Nov, 2018
#
# This script produces a plot showing best decision tree depth and a plot
#   showing feature importances.
#
# Usage:
#Python src/04_analysis_plots_script.py data/accuracies_lebron_james.csv data/features_lebron_james.csv "lebron james" results/figs/

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('input_file1')
parser.add_argument('input_file2')
parser.add_argument('player')
parser.add_argument('output_dir')

args = parser.parse_args()

def main():
    #add an under score for file slug
    name_underscored= args.player.replace(" ", "_")

    #read in data and plot train and test accuracies
    accuracy_df = pd.read_csv(args.input_file1)
    fig, share = plt.subplots()
    plt.plot(accuracy_df[['depths']],accuracy_df[['train_accuracy']],label='train')
    plt.plot(accuracy_df[['depths']],accuracy_df[['test_accuracy']],label='test')
    plt.xlabel('Max Depth')
    plt.ylabel('Accuracy')
    plt.savefig(args.output_dir+"train-test-acc"+"_"+args.player)
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
    #plt.subplots_adjust(bottom=0.1)
    plt.tight_layout()
    plt.savefig(args.output_dir+"best_features_"+args.player)


main()

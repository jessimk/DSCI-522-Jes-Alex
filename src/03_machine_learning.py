
#!/usr/bin/env python
# 03_machine_learning.py
# Alex Hope and Jes Simkin Nov, 2018
#
# This script takes a csv, runs decision tree analysis and outputs two csvs:
#   one for later creating model depth and accuracy plotting, and
#   another for plotting feature importances.
#
# Usage
# Inputs: tidy csv path, output path for model test and train accuracies,
##         output path for model feature importances
# Outputs: csv of model accuracies, csv of model feature importances
# Example: Python src/03_machine_learning.py data/tidy_data_lebron_james.csv
##          data/accuracies_lebron_james.csv data/features_lebron_james.csv

import argparse
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file1')
parser.add_argument('output_file2')
args = parser.parse_args()

def main():

    #Read player data
    player_data = pd.read_csv(args.input_file)

    #Create X and y from player_data
    X= player_data.drop(['Unnamed: 0', 'SHOT_RESULT'], axis=1)
    y=player_data[['SHOT_RESULT']]

    #Split Dataset by 80-20
    Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2, random_state=231)

    #Try out different k values
    depths= range(1,40)
    train_accuracy=[]
    test_accuracy=[]
    for i in depths:
        player_shot_model= tree.DecisionTreeClassifier(max_depth=i, random_state=231, class_weight="balanced")
        player_shot_model.fit(Xtrain,ytrain)
        train_accuracy.append(player_shot_model.score(Xtrain,ytrain))
        player_shot_model.predict(Xtest)
        test_accuracy.append(player_shot_model.score(Xtest,ytest))

    #creates a df of train and test accuracies and depths for plotting in script 4
    train_df = pd.DataFrame(train_accuracy, columns=["train_accuracy"])
    test_df = pd.DataFrame(test_accuracy, columns=["test_accuracy"])
    depths_df = pd.DataFrame(list(depths), columns=["depths"])

    frames = [train_df, test_df, depths_df]
    train_test_df = pd.concat(frames, axis=1)

    train_test_df.to_csv(args.output_file1)

    #finds feature importances and create a plot-ready df of feature importances
    importances = player_shot_model.feature_importances_
    importances_df = pd.DataFrame(importances, columns=["importances"])
    feature_names_df= pd.DataFrame(list(X), columns=["feature names"])
    index_df = pd.DataFrame(list(range(len(X.columns.values))), columns=["index"])

    frames = [index_df, feature_names_df, importances_df]
    importances_df_csv = pd.concat(frames, axis=1)

    importances_df_csv["feature names"] = importances_df_csv["feature names"].str.replace("_"," ")
    importances_df_csv["feature names"] = importances_df_csv["feature names"].str.title()
    importances_df_csv["feature names"] = importances_df_csv["feature names"].str.replace("Shot Dist","Shot Distance")
    importances_df_csv["feature names"] = importances_df_csv["feature names"].str.replace("Pts Type","Points Type")
    importances_df_csv["feature names"] = importances_df_csv["feature names"].str.replace("Close Def Dist","Closest Defender")

    #export a csv for plotting in script 4
    importances_df_csv.to_csv(args.output_file2)

main()

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('input_file2')

parser.add_argument('output_file')
args = parser.parse_args()

def main():
    accuracy_df = pd.read_csv(args.input_file)
    accuracy_df=pd.DataFrame(accuracy_df)
    test_train_plot = plt.plot(accuracy_df[['depths']],accuracy_df[['train_accuracy']],label='train')+plt.plot(accuracy_df[['depths']],accuracy_df[['test_accuracy']],label='test')
    plt.xlabel('Max Depth')
    plt.ylabel('Accuracy')
    plt.savefig("results/figs/train-test-acc.png") #args.output_file
    
    plt.clf()
    
    
    feature_df= pd.read_csv(args.input_file2)
    feature_df = pd.DataFrame(feature_df)
    features=feature_df['feature names']
    
    importances=feature_df['importances']
    bar=plt.bar(feature_df['feature names'],feature_df['importances'])
    plt.xticks(feature_df['feature names'], rotation= 45)
    plt.ylabel('Feature Importance')
    plt.subplots_adjust(bottom=0.1)
    plt.savefig("results/figs/best_features.png") #args.output_file
    
    plt.clf()


    
main()

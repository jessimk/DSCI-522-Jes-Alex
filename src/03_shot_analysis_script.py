
# coding: utf-8

# In[4]:


#Read input file
import argparse
import pandas as pd
import numpy as np
from sklearn import tree 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import graphviz

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

def main():
    #Read player data
    player_data = pd.read_csv(args.input_file)
    
    #Create X and y from player_data
    X= player_data.drop(['Unnamed: 0', 'SHOT_RESULT'], axis=1)
    y=player_data[['SHOT_RESULT']]
    
    #Split Dataset by 80-20
    Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2)
    
    #Try out different k values and plot
    depths= range(1,40)
    train_accuracy=[]
    test_accuracy=[]
    for i in depths:
        player_shot_model= tree.DecisionTreeClassifier(max_depth=i)
        player_shot_model.fit(Xtrain,ytrain)
        train_accuracy.append(player_shot_model.score(Xtrain,ytrain))
        player_shot_model.predict(Xtest)
        test_accuracy.append(player_shot_model.score(Xtest,ytest))
    best_test = str(max(test_accuracy))
    print('The test set accuracy for this player is '+ str(best_test))
    best_depth = depths[np.argmax(test_accuracy)] 
    print('The best depth for the Decision Tree Classifier is ' + str(best_depth))
    #caption_text = "Here is the plotted training and test accuracy for various depths.We used our best depth of "+str(best_depth)+" which had a testing set accuracy of "+str(best_test)
    test_train_plot = plt.plot(depths,train_accuracy,label='train')+plt.plot(depths,test_accuracy,label='test') #plt.text(0,0,caption_text)

    plt.savefig("results/figs/train-test-acc.png") #args.output_file
    plt.clf()
        
    importances = player_shot_model.feature_importances_
    feature_names= pd.DataFrame(list(X))
    plt.bar(range(len(X.columns.values)), player_shot_model.feature_importances_)
    plt.xticks(range(len(X.columns.values)),X.columns.values, rotation= 90)
    plt.savefig("results/figs/best_features.png") #args.output_file
    plt.clf()
    
main()









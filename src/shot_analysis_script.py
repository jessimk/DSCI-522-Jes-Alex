
# coding: utf-8

# In[2]:


#Read input file
import argparse
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

def main():
    #Read player data
    player_data = pd.read_csv(args.input_file, sep = ' ', header= None)
    
    #Create X and y from player_data
    X= player_data.drop(['Unnamed: 0', 'SHOT_RESULT'])
    y=player_data[['SHOT_RESULT']]
    
    #Split Dataset by 80-20
    Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2)
    
    #Try out different k values and plot
    depths= range(1,40)
    train_accuracy=[]
    test_accuracy=[]
    for i in depths:
        player_shot_model=DecisionTreeClassifier(max_depth=i)
        player_shot_model.fit(Xtrain,ytrain)
        train_accuracy.append(player_shot_model.score(Xtrain,ytrain))
        shot_model.predict(Xtest)
        test_accuracy.append(shot_model.score(Xtest,ytest))
    
    best_depth = depths[np.argmax(test_accuracy)] 
    test_train_plot = plt.plot(depths,train_accuracy,label='train')+plt.plot(depths,test_accuracy,label='test')
    plt.savefig(args.output_file)
    
    importances = player_shot_model.feature_importances_


    feature_names= pd.DataFrame(list(X))

    plt.bar(range(len(X.columns.values)), player_shot_model.feature_importances_)
    plt.xticks(range(len(X.columns.values)),X.columns.values, rotation= 90)
    best_model = DecisionTreeClassifier(max_depth = best_depth)
    tree_graph = tree.export_graphviz(best_model, out_file=None, 
                             feature_names=feature_cols,  
                             class_names=class_names,  
                             filled=True, rounded=True,  
                             special_characters=True, **kwargs)
    graph=graphviz.Source(tree_graph)
    graph.render(save_file_prefix)
    return graph

if __name__ == "__main__":
    main()


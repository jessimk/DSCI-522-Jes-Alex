
# coding: utf-8

# In[ ]:


import argparse
import pandas as pd
import numpy as np
from sklearn import tree 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import graphviz

#Read player data
player_data = pd.read_csv("../data/tidy_data_lebron_james.csv")

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

best_depth = depths[np.argmax(test_accuracy)] 

test_train_plot = plt.plot(depths,train_accuracy,label='train')+plt.plot(depths,test_accuracy,label='test')

plt.savefig("abc.png") #args.output_file
plt.clf()


# In[ ]:


importances = player_shot_model.feature_importances_
feature_names= pd.DataFrame(list(X))
plt.bar(range(len(X.columns.values)), player_shot_model.feature_importances_)
plt.xticks(range(len(X.columns.values)),X.columns.values, rotation= 90)
plt.savefig("importances.png") #args.output_file
plt.clf()


Report
================

A Classification Decision Tree for Lebron James's Shots
=======================================================

Authors: Alex Hope, Jes Simkin Nov, 2018

Question
--------

Considering there are hundreds of players in the NBA with differing skillsets and styles of play, we narrowed our analyses to simply a single player, Lebron James. We did this to hopefully get at the nuances of what conditions best explain Lebron's shooting percentage and marvellous talent. Our question is a predictive one, namely, we are interested in using a set of measurements to predict another measurement about a single individual.

Our question for this analysis is:

**What are the three strongest predictors for determining whether Lebron makes or misses a shot?**

![alt tag](https://media.giphy.com/media/l0MYwdebx8o0XI56E/giphy-tumblr.gif)

[GIF Source](https://media.giphy.com/media/l0MYwdebx8o0XI56E/giphy-tumblr.gif)

Exploring The Data
------------------

We have chosen to work with 8 features. To get a sense of the features and build our intuition around which might end up being top predictors, we explored the distribution of each feature, grouped by shot result (made or missed).

Here are a few features with distributions that might suggest they may be important in our model later on.

### Closest Defender (ft): ![alt tag](../results/figs/EDA_CLOSE_DEF_DIST_lebron_james.png)

### Number of Dribbles: ![alt tag](../results/figs/EDA_DRIBBLES_lebron_james.png)

### Time on the Shot Clock (seconds): ![alt tag](../results/figs/EDA_SHOT_CLOCK_lebron_james.png)

### Shot Distance (ft): ![alt tag](../results/figs/EDA_SHOT_DIST_lebron_james.png)

Analysis
--------

### How our model performs:

![alt tag](../results/figs/train-test-acc_lebron%20james.png)

### Top Three Features:

![alt tag](../results/figs/best_features_lebron%20james.png)

<center>
<img src="https://media.giphy.com/media/lKafiHISf6FEtciruw/giphy.gif">
</center>
Observations
------------

Our best tree depth was a depth of 7 with a test set accuracy of 60% for predicting whether Lebron James makes or misses a shot.

We were surprised by the limitations of our features in predicting whether Lebron makes a shot or not.

It appears that there might be other features to consider, or that there's more to the game of basketball than can be encoded.

\[...Insert what we might also consider doing differently here...\]

References
----------

-   Lebron James Shot Log from the 2014-2015 NBA Season. Raw Data Source: [Kaggle, NBA Shot Logs Dataset](https://www.kaggle.com/dansbecker/nba-shot-logs/home)
-   Data Analysis Pipeline Example by Tiffany Timbers for UBC DSCI 522 (2018) [Github Repo](https://github.com/ttimbers/data_analysis_pipeline_eg/tree/v1.1)
-   Feature Importance by Chris Albon
    *l**i**n**k*
     (<https://chrisalbon.com/machine_learning/trees_and_forests/feature_importance/>)

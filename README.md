# A Classification Decision Tree for Lebron James's Shots 
   
   
### Authors 

- Alex Hope [@ehhope](https://github.com/ehhope)  
- Jes Simkin [@jessimk](https://github.com/jessimk) 

### Goal

- Create a decision tree model for Lebron James's shots. Use our model to find the three strongest predictors for determining whether Lebron makes or misses a shot.

### Dependencies

- **R**: 
	- `tidyverse  v1.2.1`

- **Python**: 
	- `argparse v1.1`
	- `pandas v0.20.3`
	- `matplotlib v3.0.1`
	- `numpy v1.15.4`
	- `scikit-learn v0.20.1`

### Usage
1. Clone this repo.
2. Run these commands:

`Rscript src/01_loading_wrangling.R "lebron james"	data/shot_logs_raw.csv data/tidy_data_lebron_james.csv`
`python src/02_EDA.py data/tidy_data_lebron_james.csv results/figs/EDA "lebron james"`
`python src/03_machine_learning.py data/tidy_data_lebron_james.csv data/accuracies_lebron_james.csv data/features_lebron_james.csv`
`python src/04_analysis_plots_script.py data/accuracies_lebron_james.csv data/features_lebron_james.csv results/figs/train-test-acc_lebron_james.png results/figs/best_features_lebron_james.png`
`Rscript -e "rmarkdown::render('docs/Report.Rmd')"`

OR

Use Make and run: 

`make all`
  
  
_✨Note: We plan to update our scripts so that they are flexible and robust enough to be able to run our analysis for any player in the data set. ✨_

  
<p align="center"> 🏀 🏀 🏀</p>


### What you'll find in this repo:

### [Data](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/tree/master/data)

- 2014-2015 NBA Season Shot Log from [Kaggle; NBA Shot Logs Dataset](https://www.kaggle.com/dansbecker/nba-shot-logs/home)

- Other CSV's created with our scripts
  
### [Documents](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/tree/master/docs)

- [Proposal](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/docs/Proposal.ipynb)

- [Report](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/docs/Report.md)


### [Results](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/tree/master/results/figs)

- Figures from our Analysis

### [Scripts](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/tree/master/src)

- `01_loading_wrangling.R`, [loads and wrangles data](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/src/01_loading_wrangling.R)

- `02_EDA.py`, [creates exploratory data analysis plots](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/src/02_EDA.py)
	
- `03_machine_learning.py`, [performs machine learning](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/src/03_machine_learning.py)

- `04_analysis_plots_script.py`, [creates plots from machine learning findings](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/src/04_analysis_plots_script.py)

</br>	
<p align="center">
👑
</p>

<p align="center">   
<a href="https://media.giphy.com/media/xT4uQfHn1CUGyYsiiY/giphy.gif"><img width="200" height="200" src="https://media.giphy.com/media/xT4uQfHn1CUGyYsiiY/giphy.gif"></a>

</p>
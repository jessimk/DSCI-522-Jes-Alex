# A Classification Decision Tree for Lebron James's Shots 
   
   
### Authors: 

- Alex Hope [@ehhope](https://github.com/ehhope)  
- Jes Simkin [@jessimk](https://github.com/jessimk) 

### [Data](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/tree/master/data)

- Lebron James Shot Log from the 2014-2015 NBA Season, raw data source: [Kaggle, NBA Shot Logs Dataset](https://www.kaggle.com/dansbecker/nba-shot-logs/home)

- Other CSV's created with our scripts
  
### [Documents](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/tree/master/docs)

- Proposal: [Proposal](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/docs/Proposal.ipynb)

- Milestone1: 
	- [Release 2.0](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/releases)
	- [Draft Report (md)](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/docs/Report.md)
	- [Draft Report (Rmd)](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/docs/Report.Rmd)

  
### [Results](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/tree/master/results/figs)

- Figures from our Analysis

### [Scripts](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/tree/master/src)

- `01_loading_wrangling.R`, [loads and wrangles data](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/src/01_loading_wrangling.R)

	- Takes 1 input file (reads raw data in data)
	- Delivers 1 output file

- `02_EDA.py`, [creates exploratory data analysis plots](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/src/02_EDA.py)
	
	 - Takes 1 input file (wrangled data for specific player)
	 - Delivers 9 output files as EDA figures (.png)

- `03_machine_learning.py`, [performs machine learning](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/src/03_machine_learning.py)
	
	- Takes 1 input file (wrangled player_data)
	- Delivers 2 output files (1 dataframe for train and test plot in script 4, 1 dataframe for feature importance in script 4)

- `04_analysis_plots_script.py`, [creates plots from machine learning findings](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/src/04_analysis_plots_script.py)
	
	- Takes 2 input files (1 dataframe for train-test plot, 1 dataframe for feature importance)
	- Delivers 2 output files stored in results/figs under accuracy and features (.png)




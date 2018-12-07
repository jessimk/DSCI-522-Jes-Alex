## What you'll find in this folder:

- `01_loading_wrangling.R`, [loads and wrangles data](https://github.com/UBC-MDS/DSCI-522-Jes-Alex/blob/master/src/01_loading_wrangling.R)

	- Takes 1 input file (reads raw data in data)
	- Allows you to select any player from dataset in argument, and will wrangle data for specific player prior to EDA.
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

### Dependency Graph

<a href="https://github.com/jessimk/DSCI-522-Jes-Alex/blob/master/src/Makefile.png?raw=true"></a>
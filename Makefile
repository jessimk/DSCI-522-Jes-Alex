# Makefile Structure for Decision Tree Analysis of Lebron James

# Driver script
# Alex Hope, Jes Simkin Nov 2018

# This script uses a decision tree classification model to determine the
#  three strongest predictors for whether Lebron makes or misses a shot.

# This script takes no arguments.


# usage: make all

all: docs/Report.md

# load and tidy data
data/tidy_data_lebron_james.csv : data/shot_logs_raw.csv src/01_loading_wrangling.R
	Rscript src/01_loading_wrangling.R "lebron james"	data/shot_logs_raw.csv data/tidy_data_lebron_james.csv

# plot EDA
results/figs/EDA_SHOT_CLOCK_lebron_james.png results/figs/EDA_SHOT_NUMBER_lebron_james.png results/figs/EDA_SHOT_DIST_lebron_james.png results/figs/EDA_SHOT_RESULT_lebron_james.png results/figs/EDA_TOUCH_TIME__lebron_james.png results/figs/EDA_PERIOD_lebron_james.png results/figs/EDA_PTS_TYPE_lebron_james.png results/figs/EDA_DRIBBLES_lebron_james.png results/figs/EDA_CLOSE_DEF_DIST_lebron_james.png: data/tidy_data_lebron_james.csv src/02_EDA.py
	Python src/02_EDA.py data/tidy_data_lebron_james.csv results/figs/EDA "lebron james"

# export model data
data/accuracies_lebron_james.csv data/features_lebron_james.csv: data/tidy_data_lebron_james.csv src/03_machine_learning.py
	Python src/03_machine_learning.py data/tidy_data_lebron_james.csv data/accuracies_lebron_james.csv data/features_lebron_james.csv

# plot analysis
results/figs/train-test-acc_lebron_james.png results/figs/best_features_lebron_james.png: data/accuracies_lebron_james.csv data/features_lebron_james.csv src/04_analysis_plots_script.py
	Python src/04_analysis_plots_script.py data/accuracies_lebron_james.csv data/features_lebron_james.csv results/figs/train-test-acc_lebron_james.png results/figs/best_features_lebron_james.png

# make report
docs/Report.md: docs/Report.Rmd results/figs/EDA_CLOSE_DEF_DIST_lebron_james.png
		Rscript -e "rmarkdown::render('docs/Report.Rmd')"

clean:
	rm -f data/tidy_data_lebron_james.csv
	rm -f results/figs/EDA_SHOT_CLOCK_lebron_james.png results/figs/EDA_SHOT_NUMBER_lebron_james.png results/figs/EDA_SHOT_DIST_lebron_james.png results/figs/EDA_SHOT_RESULT_lebron_james.png results/figs/EDA_TOUCH_TIME__lebron_james.png results/figs/EDA_PERIOD_lebron_james.png results/figs/EDA_PTS_TYPE_lebron_james.png results/figs/EDA_DRIBBLES_lebron_james.png results/figs/EDA_CLOSE_DEF_DIST_lebron_james.png
	rm -f data/accuracies_lebron_james.csv data/features_lebron_james.csv
	rm -f results/figs/train-test-acc_lebron_james.png results/figs/best_features_lebron_james.png results/figs/EDA_DRIBBLES_lebron_james.png results/figs/EDA_SHOT_CLOCK_lebron_james.png results/figs/EDA_SHOT_DIST_lebron_james.png results/figs/train-test-acc_lebron_james.png results/figs/best_features_lebron_james.png
	rm -f docs/Report.md docs/Report.Rmd

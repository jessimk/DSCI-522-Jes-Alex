# Makefile Structure for Decision Tree Analysis of Lebron
all: doc/Report.md

data/tidy_data_lebron_james.csv : data/shot_logs_raw.csv src/01_loading_wrangling.R
	Rscript src/01_loading_wrangling.R "lebron james"	data/shot_logs_raw.csv data/tidy_data_lebron_james.csv

results/figs/EDA_SHOT_CLOCK_lebron_james.png results/figs/EDA_SHOT_NUMBER_lebron_james.png results/figs/EDA_SHOT_DIST_lebron_james.png results/figs/EDA_SHOT_RESULT_lebron_james.png results/figs/EDA_TOUCH_TIME__lebron_james.png results/figs/EDA_PERIOD_lebron_james.png results/figs/EDA_PTS_TYPE_lebron_james.png results/figs/EDA_DRIBBLES_lebron_james.png results/figs/EDA_CLOSE_DEF_DIST_lebron_james.png: data/tidy_data_lebron_james.csv src/02_EDA.py
	Python src/02_EDA.py data/tidy_data_lebron_james.csv results/figs/EDA "lebron james"

data/accuracies_lebron_james.csv data/features_lebron_james.csv: data/tidy_data_lebron_james.csv src/03_machine_learning.py
	Python src/03_machine_learning.py data/tidy_data_lebron_james.csv data/accuracies_lebron_james.csv data/features_lebron_james.csv

results/figs/train-test-acc_lebron_james.png results/figs/best_features_lebron_james.png: data/accuracies_lebron_james.csv data/features_lebron_james.csv src/04_analysis_plots_script.py
	Python src/04_analysis_plots_script.py data/accuracies_lebron_james.csv data/features_lebron_james.csv results/figs/train-test-acc_lebron_james.png results/figs/best_features_lebron_james.png

clean:
	rm -f data/tidy_data_lebron_james.csv
	rm -f results/figs/EDA_SHOT_CLOCK_lebron_james.png results/figs/EDA_SHOT_NUMBER_lebron_james.png results/figs/EDA_SHOT_DIST_lebron_james.png results/figs/EDA_SHOT_RESULT_lebron_james.png results/figs/EDA_TOUCH_TIME__lebron_james.png results/figs/EDA_PERIOD_lebron_james.png results/figs/EDA_PTS_TYPE_lebron_james.png results/figs/EDA_DRIBBLES_lebron_james.png results/figs/EDA_CLOSE_DEF_DIST_lebron_james.png
	rm -f data/accuracies_lebron_james.csv data/features_lebron_james.csv
	rm -f results/figs/train-test-acc_lebron_james.png results/figs/best_features_lebron_james.png
	rm -f doc/Report.md doc/Report.Rmd

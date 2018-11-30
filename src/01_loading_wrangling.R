#! /usr/bin/env Rscript
# 01_loading_wrangling_data.R
# Jes Simkin and Alex Hope Nov, 2018
#
# This script loads the raw shot log data, performs data cleaning and wrangling,
# and outputs a csv file for a specified player into the data folder.
#
# Usage: Rscript src/01_loading_wrangling.R "lebron james" data/shot_logs_raw.csv data/tidy_data_lebron_james.csv

library(tidyverse)

# read in command line arguments
args <- commandArgs(trailingOnly = TRUE)

player <- args[1]
input <- args[2]
output <- args[3]

# define main function
main <- function(){

  # read in data
  data <- read.csv(input)

  #wrangle player specific data, remove errors and rename shot_clock NAs
  tidy_data <- data %>%
      filter(player_name == player,
             TOUCH_TIME >= 0) %>%
      mutate(SHOT_CLOCK = replace_na(SHOT_CLOCK, 0)) %>%
      select(SHOT_CLOCK, SHOT_NUMBER, SHOT_DIST, SHOT_RESULT,
             TOUCH_TIME, PERIOD, PTS_TYPE, DRIBBLES, CLOSE_DEF_DIST)


  write.csv(tidy_data, output)
}

# call main function
main()

Tidying Data LBJ Data
================

Setup
=====

Loading data into R
-------------------

``` r
lbj_data <- read_csv("https://raw.githubusercontent.com/UBC-MDS/DSCI-522-Jes-Alex/master/data/shot_logs_raw.csv?token=Ao9QkTPZ0S2NSZI8bIRGzjLZHbaycrCbks5b93bjwA%3D%3D")
```

    ## Parsed with column specification:
    ## cols(
    ##   .default = col_integer(),
    ##   MATCHUP = col_character(),
    ##   LOCATION = col_character(),
    ##   W = col_character(),
    ##   GAME_CLOCK = col_time(format = ""),
    ##   SHOT_CLOCK = col_double(),
    ##   TOUCH_TIME = col_double(),
    ##   SHOT_DIST = col_double(),
    ##   SHOT_RESULT = col_character(),
    ##   CLOSEST_DEFENDER = col_character(),
    ##   CLOSE_DEF_DIST = col_double(),
    ##   player_name = col_character()
    ## )

    ## See spec(...) for full column specifications.

Filtering raw data for Lebron James's shots and selecting our classifier columns
--------------------------------------------------------------------------------

``` r
lbj_data_clean <- lbj_data %>% 
  filter(player_name == "lebron james") %>% 
  select(GAME_CLOCK, SHOT_CLOCK, SHOT_NUMBER, SHOT_DIST, SHOT_RESULT, TOUCH_TIME, PERIOD, PTS_TYPE, DRIBBLES)

write.csv(lbj_data_clean, "lbj_shots_tidy.csv")

head(lbj_data_clean)
```

    ## # A tibble: 6 x 9
    ##   GAME_CLOCK SHOT_CLOCK SHOT_NUMBER SHOT_DIST SHOT_RESULT TOUCH_TIME PERIOD
    ##   <time>          <dbl>       <int>     <dbl> <chr>            <dbl>  <int>
    ## 1 09:09            13.7           1       7   missed             9.5      1
    ## 2 06:08            15.2           2       5.4 missed             7.9      1
    ## 3 04:38            12.3           3      23.2 made               5.6      1
    ## 4 00:02            NA             4      27.1 missed             2        1
    ## 5 10:17            20.8           5       3.1 made               2.7      2
    ## 6 06:14            16.2           6       5.7 missed             8.3      2
    ## # ... with 2 more variables: PTS_TYPE <int>, DRIBBLES <int>

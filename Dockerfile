# get python package dependencies
FROM continuumio/anaconda3

# install numpy, pandas & matplotlib
RUN conda install numpy==1.15.4 && \
conda install pandas==0.20.3 && \
conda install scikit-learn==0.20.1 && \
conda install matplotlib==3.0.1

# install make
RUN apt-get update && apt-get install make

# install tidyverse from rocker/tidyverse

RUN conda install libiconv

# Install R dependencies
RUN conda install --quiet --yes -c conda-forge r-rmarkdown r-knitr r-tidyverse

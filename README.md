# stage_recombination_AH


These scripts were realized for a 6 months Bioinformatic Master 2 internship by Opale Rambaud under the supervision of Alexandre Hassanin.

The aim of the internship was to visualize the bipartition signal obtained by the BSW program (see Dylkln github) in the form of a barcode and then to search for recombination candidates. 

The github contains 4 scripts : 


LG : Log Generation. This script allows to generate the log files from the csv results of BSW. This files can after be used with the SuperTRI program. The input is a vs file with bipartitions in rows and boostrap signal in columns. The output is log files for every windows with all of bipartition with a signal > 1. 

ISC + BC : Informative Sites Count and Bipartitions Count. This script allows to generate graph of the count of informatives sites per windows and the count of bipartitions per windows. The input is csv files from BSW and a fasta alignement file. The ouput are the two graphes. 

BBC : Bootstrap Barcodes Construction. This script allows to build the barcode representation from csv file. The input is a csv files with the bipartition you want to visualize in barcode. The input is a barcode per biparttion. 

SRC : Search For Recombination Candidates. This script allows to make a recombination candidates search. The inputs are the csv file with the bipartion you want to serch for candidates and the csv files with all bipartion who can be candidates. The output is a text file with the candidates per fragment of signal loss. 


These scripts are in Jupyter Notebook format. 


If you are any questions please send an email to opale.rambaud@gmail.com



![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)

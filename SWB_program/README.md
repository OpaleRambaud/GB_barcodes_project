# SWB program

## Related project : GB_barcodes_project

Copyright (C) 2022 Sorbonne Université / Institut de Systématique, Évolution, Biodiversité (ISYEB) / Hassanin Rambaud

__Authors :__

Alexandre Hassanin
Dylan Klein
Opale Rambaud 



__Contact :__

If you have any questions about this script please send an email at : alexandre.hassanin@mnhn.fr or opale.rambaud@gmail.com

--------------------------------------------------------------------------------------------------------------------------------------------


## Quick description of the program : 

This program aims to give the frequencies of bipartitions calculated by maximum likelihood from a sequence alignment.

 
The ouput of this program is : a csv file with the bootsrap value for each window and for each bipartitions. 


## Prerequisites : 

The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.
Please make sure run this script with the Phylo environment using for all programs of the GB_barcodes_project.


/!\ Important note : please activate the environment (with conda activate) only by being in the program directory, not before.



## Using the program

To use the program, you must be in the "SWB_program/program" directory and run the following command:

```
python SWB_program.py -f <FASTA_FILE> -n <NREP> -ws <WINDOW_SIZE> -s <STEP> -t <THREADS>
```

With the following arguments:


- *FASTA_FILE* : The file in fasta format containing the sequence alignments.

OPTIONAL ARGUMENTS :


- *NREP*: Number of bootstrap replication arrays that will be generated (default 100). 
- *WINDOW_SIZE*: The desired window size (default 1000). 
- *STEP*:  The desired window pitch (default 100).
- *THREADS*: The number of Hearts the program can use (default 1).

##### Example of use


```
python SWB_program.py -f Sarbecovirus_75G_220721.fasta -n 100 -ws 2000 -s 50 -t 1
```

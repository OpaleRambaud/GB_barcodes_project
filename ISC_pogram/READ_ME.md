# ISC program 

## Related project : GB_barcodes_project

Copyright (C) 2022 Sorbonne Université / Institut de Systématique, Évolution, Biodiversité (ISYEB) / Hassanin Rambaud


__Authors :__

Alexandre Hassanin
Opale Rambaud 



__Contact :__

If you have any questions about this script please send an email at : alexandre.hassanin@mnhn.fr or opale.rambaud@gmail.com

--------------------------------------------------------------------------------------------------------------------------------------------


## Quick description of the program : 

This program calculates the number of informative sites (sites with a different nucleotides) for each analysis window

The ouput of this program is a csv file with the number of informatives sites

## Language :

This script is in Python 3.7.3

## Prerequisites : 

The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.
Please make sure run this script with the Phylo environment using for all programs of the GB_barcodes_project.


## Using the program : 

To use the program, you must be in the "ISC_program" directory and run the following command :

```
python ISC_program.py -f <FASTA_FILE> -ws <WINDOW_SIZE> -s <STEP> -al <ALIGNMENT LENGHT> 
```

With the following arguments:

MANDATORY :

- *FASAT_FILE* : The fasta file of the alignment
- *WINDOW_SIZE*: The size of the window used in the SWB program.
- *STEP*: The step used in the SWB program.
- *ALIGNMENT LENGHT* : The lenght of the alignement used in SWB. 




##### Example of use : 

```
python ISC_program.py -r S.csv -ws 2000 -s 50 -al 27195
# SWD program 

## Related project : GB_barcodes_project

Copyright (C) 2022 Sorbonne Université / Institut de Systématique, Évolution, Biodiversité (ISYEB) / Hassanin Rambaud


__Authors :__

Alexandre Hassanin
Opale Rambaud 



__Contact :__

If you have any questions about this script please send an email at : alexandre.hassanin@mnhn.fr or opale.rambaud@gmail.com

--------------------------------------------------------------------------------------------------------------------------------------------


## Quick description of the program : 

This program calculates the distance (in % differences) between two selected sequences in the alignment file per analysis window.

The ouput of this program is a csv file with the % of difference per windows between 2 selected sequences. 

## Language :

This script is in Python 3.7.3

## Prerequisites : 

The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.
Please make sure run this script with the Phylo environment using for all programs of the GB_barcodes_project.


## Using the program : 

To use the program, you must be in the "SWD_program" directory and run the following command :

```
python SWD_program.py -f <FASTA_FILE> -ws <WINDOW_SIZE> -s <STEP> -al <ALIGNMENT LENGHT> -g <GAP>
```

With the following arguments:

MANDATORY :

- *FASTA_FILE* : The file in .fasta format containing the alignement used in the SWB program. 
- *WINDOW_SIZE*: The size of the window used in the SWB program.
- *STEP*: The step used in the SWB program.
- *ALIGNMENT LENGHT* : The lenght of the alignement used in SWB. 

OPTIONNALS :

- *GAP* : The way you want to treat the gap : 0 = not considered as a difference , 1 = considered as a difference , 2 = ignored. Default = 1


##### Example of use : 

```
python SWD_program.py -f Sarbecovirus_75G_220721.fasta -ws 2000 -s 50 -al 30100 -g 1 
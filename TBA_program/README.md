# TBA program

## Related project : GB_barcodes_project

Copyright (C) 2022 Sorbonne Université / Institut de Systématique, Évolution, Biodiversité (ISYEB) / Hassanin Rambaud


__Authors :__

Alexandre Hassanin
Opale Rambaud 



__Contact :__

If you have any questions about this script please send an email at : alexandre.hassanin@mnhn.fr or opale.rambaud@gmail.com

--------------------------------------------------------------------------------------------------------------------------------------------


## Quick description of the program : 

This program allows to find, for each node of a reference tree, 
the bipartitions coming from the SWB and BBC programs which question this node (alternatives). 

The output of this program is a .csv file which contains for each node of the reference tree its alternatives and the fragments for which we obtain a 
signal inside these alternative bipartitions. 

## Language :

This script is in Python 3.7.3

## Prerequisites : 

The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.
Please make sure run this script with the Phylo environment using for all programs of the GB_barcodes_project.


## Using the program : 

To use the program, you must be in the "TBA_program" directory and run the following command :

```
python TBA_program.py -n <TRE_FILE> -r <BBC_RESULTS_FILE> -ws <WINDOW_SIZE> -s <STEP> -gl <GENOME_ALIGNMENT_LENGTH>
```

With the following arguments:


- *TRE_FILE* : The file in .TRE format containing the reference parenthesis tree.
- *BBC_RESULTS_FILE* : The file in .csv format containing the filtered and ordered bipartions obtained from the BBC program. 
(The name of the results file is : "name_of_the_alignment_output_bp_sup_70").
- *WINDOW_SIZE*: The size of the window used in the SWB program.
- *STEP*: The step used in the SWB program.
- *GENOME_ALIGNMENT_LENGTH*: The length in nucleotides of the alignement used in the SWB program.


##### Example of use : 

```
python TBA_program.py -n Sarbecovirus_75G_220721.tre -r Sarbecovirus_75G_220721_output_bp_sup_70.csv -ws 2000 -s 50 -gl 29677
```


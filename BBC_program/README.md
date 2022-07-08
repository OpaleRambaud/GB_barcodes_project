# BBC program 

## Related project : GB_barcodes_project

Copyright (C) 2022 Alexandre Hassanin MNHN


__Authors :__

Opale Rambaud (under the direction of  : Alexandre Hassanin)


__Contact :__

If you have any questions about this script please send an email at : alexandre.hassanin@mnhn.fr

--------------------------------------------------------------------------------------------------------------------------------------------


## Quick description of the program : 

This program sorts the result file of the SWB program by selecting only the bipartitions with at least one bootstrap superior to 70. It then orders these bipartitions by 
decreasing bootstrap mean. Then it builds a barcode for each bipartition. A barcode is a visual representation of the phylogenetic signal along the alignment. The red parts 
represent the areas for which the signal is lower than 50 and the green parts represent the areas for which the signal is higher than 70. The grey areas represent the areas 
where the signal is between 50 and 70. 

The outputs of this program are : a .csv file containing the sorted and filtered bipartitions and a barcode for each bipartition in this file.  

## Language :

This script is in Python 3.7.3

## Prerequisites : 

The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.
Please make sure run this script with the Phylo environment using for all programs of the GB_barcodes_project.


## Using the program : 

To use the program, you must be in the "barcodes_program" directory and run the following command :

```
python BBC_program.py -n <FASTA_FILE> -r <SWB_FILE> -ws <WINDOW_SIZE> -s <STEP> 
```

With the following arguments:


- *FASTA_FILE* : The file in .fasta format containing the alignement used in the SWB program.
- *SWB_FILE* : The file in .csv format containing the results of the SWB program. 
(The name of the results file is : "name_of_the_alignment_SWB_ws_s.csv").
- *WINDOW_SIZE*: The size of the window used in the SWB program.
- *STEP*: The step used in the SWB program.


##### Example of use : 

```
python BBC_program.py -f Rhinacovirus.fasta -r alpha_Rhinacovirus_SWB_ws2000_s50.csv -ws 2000 -s 50 
```


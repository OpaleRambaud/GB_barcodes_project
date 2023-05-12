# SNC program 

## Related project : GB_barcodes_project

Copyright (C) 2022 Sorbonne Université / Institut de Systématique, Évolution, Biodiversité (ISYEB) / Hassanin Rambaud


__Authors :__

Alexandre Hassanin
Opale Rambaud 



__Contact :__

If you have any questions about this script please send an email at : alexandre.hassanin@mnhn.fr or opale.rambaud@gmail.com
-------------------------------------------------------------------------------------------------------------------------------------------------------------


## Quick description of the program : 

The purpose of this program is to calculate the base composition for each window of the SWB analysis. 

Thus, you will be able to visualize the evolution of the base composition along your alignment.

The ouput of this program is : a csv file with the base composition of each analysis windows  

## Language :

This script is in Python 3.7.3

## Prerequisites

The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.
Please make sure run this script with the Phylo environment using for all programs of the GB_barcodes_project.
You must have the biopython package installed on your computer. 

/!\ Important note : 

You have to create a corresponding fasta file for your alignment. 
This file should contain a representation of the alignment with the non-coding parts represented by dashes (-) 
and the coding parts represented by the codon positions (123). Please refer to the example file 
named "corresponding_example.fasta" in the folder. 


## Using the program

To use the program, you must be in the "SNC_program" directory and run the following command :

```
python SNC_program.py -f <FASTA_FILE> -c <CORRESPONDING_FILE> -ws <WINDOW_SIZE> -s <STEP> 
```

With the following arguments:


- *FASTA_FILE* : The file in fasta format containing the sequence alignments.
- *CORRESPONDING_FILE* : The file in fasta format containing the corresponding.
- *WINDOW_SIZE*: The size of the window previously used in the SWB program . 
- *STEP*:  The step previously used in the SWB program.


##### Example of use


```
python SNC_program.py -f Sarbecovirus_75G_220721.fasta -c corresponding_example.fasta -ws 2000 -s 50
```
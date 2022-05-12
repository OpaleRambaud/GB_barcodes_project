# Nucleotide bases composition

__Author :__

Opale Rambaud

-------------------------------------------------------------------------------------------------------------------------------------------------------------

The purpose of this program is to calculate the base composition for each window of the BSW analysis. 

Thus, you will be able to visualize the evolution of the base composition along your alignment.

## Prerequisites

The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.
You must have the biopython package installed on your computer. 

/!\ Important note : 

You have to create a corresponding fasta file for your alignment. 
This file should contain a representation of the alignment with the non-coding parts represented by dashes (-) 
and the coding parts represented by the codon positions (123). Please refer to the example file 
named "corresponding_example.fasta" in the folder. 


## Using the program

To use the program run the following command:

```
python compo_bases.py -f <FASTA_FILE> -ws <WINDOW_SIZE> -s <STEP> 
```

With the following arguments:


- *FASTA_FILE* : The file in fasta format containing the sequence alignments.
- *CORRESPONDING_FILE* : The file in fasta format containing the corresponding.
- *WINDOW_SIZE*: The size of the window previously used in the BSW program . 
- *STEP*:  The step previously used in the BSW program.


##### Example of use


```
python compo_bases -f alignment.fasta -c corresponding_example.fasta -ws 2000 -s 50
```
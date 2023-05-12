# GB_barcodes_project

Copyright (C) 2022 Sorbonne Université / Institut de Systématique, Évolution, Biodiversité (ISYEB) / Hassanin Rambaud


__Authors :__

Alexandre Hassanin
Dylan Klein
Opale Rambaud 



__Contact :__

If you have any questions about this script please send an email at : alexandre.hassanin@mnhn.fr or opale.rambaud@gmail.com

--------------------------------------------------------------------------------------------------------------------------------------------


# Quick presentation of the project :


This repository is reffered to the following article : Genomic Bootstrap Barcodes and Their Application to Study the Evolution of Sarbecoviruses. 
Viruses, 14(2), 440 by Hassanin, A., Rambaud, O., & Klein, D. de l'ISYEB (2022). doi.org/10.3390/v14020440. 
Please read it to know the context, purpose and methods of the project. [Click here to read the article](https://www.mdpi.com/1999-4915/14/2/440).


Recombination creates mosaic genomes containing regions with mixed ancestry, and the
accumulation of such events over time can complicate greatly many aspects of evolutionary inference.

Here, we developed a method (the GB_barcodes_project) to help understand recombination events and thus provide a better understanding of the evolutionary history of genomes.

# Presentation of the programs :

The project contains several programs corresponding to different analysis steps. You will find each of the scripts allowing to use the programs in the corresponding directories. 
Each program is accompanied by a read_me to facilitate its use. Please read them carefully before starting to use a program. 


- SWB_program : Slidding Windows Bootstrap. The SWB program was designed to conduct bootstrap analyses on N subdatasets extracted from a multiple genome alignment (input file in Fasta format) using a
window of W nucleotides moving in steps of S nucleotides along the alignment.

## SWB_program related programs : 

	- Input : alignment of sequences (.fasta) 
	- Ouput : csv file with bootstrap value per analysis windows 

- BBC_program : Bootstrap Barcodes Construction. This script allows to generate genomic bootstrap (GB)
barcodes to highlight the regions supporting phylogenetic relationships. A GB barcode can be viewed as a simplified representation of the SWB results. 

	- Input : SWB output
	- Ouput : filtered and ordoned SWB output + GB barcodes for each bipartition

- LFG_program : Log Files Generation. This script allows to generate the log files from the csv results of SWB. This files can after be used with the SuperTRI program.

	- Input : SWB ouput 
	- Ouput : log file for each analysis windows 

- TBA_program : Tree Barcodes and their Alternatives. This program allows to find, for each node of a reference tree, the bipartitions coming from the SWB and BBC programs which question this node (alternatives).

	- Input : SWB ouput + newick tree
	- Ouput : csv file containing the alternatives 
	
	
- SNC_program : Synonymous Nucleotide Composition. The purpose of this program is to calculate the base composition for each window of the SWB analysis.

	- Input : fasta alignment
	- Ouput : csv file with base composition for each analysis window
	
- SWD_program : Sliding Windows Distance Analysis. This program allows to calculate the distances (in % of difference) for each analysis windows.

	- Input : fasta alignment
	- Ouput : csv file with distance for each analysis window
	
- BPC_program : Bipartitions Count. This program allows to count the number of bipartition with a boostrap superior to 0 for each analysis window.

	- Input : SWB output
	- Ouptput : csv file with number of bipartition per windows
	
- ISC_program : Inofmatives Sites Count. This program allows to count number of sites with different nucleotides for each analysis window.

	- Input : fasta alignment
	- Output : csv file with number of informative sites for each window
	
## Other programs : 
	
- CGB_program : Colored Barcodes. This program allows to create barcodes of selectionned bipartition with the color you want.

	- Input : csv file with bipartitions and the areas you want to color 
	- Ouput : colored barcodes for each bipartition


- SuperTri program : This program will help you producing a matrix representation weighted by bootstrap proportions or Bayesian posterior probabilities.
Reference : SuperTRI: A new approach based on branch support analyses of multiple independent data sets for assessing reliability of phylogenetic inferences 
by Anne Ropiquet, Blaise Li, Alexandre Hassanin. (2009).


## *Information about use :*

## Prerequisites : 

The scripts are all written in Python 3.7.3 except for the scripts of the Supertri program which are in Python 2.7
They are usable via a command interpreter, as well on a Windows, MacOs or Linux machine.
The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.

## Environment : 

All programs must be run in the Phylo environment, except for the Supertri program which must be run in its own environment
(please visit the Supertri directory for more information).

First create the environment :

 If you run this program on Linux computer or a PC use this command :

```
conda env create --file environment.yml
```
  If you run this program on MacOS use this command :

```
conda env create --file environment-macos.yml
```

Then activate the conda environment :

```
conda activate Phylo
```


## Example of use :

If you want to try the project please use the example data set. These data were published in the following article :
The command lines used in the example correspond to this data set.
Its an alignment of 75 taxons.
The computation time of this example is approximately 2 days.

## Limits of the method :


The computation time of the SWB program is one of the limits of the method. 
Depending on the number of taxa used, the calculation times vary. 

Here are some examples of calculation times given as information:

- 15 taxons : approximately 5 hours
- 52 taxons : approximately 2 days
- 64 taxons : approximately 3 days
- 150 taxons : approximately 7 days

The other limitation of the method is the size of the gaps in the genome alignment. 
The size of the gaps must not exceed the size of the analysis window (ws parameter). 











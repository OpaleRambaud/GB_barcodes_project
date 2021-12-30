# Recombination detection program

This program aims to give the frequencies of bipartitions calculated by maximum likelihood from a sequence alignment.

## Prerequisites

The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.
It is imperative to have [RAxML](https://cme.h-its.org/exelixis/web/software/raxml/) installed on your machine. You can do this *via* conda with the following command: 
```
conda install -c bioconda raxml
```

## Download the programme

1. Cloning the github directory

> HTTPS link

```
git clone https://github.com/Dylkln/Phylo_AH.git
```

> SSH link

```
git clone git@github.com:Dylkln/Phylo_AH.git
```

2. Initialise the conda environment from the *environment.yml* file

```
conda env create --file environment.yml
```

3. Activate the conda environment

```
conda activate phylo
```

## Using the program

To use the program, you must be in the "program" directory and run the following command:

```
python phylo.py -f <FASTA_FILE> -n <NREP> -ws <WINDOW_SIZE> -s <STEP> -t <THREADS>
```

With the following arguments:

**MANDATORY**
- *FASTA_FILE* : The file in fasta format containing the sequence alignments.

**OPTIONAL**
- *NREP*: Number of bootstrap replication arrays that will be generated (default 100). 
- *WINDOW_SIZE*: The desired window size (default 1000). 
- *STEP*:  The desired window pitch (default 100).
- *THREADS*: The number of Hearts the program can use (default 1).

##### Example of use


```
python phylo.py -f ../data/exemple.fasta -n 10 -ws 1000 -s 100 -t 1
```

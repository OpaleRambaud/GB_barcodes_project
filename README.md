# Programme de détection des recombinaisons

Ce programme a pour but de donner les fréquences de bipartitions calculées par maximum de vraisemblance à partir d'un alignement de séquence.

## Prérequis

L'utilisation de [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) est fortement recommandée.
Il est impératif d'avoir [RAxML](https://cme.h-its.org/exelixis/web/software/raxml/) installé sur votre machine. Vous pouvez le faire *via* conda par la commande suivante : 
```
conda install -c bioconda raxml
```

## Télécharger le programme

1. Clonage du répertoire github

> Lien HTTPS

```
git clone https://github.com/Dylkln/Phylo_AH.git
```

> Lien SSH

```
git clone git@github.com:Dylkln/Phylo_AH.git
```

2. Initialiser l'environnement conda à partir du fichier *environment.yml*

```
conda env create --file environment.yml
```

3. Activer l'environnement conda

```
conda activate phylo
```

## Utilisation du programme

Pour utiliser le programme, vous devez être dans le répertoire "program" et lancer la commande suivante :

```
python phylo.py -f <FASTA_FILE> -n <NREP> -ws <WINDOW_SIZE> -s <STEP> -t <THREADS>
```

Avec les arguments suivants:

**OBLIGATOIRES**
- *FASTA_FILE* : Le fichier au format fasta contenant les alignements de séquences.

**OPTIONNELS**
- *NREP* : Nombre de matrice de réplication de bootstrap qui seront générées (par défaut 100). 
- *WINDOW_SIZE* : La taille de fenêtre désirée (par déaut 1000). 
- *STEP* :  Le pas de la fenêtre désirée (par défaut 100).
- *THREADS* : Le nombre de Coeurs que le programme peut utiliser (par défaut 1).

##### Exemple d'utilisation

```
python phylo.py -f ../data/exemple.fasta -n 10 -ws 1000 -s 100 -t 1
```

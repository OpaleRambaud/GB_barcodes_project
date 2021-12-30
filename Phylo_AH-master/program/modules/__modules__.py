"""
This module file contains all functions needed by the main program.
"""

########################## MODULE TO IMPORT #######################################

from Bio import Phylo
from Bio import AlignIO, SeqIO
from Bio.Phylo.Consensus import _BitString
import dendropy
from dendropy.interop import raxml
import pandas as pd

###################################################################################


def read_fasta(fasta_file):
    """
    read a fasta file and retrieve its sequences
    """

    sequences = AlignIO.read(fasta_file, "fasta")

    return sequences


def likelihood_tree(fasta_file, rx_runner):
    """
    create a maximum likelihood tree using a nexus file, and the raxml runner
    """

    data = dendropy.DnaCharacterMatrix.get(
        path = fasta_file,
        schema = "fasta")
    tree = rx_runner.estimate_tree(data)

    return tree


def sliding_window(sequence, window_size, step):
    """
    create a sliding window with a size and step defined at program startup
    """

    if step <= 0:
        raise Exception("** ERROR ** : step must be a positive value")
    if step > window_size:
        raise Exception("** ERROR ** : step must not be larger than window_size")
    if window_size > len(sequence):
        raise Exception("** ERROR ** : window_size must not be larger than sequence length")

    i = 0
    while i + window_size < len(sequence):
        yield sequence[i:i + window_size]
        i += step


def get_sequences_from_windows(sequences, window_size, step):
    """
    retrieve a dictionnary containing the index of the windows as a key and
    a list of windows associated with this index as a value
    """

    seq_dict = {}
    for seq in sequences:
        for index, win in enumerate(sliding_window(seq, window_size, step)):
            tmp = index + 1
            if tmp not in seq_dict.keys():
                seq_dict[tmp] = []
            seq_dict[tmp].append(win)

    return seq_dict


def save_alignments_to_fasta(alignments, output_file):
    """
    save a multiple sequence alignment in a fasta file
    """

    return SeqIO.write(alignments, output_file, "fasta")


def get_bitstrings(tree):
    """
    get bitstrings of a tree
    """

    bitstrs = []
    term_names = [term.name for term in tree.get_terminals()]
    term_names.sort()

    for clade in tree.get_nonterminals():
        clade_term_names = [term.name for term in clade.get_terminals()]
        boolvals = [name in clade_term_names for name in term_names]
        bitstr = _BitString("".join(map(str, map(int, boolvals))))
        strs = ""
        for bit in bitstr:
            if bit == "1":
                strs += "*"
            else:
                strs += "-"
        bitstrs.append(strs)

    return bitstrs


def save_taxa_names(taxa_names, taxa_file):
    """
    Save taxa names in a text file
    """

    with open(f"../results/{taxa_file}", "w") as filout:
        for index, taxa in enumerate(taxa_names):
            filout.write(f"{index + 1} --> {taxa}\n")



def main():
    sys.exit() # aucune action souhaitée.
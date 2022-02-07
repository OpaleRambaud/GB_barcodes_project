#!/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Alexandre Hassanin MNHN
__author__ = "Dylan KLEIN"


"""
This program is used to get frequencies of bipartition.
These frequencies are calculated on trees created with the bootstrap method
using RAxML using evolution model (Maximum Likelihood)

USAGE : {MANDATORY} -f [FASTA_FILE]
        {OPTIONAL} -n [NREP] -ws [WINDOW-SIZE] -s [STEP] -t [THREADS]
"""

# ====================================== MODULES TO IMPORT ====================================== #

from modules.__modules__ import *
import argparse
import os
import subprocess
from subprocess import DEVNULL


# =============================================================================================== #


def isfile(path):
    """
    Check if path is an existing file
    """

    if not os.path.isfile(path):

        if os.path.isdir(path):
            err = f"{path} is a directory"
        else:
            err = f"{path} does not exist"

        raise argparse.ArgumentTypeError(err)

    return path


def arguments():
    """
    set arguments
    """

    parser = argparse.ArgumentParser()

    # Mandatory arguments
    parser.add_argument("-f", "--fasta_file", dest="fasta_file",
                        type=isfile, required=True,
                        help="fasta_file is a .fasta file containing the alignment")

    # Optional arguments
    parser.add_argument("-n", "--nreps", dest="nreps",
                        type=int, default=100,
                        help="number of bootstrap replicate matrices that will be generated")
    parser.add_argument("-ws", "--window_size", dest="window_size",
                        type=int, default=1000,
                        help="define the size of the window used in the analysis")
    parser.add_argument("-s", "--step", dest="step",
                        type=int, default=100,
                        help="define the step of the window used in the analysis")
    parser.add_argument("-t", "--threads", dest="threads",
                        type=int, default=2,
                        help="define the number of threads you want to use for the analysis")

    return parser.parse_args()


def main():
    """
    Main program function
    """

    # Initialisation
    rx_runner = raxml.RaxmlRunner()

    # Get args
    args = arguments()

    # Get sequences
    sequences = read_fasta(args.fasta_file)

    # Create Likelihood tree
    tree = likelihood_tree(args.fasta_file, rx_runner)
    tree.write(path="../ref_tree/ref_tree.tre", schema="newick")
    print(tree.as_ascii_plot())

    taxa_file = "taxa_names.txt"
    term_names = list(tree.taxon_namespace)
    term_names.sort()
    save_taxa_names(term_names, taxa_file)

    # Get every windows in a dict
    seq_dict = get_sequences_from_windows(sequences, args.window_size, args.step)

    # Create a tmp file name, a RAxML command line and a new dict
    # to store all bitstrings from bootstrap trees built by RAxML

    tmp = "tempfile.fa"
    command_raxml = ["raxmlHPC", "-T", f"{args.threads}", "'f a", "-m", "GTRGAMMA", "-p",
                     "12345", "-x", "12345", "-#", f"{args.nreps}", "-s", f"{tmp}", "-n", "trees"]

    bitstrings_dict = {}.fromkeys(set(seq_dict.keys()), [])

    print(f"YOUR NUMBER OF REPETITIONS IS SET TO {args.nreps}")
    print("*** RAxML IS RUNNING : PLEASE WAIT ***\n")

    files_to_rm = ["RAxML_bootstrap.trees", "RAxML_info.trees",
                   "tempfile.fa", "tempfile.fa.reduced"]
    # Launch RAxML with the command line and save all bootstrap trees
    for index, seq in seq_dict.items():
        save_alignments_to_fasta(seq, tmp)
        subprocess.call(command_raxml, stdout=DEVNULL)

        print(f"RUN NUMBER {index} OUT OF {len(seq_dict)}\n")

        bits_list = [
            get_bitstrings(tree)
            for tree in Phylo.parse("RAxML_bootstrap.trees", "newick")
        ]

        bitstrings_dict[index] = bits_list

        for file in files_to_rm:
            if os.path.exists(file):
                os.remove(file)

    # Create a nested dictionnary to store the bipartition frequencies
    frq_bip = {}.fromkeys(set(bitstrings_dict.keys()), {})

    # Fill the dictionnary with bipartitions frequencies
    for index, liste_bits in bitstrings_dict.items():
        tmp = {}
        for liste in liste_bits:
            for bitstrs in liste:
                if bitstrs not in tmp.keys():
                    tmp[bitstrs] = 0
                tmp[bitstrs] += 1
        tmp = dict(sorted(tmp.items(), key=lambda x: x[1], reverse=True))
        frq_bip[index] = tmp

    # Convert the dictionnary in Pandas Dataframe
    df_freq = pd.DataFrame.from_dict(frq_bip)
    df_freq.fillna(value=0, inplace=True)

    # Save the Pandas Dataframe
    csv_file = f"frq_bip_{args.window_size}_win_{args.step}_step_{args.nreps}_bt.csv"

    df_freq.to_csv(f"../results/{csv_file}")


if __name__ == '__main__':
    main()

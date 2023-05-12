#!/bin/env python3
# -*- coding: utf-8 -*-
# This program is free software: you can redistribute it and/or modify it under the terms of the 
# GNU General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# A copy of the GNU General Public License is available at http://www.gnu.org/licenses/gpl-3.0.html

__author__ = "Dylan KLEIN"
__contact__ = "klein.dylan@outlook.com"
__version__ = "1.0.0"
__license__ = "GPL"

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
import time
import string
import sys
import csv 
import pandas as pd
from Bio import SeqIO


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

def alphabetic_fasta (fasta_file) :  

    """
    This function allows you to edit the input fasta file in order to order 
    it alphabetically by adding a two letter code in front of the taxon names.
    
    Input : original fasta file with sequences.
    Ouput : corrected fasta file with alphabetic order.
    """
  
    original_file = str(fasta_file)
    corrected_file = "alpha_" + original_file 
    #corrected_file = original_file 

    with open(original_file) as original, open(corrected_file, 'w') as corrected:
        records = SeqIO.parse(original_file, 'fasta')
        first_letter = 0
        second_letter = 0
        for record in records: 
            name=record.id
            if record.id == name:
                code_first = string.ascii_uppercase[first_letter]
                code_second = string.ascii_uppercase[second_letter]
                record.id = code_first + code_second + "_" + name
                record.description = code_first + code_second + "_" + name
            SeqIO.write(record, corrected, 'fasta')
            corrected.write('\n')
            second_letter += 1
            if code_second == "Z" :
                second_letter = 0
                first_letter += 1
                
                
    os.remove(original_file)
    os.rename(corrected_file, original_file)

def main():
    """
    Main program function
    """
    start_time = time.time()
    print("Please wait")
    
    

    
    # Initialisation
    rx_runner = raxml.RaxmlRunner()

    # Get args
    args = arguments()
    
    # Alphabetic 
    alphabetic_fasta(args.fasta_file)
    
    name_base = os.path.basename(args.fasta_file)
    name_base = name_base.split(".")
    name_base = name_base[0]

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
    win_size = args.window_size
    sstepp = args.step
    csv_file = name_base + "_SWB_ws" + str(win_size) +  "_s" + str(sstepp) + ".csv"

    df_freq.to_csv(f"../results/{csv_file}")
    
    end = time.time()
    
    time_in_sec = end - start_time
    time_in_min = time_in_sec / 60
    
    print("Analysis done ! Run time (in minutes) :")
    print(time_in_min)


if __name__ == '__main__':
    main()

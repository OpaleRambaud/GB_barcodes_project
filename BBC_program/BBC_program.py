#!/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Alexandre Hassanin MNHN
__author__ = "Opale RAMBAUD"

"""
This program allows to build the barcodes from the results file of the SWB program.

"""

########################################## MODULES IMPORT #####################################
import module_build_barcode as bc
import module_set_data as set_dat
import pandas as pd
import argparse
import sys
import os
###############################################################################################



def arguments():


    parser = argparse.ArgumentParser()

    # Mandatory arguments
    parser.add_argument("-f", "--fasta_file", dest="fasta_file",
                        type=str, required=True,
                        help="fasta_file is a .fasta file containing the alignment")
                        
    parser.add_argument("-r", "--results_file", dest="results_file",
                        type=str, required=True,
                        help="results_file is .csv file with the results of SWB program")                        

    parser.add_argument("-ws", "--window_size", dest="window_size",
                        type=int, required=True,
                        help="define the size of the window used in the analysis")
                        
    parser.add_argument("-s", "--step", dest="step",
                        type=int, required=True,
                        help="define the step of the window used in the analysis")


    return parser.parse_args()
    


def main():

    args = arguments()
    
    ##### SETTINGS OF THE DATA #####
    name_base = os.path.basename(args.fasta_file)
    name_base = name_base.split(".")
    name_base= name_base[0]
    print("Preparation of your data for the building of the barcodes")
    
    print("étape fasta")
    gen_len = set_dat.get_genome_len (args.fasta_file)
    
    print("étape filtrage")   
    filtered = set_dat.filtering_sup(args.results_file, 70)  ######## voir dans le code de dylan comment recup le nom du fichier output 
    sorted = set_dat.sorted_by_bt (filtered) 
    
    print("étape noms")
    name_list = set_dat.export_gen_name(args.fasta_file)
    dic_name = set_dat.name_list_to_dico (name_list)

    name_file = set_dat.translate_stars_to_named (sorted,dic_name)
    named_file = set_dat.unnamed_to_named(sorted, name_file,name_base )

    
    
    
    ##### BUILDING BARCODES ####
    
    print("Barcodes building") 
    print("Settings ...")
    data_sorted = pd.read_csv(named_file)
    nb_col = bc.number_of_columns(data_sorted)
    nb_of_row = bc.number_of_row(data_sorted) 
    dic_name2 = bc.put_name_in_dict (data_sorted)
    l_row_csv = bc.bootstrap_per_windows (args.window_size,args.step,nb_col,data_sorted, nb_of_row, gen_len) 
    #color = bc.set_color_for_barcodes()
    bc.barcodes_plot (data_sorted, dic_name2,l_row_csv, nb_of_row) 
    print("End of the analyse. Your barcodes are all done ! You can see them in the current field.") 

if __name__ == '__main__':
    main()
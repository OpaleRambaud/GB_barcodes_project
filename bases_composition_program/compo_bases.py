####################### IMPORT ##########################



import csv
import pandas as pd

import sys
import os
import argparse
from Bio import SeqIO


###################### FUNCTIONS ###############################


def arguments():
    """
    set arguments
    """

    parser = argparse.ArgumentParser()

    # Mandatory arguments
    parser.add_argument("-f", "--fasta_file", dest="fasta_file",
                        type=str, required=True,
                        help="fasta_file is a .fasta file containing the alignment")
                        
    parser.add_argument("-c", "--corresponding_file", dest="fasta_file_corr",
                        type=str, required=True,
                        help="fasta_file is a .fasta file containing the corresponding position")
                        
    parser.add_argument("-ws", "--window_size", dest="win_size",
                        type=int, required=True,
                        help="size of the window used for the bsw program")

    parser.add_argument("-s", "--step", dest="step",
                        type=int, required=True,
                        help="step used for the bsw program")
    return parser.parse_args()                            


def get_coding_corresponding (fasta_file_corr) :


    list_corr = []

    for seq in SeqIO.parse(fasta_file_corr, "fasta"): # TO DO : inter the name of your fasta file

        for index, nt in enumerate(seq) :
            list_corr.append(nt)

    return(list_corr)

def get_genome_len (fasta_file) :

    original_file = str(fasta_file)
    with open(original_file) as original :
        records = SeqIO.parse(original_file, 'fasta')
        for record in records:
            sequ = record.seq
            genome_len = len(sequ)
            break
        
    return genome_len
    
    
    
def get_col (genome_len , step, win_size ) :

    first = 1
    window = []
    for nucl in range(1, genome_len+1 , step) :
       
        if nucl + win_size > genome_len :
            
            break
        window.append(nucl)
    return(len(window))

def get_windows (window_size,step,nb_col,genome_len) :


    """
    This function allows to get the equivalent of the windows in nucleotides position
    (with the median postion)
    
    Input : windows size , step, number of columns, number of rows, genome lenght
    Ouput : a list of corresponding between windows and position 
    """
    win_nucl =[]
    i_deb = 1
    i_fin = window_size 
    stepp = step  
    i_milieu = ((i_deb+i_fin)-1)/2
    i_pas = i_milieu + stepp
    for i in range(1,(nb_col+1)):
        #print(i)
        if i == 1 : 
            win_nucl.append((i_deb,i_pas))
            i_milieu = i_milieu + stepp
            i_deb = i_deb + stepp
            i_fin = i_fin + stepp
            i_pas = i_pas + stepp
        if i == (nb_col-1) :
            win_nucl.append((i_milieu+1 ,i_fin))
            i_milieu = i_milieu + stepp
            i_deb = i_deb + stepp
            i_fin = i_fin + stepp
            i_pas = i_pas + stepp
            break
            
            
        else : 
            win_nucl.append((i_milieu+1 ,i_pas))
            i_milieu = i_milieu + stepp
            i_deb = i_deb + stepp
            i_fin = i_fin + stepp
            i_pas = i_pas + stepp
            
    return(win_nucl)

def get_real_windows (window_size,step,nb_col,genome_len) :

    """
    This function allows to get the equivalent of the windows in nucleotides position
    (with the real postion)
    
    Input : windows size , step, number of columns, number of rows, genome lenght
    Ouput : a list of corresponding between windows and position 
    """

    win_nucl_real =[]
    i_deb = 1
    i_fin = window_size 
    stepp = step  
    i_milieu = ((i_deb+i_fin)-1)/2
    i_pas = i_milieu + stepp
    for i in range(1,(nb_col+1)):
        #print(i)
        if i == 1 : 
            win_nucl_real.append((i_deb,i_fin))
            i_milieu = i_milieu + stepp
            i_deb = i_deb + stepp
            i_fin = i_fin + stepp
            i_pas = i_pas + stepp
        if i == (nb_col-1) :
            win_nucl_real.append((i_deb ,i_fin))
            i_milieu = i_milieu + stepp
            i_deb = i_deb + stepp
            i_fin = i_fin + stepp
            i_pas = i_pas + stepp
            break
            
            
        else : 
            win_nucl_real.append((i_deb ,i_fin))
            i_milieu = i_milieu + stepp
            i_deb = i_deb + stepp
            i_fin = i_fin + stepp
            i_pas = i_pas + stepp
            
    return(win_nucl_real)
            

def get_seq (fasta_file) :

    """
    This function allows to get all seuqences from a multi fasta file
    
    Input : fasta file with multi sequences
    Ouput : a list of the sequences 
    """

    all_seq = []

    for seq in SeqIO.parse(fasta_file, "fasta"): # TO DO : inter the name of your fasta file

        my_seq = []
        for index, nt in enumerate(seq) :
            my_seq.append(nt)
        all_seq.append(my_seq)
    return(all_seq)

def get_base_per_window (base_princ, base_2, base_3, base_4, win_nucl, win_nucl_real, all_seq , num_seq, list_corr) :	
	

    l_nucl_base = {}
    l_nucl_base["nucleotide"] = base_princ

    for window in range(len(win_nucl_real)) :

       
        list_tmp = []
        cmpt_base_princ = 0
        cmpt_tot = 0


        for pos in range(int(win_nucl_real[window][0]), int(win_nucl_real[window][1])+1 ):

            pos2 = pos -1
        
            if list_corr[pos2] == "3" :

                list_tmp.append(all_seq[num_seq][pos2])


        
        for ind, nucl in enumerate(list_tmp) :
        
            if nucl == base_princ :

                cmpt_base_princ += 1
                cmpt_tot += 1
                            
            if nucl == base_2 : 
            
                cmpt_tot += 1 
            
            if nucl == base_3 :
            
                cmpt_tot += 1
            
            if nucl == base_4 :

                cmpt_tot += 1

        nb_base_princ = (cmpt_base_princ*100)/cmpt_tot
        i_deb = int(win_nucl_real[window][0])
        i_fin = int(win_nucl_real[window][1])
        i_milieu = ((i_deb+i_fin)-1)/2
        l_nucl_base[i_milieu] = round(nb_base_princ, 2)


    return(l_nucl_base)	    

def compo_to_csv (nb_A, nb_C, nb_G, nb_T, fasta_file,num_seq) : 

    """
    This function allows save in a csv file the base composition for each sequence of the fasta file.
    
    Input : dictionnary with the base composition in % 
    Ouput : a csv file with the composition of each base for each window and for each sequence
    """
    name_seq = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        name_seq.append(record.id)
    
        
    
        
    all_dico = []
    all_dico.append(nb_A)
    all_dico.append(nb_C)
    all_dico.append(nb_G)
    all_dico.append(nb_T) 
    
    labels = []
    for key,value in nb_A.items() :
    

        labels.append(key)
                
    with open("C:/Users/opale/Desktop/prog_ing/15_seq/compo_bases/compo_bases_seq_" + str(num_seq+1) + ".csv", 'w') as f:
        f.write(name_seq[num_seq])
        f.write("\n")
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in all_dico:
            writer.writerow(elem)



############################## MAIN ################################
def main () :



    args = arguments()
    all_seq = get_seq (args.fasta_file)


    genome_len =  get_genome_len (args.fasta_file)
    nb_col = get_col (genome_len ,args.step, args.win_size ) 
    win_nucl = get_windows (args.win_size,args.step,nb_col,genome_len) 
    win_nucl_real = get_real_windows (args.win_size,args.step,nb_col,genome_len)
    list_corr = get_coding_corresponding (args.fasta_file_corr)
   


    for num_seq in range(len(all_seq)) :

        print(num_seq)

        nb_A = get_base_per_window ( "A", "T", "C", "G", win_nucl, win_nucl_real, all_seq, num_seq, list_corr)
        
        nb_C = get_base_per_window ( "C", "T", "A", "G", win_nucl, win_nucl_real, all_seq, num_seq, list_corr)
        nb_G = get_base_per_window ( "G", "T", "C", "A", win_nucl, win_nucl_real, all_seq , num_seq, list_corr)
        nb_T = get_base_per_window ( "T", "A", "C", "G", win_nucl, win_nucl_real, all_seq, num_seq, list_corr)
        
        compo_to_csv (nb_A, nb_C, nb_G, nb_T,args.fasta_file,num_seq)    




if __name__ == '__main__':
    main()
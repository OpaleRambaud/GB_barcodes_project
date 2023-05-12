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
                        
                        
    parser.add_argument("-ws", "--window_size", dest="win_size",
                        type=int, required=True,
                        help="size of the window used for the SWB program")

    parser.add_argument("-s", "--step", dest="step",
                        type=int, required=True,
                        help="step used for the SWB program")
                                                
                        
    parser.add_argument("-al", "--alignment_len", dest="genome_len",
                        type=int, required=True,
                        help="define the lenght of the complete alignment")
                        
                        
    parser.add_argument("-g", "--gap", dest="gap",
                        type=int, default=1,
                        help="do you want to consider a gap like a difference or not ? 0 = no , 1= yes, 2 = ignore gaps ")
    return parser.parse_args()     
    
    
    
def wich_seq1 () :


    seq1 = input("Please enter the name of the first sequence you wish to compare : ")
    print("\n")


    return seq1

def wich_seq2 () :


    seq2 = input("Please enter the name of the second sequence you wish to compare : ")
    print("\n")

    return seq2

    
    
def get_col (genome_len , step, win_size ) :

    """
    This function allows to get the number of window used in the SWB program.
    
    Input : the genome length, the step used in SWB program, the window size used in the SWB program
    Output : number of windows in integer format
    """

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
            win_nucl_real.append((i_deb , genome_len))
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
            
def export_gen_name (fasta_file) :

    """
    This function allows you to export the name of all taxons of the analysis.
    
    Input : original fasta file with sequences.
    Ouput : a list with the name of the genome contains in the fasta.
    """ 

    original_file = str(fasta_file)
    name_list = []
    with open(original_file) as original:
        records = SeqIO.parse(original_file, 'fasta')
        for record in records: 
            name=record.id
            name_list.append(name)
        #print(name_list)
        
    return name_list

    
def get_seq (fasta_file) :

    """
    This function allows to get all sequences from a multi fasta file
    
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


def get_interest_seq1 (name_list, seq1, all_seq) :

    rep = "non"
    for i,name in enumerate(name_list):
    
        if seq1 in name :
        
            return all_seq[i]
            rep = "oui"
            
        
        
            
            
    if rep == "non" :
        
        print("This sequence : " + str(seq1) + " do not exist in the alignment file")
            

def get_interest_seq2 (name_list, seq2, all_seq) :

    rep = "non"
    for i,name in enumerate(name_list):
    
    
        if seq2 in name :
        
            return all_seq[i]
            
            rep = "oui"
            
        
        
            
            
    if rep == "non" :
        
        print("This sequence : " + str(seq2) + " do not exist in the alignment file")            


def cmpt_difference (seq_nucl1, seq_nucl2, gap_or_not) : 

    list_diff = []
    for i,nucl in enumerate(seq_nucl1) :
    
   
        if nucl == "-" : 
        
            if gap_or_not == 0 : 
            
                list_diff.append(0)
                
            if gap_or_not == 1 : 
            
                list_diff.append(1)
                
            if gap_or_not == 2 :
            
                continue
        
        else :    
    
            if nucl == seq_nucl2[i] :
            
                list_diff.append(0)
                
            else :
            
                list_diff.append(1)
            
    return list_diff

def diff_per_win (list_diff , win_nucl_real) :


    l_nucl_base = {}

    for window in range(len(win_nucl_real)) :

        cmpt_diff = 0
        cmpt_idem = 0
        cmpt_tot = 0


        for pos in range(int(win_nucl_real[window][0]), int(win_nucl_real[window][1])+1 ):
        
            pos2 = pos -1
            #print(len(list_diff))
            #print(pos2)
            if list_diff[pos2] == 0 :
            
                cmpt_idem += 1
                cmpt_tot += 1
                
                
            if list_diff[pos2] == 1 :
            
                cmpt_diff += 1
                cmpt_tot += 1 
                
                
        nb_base_diff = (cmpt_diff*100)/cmpt_tot  


        i_deb = int(win_nucl_real[window][0])
        i_fin = int(win_nucl_real[window][1])
        i_milieu = round(((i_deb+i_fin)-1)/2,0)
        l_nucl_base[i_milieu] = round(nb_base_diff, 2)


    return(l_nucl_base)

def diff_to_csv (nb_diff, seq1,seq2, name_base) : 


    all_dico = []
    all_dico.append(nb_diff)
    
    labels = []
    for key,value in nb_diff.items() :
    

        labels.append(key)
                
    with open(name_base + "_SWD_ouput.csv", 'w') as f:
        f.write("Distance in % between " + str(seq1) + " and " + str(seq2))
        f.write("\n")
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in all_dico:
            writer.writerow(elem)

        
######## MAIN ####### 
def main () :

    #print("Please wait")
    
    name_base = os.path.basename(args.fasta_file)
    name_base = name_base.split(".")
    name_base= name_base[0]
    args = arguments()
    seq1 = wich_seq1()
    seq2 = wich_seq2()
    gap_or_not = args.gap
    genome_len = args.genome_len
    name_list = export_gen_name(args.fasta_file)
    all_seq = get_seq (args.fasta_file)
    nb_col = get_col (genome_len ,args.step, args.win_size ) 
    win_nucl = get_windows (args.win_size,args.step,nb_col,genome_len) 
    win_nucl_real = get_real_windows (args.win_size,args.step,nb_col,genome_len)
    
    
    seq_nucl1 = get_interest_seq1(name_list, seq1, all_seq)


    seq_nucl2 = get_interest_seq2 (name_list, seq2, all_seq)
    
    
    list_diff = cmpt_difference (seq_nucl1, seq_nucl2, gap_or_not)
    
    nb_diff = diff_per_win(list_diff , win_nucl_real)
    
    diff_to_csv (nb_diff, seq1,seq2)
    
    print("Your file is ready you can find it in the current file!")
    
if __name__ == '__main__':
    main()
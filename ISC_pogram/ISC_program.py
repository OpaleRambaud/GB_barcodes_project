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
    return parser.parse_args() 


    
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


                
                
def count_nt (fasta_file) :

    nt_dic = {}
    # nts = ["N", "A", "T", "C", "G"]
    for seq in SeqIO.parse(fasta_file, "fasta"): 
        for index, nt in enumerate(seq):
            pos = index + 1
            if pos not in nt_dic.keys():
                nt_dic[pos] = {}
            if nt not in nt_dic[pos]:
                nt_dic[pos][nt] = 0
            nt_dic[pos][nt] += 1
            
    return nt_dic


def dic_inf_site (nt_dic) :

    sites_inf = {}
    cmpt = 0

    for i in nt_dic :
        
        
        if len(nt_dic[i]) == 1 :
            sites_inf[i] = 0
            
        if len(nt_dic[i]) > 2 :
            sites_inf[i] = 1
            
        if len(nt_dic[i]) == 2 :        
            ke = []
            for key in nt_dic[i].keys() :
                ke.append(key)
                
            for k in ke : 
                if nt_dic[i][k] > 1 :
                    cmpt += 1
                    
            if cmpt == 2 :
                sites_inf[i] = 1
                
            if cmpt < 2:        
                sites_inf[i]= 0

            cmpt = 0
            
            
    return sites_inf



def site_inf_win (sites_inf , win_nucl_real) :


    l_nucl_base = {}

    for window in range(len(win_nucl_real)) :

        cmpt_sites = 0



        for pos in range(int(win_nucl_real[window][0]), int(win_nucl_real[window][1])+1 ):
            pos2 = pos -1   
            nb = sites_inf.get(pos)
            
            
            cmpt_sites += nb
            #print(cmpt_sites)

        i_deb = int(win_nucl_real[window][0])
        i_fin = int(win_nucl_real[window][1])
        i_milieu = round(((i_deb+i_fin)-1)/2,0)
        l_nucl_base[i_milieu] = cmpt_sites
        
    return l_nucl_base    



def diff_to_csv (nb_site) : 


    all_dico = []
    all_dico.append(nb_site)
    
    labels = []
    for key,value in nb_site.items() :
    

        labels.append(key)
                
    with open("ISC_ouput.csv", 'w') as f:
        f.write("Number of informatives sites ")
        f.write("\n")
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in all_dico:
            writer.writerow(elem)    
############################## MAIN ################################
def main () :

    print("Please wait")
    
    args = arguments()
    
    
    genome_len = args.genome_len
    
    nb_col = get_col (genome_len ,args.step, args.win_size ) 
    win_nucl = get_windows (args.win_size,args.step,nb_col,genome_len) 
    win_nucl_real = get_real_windows (args.win_size,args.step,nb_col,genome_len)
    
    nt_dic = count_nt(args.fasta_file)
    sites_inf = dic_inf_site (nt_dic)
    nb_site = site_inf_win (sites_inf , win_nucl_real)
    
    diff_to_csv (nb_site)
    
    
    
    print("Analysis done ! Your file is ready, you can find it in the current file.")



if __name__ == '__main__':
    main()    
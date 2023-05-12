import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
import argparse
from Bio import SeqIO


from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.rcParams['figure.dpi'] = 250



def arguments():


    parser = argparse.ArgumentParser()

    # Mandatory arguments

                        
    parser.add_argument("-r", "--results_file", dest="results_file",
                        type=str, required=True,
                        help="results_file is .csv file with the results of SWB program")       

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
                
def number_of_row (data) :

    nb_of_row = len(data.index)

    return nb_of_row
    
    
def cmpt_bp (data, win_nucl_real) :

    l_nucl_base = {}
    sup0 = 0

    for window in range(1,len(win_nucl_real)+1) :
    
        data_tolist = data[str(window)].values.tolist()
        
        #print(data_tolist)
        for el in data_tolist : 
            if el > 0 :
                sup0 +=1

        i_deb = int(win_nucl_real[window-1][0])
        i_fin = int(win_nucl_real[window-1][1])
        i_milieu = round(((i_deb+i_fin)-1)/2,0)
        l_nucl_base[i_milieu] = round(sup0, 2)
        
    return l_nucl_base

def diff_to_csv (nb_sup0) : 


    all_dico = []
    all_dico.append(nb_sup0)
    
    labels = []
    for key,value in nb_sup0.items() :
    

        labels.append(key)
                
    with open("BPC_ouput.csv", 'w') as f:
        f.write("Number of bipartition with bootstrap >0")
        f.write("\n")
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in all_dico:
            writer.writerow(elem)

def main () :

    args = arguments()
    

    
    
    genome_len = args.genome_len
    
    nb_col = get_col (genome_len ,args.step, args.win_size ) 
    win_nucl = get_windows (args.win_size,args.step,nb_col,genome_len) 
    win_nucl_real = get_real_windows (args.win_size,args.step,nb_col,genome_len)
    data = pd.read_csv(args.results_file)  

    nb_sup0 = cmpt_bp (data, win_nucl_real)
    
    diff_to_csv (nb_sup0)
    
    print("your file is ready you can find it in the current file !")
    
if __name__ == '__main__':
    main()

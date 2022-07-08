"""

This barcode module file contain all the functions to build the bardcodes.

The input is a csv file from set data module.

The output are barcodes in png format for each line of the input csv.  

"""

####################### IMPORT ##########################

import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.rcParams['figure.dpi'] = 600

plt.rcParams["savefig.bbox"] = 'tight'

################### SETTINGS : 

                  
                        

def number_of_columns(data_sorted) :


    """
    This function allows to create a list with the position of the start and 
    the finish of each windows. 
    
    Input : genome length, size of the windows and the step.
    Ouput : a list with the position of the start and the finish of each windows.
    """
    
    column_list = data_sorted.columns
    nb_of_col = (len(column_list)-3)

    return nb_of_col
    
def number_of_row (data_sorted) :

    nb_of_row = len(data_sorted.index)

    return nb_of_row

def put_name_in_dict (data_sorted) :
 
   dic_name = {}
   cmpt = 1
   for i in data_sorted["Sequence names"] :
        dic_name[i] = cmpt 
        cmpt += 1  
   return dic_name
    
def bootstrap_per_windows (window_size,step,nb_col,data_sorted,nb_of_row,genome_len) :


    """
    This function allows create a list with the value of the median bootstrap for each windows.
    
    Input : results csv file, list of windows.
    Ouput : a list with the value of median bootstrap for each window.
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
            win_nucl.append((i_milieu+1 ,genome_len))
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
        

    l_row_csv = []
    l_col_csv =[]

    data_tolist = data_sorted.values.tolist()

    for x in range(0,nb_of_row): 
        l_col_csv =[]
        for i,j in zip(win_nucl,data_tolist[x][3:]):
            l_col_csv.append((i,j))
        l_row_csv.append(l_col_csv)
        
    return l_row_csv



################## PLOT :




def set_color_for_barcodes (x) : 

    """
    This function allows to set the color for the barcodes.
    The red represents the area with a bootstrap lower than 30.
    The green represents the area with a bootstrap superior to 70.
    The grey represents the area with a bootstrap between 30 and 70.
    
    
    Input : values of limit for each color.
    Ouput : colors.
    """

    if x < 30:
        return "r"
    
    if x > 70:
        return "darkgreen"
    
    return "grey"

def barcodes_plot (data_sorted, dic_name2, l_row_csv, nb_of_row) :


    """
    This function allows to build and save the barcodes for each lines of the results csv file.
    The barcodes will be colored according to the limits determined in the previous function.  
    You can choose the location to save the barcodes. 
    
    Input : results csv file from SWB.
    Ouput : barcodes in png format.
    """

    fig, ax = plt.subplots()
    lim_fin = l_row_csv[-1][-1][0][1]

    for i in range(len(l_row_csv)) :
        
        fig, ax = plt.subplots()
        plt.xlim(1,(lim_fin/1000))
        plt.ylim(0,1)
        plt.subplots_adjust(top = 0.3)
        ax.set_yticklabels([])
        ax.xaxis.set_visible(False) ###### set scale or not
        ax.yaxis.set_visible(False)
        ax.xaxis.set_major_locator(MultipleLocator(4))
        

        for el in l_row_csv[i]:
            ax.plot()
            col = set_color_for_barcodes(el[1])
            ax.axvspan((el[0][0]/1000), (el[0][1]+1)/1000, alpha=1, facecolor= col , edgecolor = 'none' )

        jpp = data_sorted["Sequence names"][i]
        #plt.title( "N°" + str(dic_name2[jpp]) , loc= 'left', fontname="Times New Roman")
        print("Create barcode " + str(dic_name2[jpp]) + " out of " + str(nb_of_row))
        plt.savefig("./BC_"+str(dic_name2[jpp]) + ".png" , transparent= True)  
        plt.clf()
        plt.close(fig)

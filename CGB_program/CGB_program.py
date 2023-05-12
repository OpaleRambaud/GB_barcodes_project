# -*- coding: utf-8 -*-



###### IMPORT #########


import argparse
import csv
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
import re
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.rcParams['figure.dpi'] = 600

plt.rcParams["savefig.bbox"] = 'tight'

plt.rcParams.update({'figure.max_open_warning': 0})

plt.rcParams['axes.facecolor'] = 'white'

####### FUNCTIONS #######
def arguments():


    parser = argparse.ArgumentParser()

    # Mandatory arguments
    parser.add_argument("-bp", "--bipartition_file", dest="alternatives_file",
                        type=str, required=True,
                        help="alternatives_file is a .csv file with the bipartition you want to color")
                        
                        
    parser.add_argument("-al", "--alignment_len", dest="genome_len",
                        type=int, required=True,
                        help="define the lenght of the complete alignment")

    parser.add_argument("-sc", "--scale", dest="scale_or_not",
                        type=int, default=0,
                        help="define if you want a scale on the bc or not")
                        
                        
    parser.add_argument("-gr", "--graduation", dest="graduation_value",
                        type=int, default=4000,
                        help="define the graduation you want for your scale")                        
                          
 
    return parser.parse_args()
    
    
def color_to_number () :

    color_num = {}
    cmpt = 0
    for cname, hex in matplotlib.colors.cnames.items():
        cmpt += 1
        color_num[cmpt]= cname
        
    return color_num
    
    
def get_inter (csv_file) :

    dic_inter = {}


    with open(csv_file) as csvfile:
    
        line = csvfile.readlines()
        for el in line [1:] :
            #print(el)
            el2 = el.split(";")
            if len(el2) > 1 :
                frag_ref = []
                bp_number = el2[0]


                
                
                interv = el2[1]
                #if interv != "intervals": 
                interv2 = interv.strip("\n")
                interv3 = interv2.split(" ")

                for intervv in interv3 :   
                    interv4 = intervv.split("-")
                    frag_ref.append((int(interv4[0]),int(interv4[1])))
            
            #if len(bp_number) < 10 :
                dic_inter[bp_number] = frag_ref
    #print(dic_inter)
    return dic_inter
    
    
    
def get_color (csv_file) : 

    dic_color = {}
    
    with open(csv_file) as csvfile:
    
        line = csvfile.readlines()
        for el in line [1:]:
            el2 = el.split(";")
            if len(el2) > 1 :
                
                bp_number = el2[0]
                
                color = el2[2]
        

                dic_color[bp_number] = int(color)
    

    return dic_color
    
def get_barcode_interest (value, chosing_color, genome_len,key, scale_or_not, graduation) :


    fig, ax = plt.subplots()
    lim_fin = genome_len

    #for i in range(len(value)) :
        
    fig, ax = plt.subplots()
    plt.xlim(1,(lim_fin))
    plt.ylim(0,1)
    plt.subplots_adjust(top = 0.3)
    ax.set_yticklabels([])
    if scale_or_not == 0 :
        ax.xaxis.set_visible(False) 
    if scale_or_not == 1 :
        ax.xaxis.set_visible(True)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_major_locator(MultipleLocator(graduation))
    

    for el in value:
    

        ax.plot()
        col = str(chosing_color)
        ax.axvspan((el[0]), (el[1]+1), alpha=1, facecolor= col , edgecolor = 'none' )


    plt.savefig("colored_bc_" + str(key) + ".png" , transparent= True)  
    plt.clf()
    plt.close(fig)    
    
def pick_a_color (dico_colors,key, dico_color) :



    choosing_color = dico_color[key]
    
    #print(choosing_color)
    
    return dico_colors[choosing_color]    
    
def main () : 

    args = arguments()
    print("Construction in progress , please wait ...")
    csv_file = args.alternatives_file
    genome_len = args.genome_len
    scale_or_not = int(args.scale_or_not)
    graduation = int(args.graduation_value)
    dico_colors = color_to_number ()   
    
    dico_interv = get_inter(csv_file)
    dico_color = get_color(csv_file)
    for key, value in dico_interv.items() :
    
        #print(value)
        cmpt = 0
        #for el in key :
            #if el == "2" :
                #cmpt += 1
            #if el == "1" :
                #cmpt += 1
        #if cmpt == 3 :
        chosing_color = pick_a_color(dico_colors , key, dico_color)
        get_barcode_interest (value, chosing_color, genome_len,key, scale_or_not, graduation)
    print("Your barcodes are all done ! You can see them in the current field.")
    
if __name__ == '__main__':
    main()   
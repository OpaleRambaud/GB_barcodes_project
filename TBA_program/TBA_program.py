import re
from itertools import combinations
import itertools
import argparse
import csv
import pandas as pd
import os

def arguments():


    parser = argparse.ArgumentParser()

    # Mandatory arguments
    parser.add_argument("-n", "--newick_file", dest="newick_file",
                        type=str, required=True,
                        help="newick_file is a .tre file containing the parenthesis tree")
                        
                        
    parser.add_argument("-r", "--results_file", dest="results_file",
                        type=str, required=True,
                        help=" results_file is .csv file with the results of SWB program")   
                        
    parser.add_argument("-ws", "--window_size", dest="window_size",
                        type=int, required=True,
                        help="define the size of the window used in the analysis")
                        
    parser.add_argument("-s", "--step", dest="step",
                        type=int, required=True,
                        help="define the step of the window used in the analysis")
                        
                        
    parser.add_argument("-gl", "--genome_len", dest="genome_len",
                        type=int, required=True,
                        help="define the lenght of the complete alignment")
                        
                    
                        
    return parser.parse_args()


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
    
    
    
def get_tree (newick_file) :

    original_file = str(newick_file)
    with open(newick_file) as f:
        lines = f.readline()
        lines = re.sub("\;|","",lines)
        
        
        return lines

def get_noeuds (tree) :

    
    inner = "("
    outer = ")"
    separator = ","
    noeuds_list = []
        
    for el in range(len(tree)) :
        if tree[el] == inner :
            cmpt_inner = 0
            cmpt_outer = 0
            tmp = []
            deb = el
            for el2 in range(el, len(tree)) :
                if tree[el2] == inner :
                    cmpt_inner += 1
                if tree[el2] == outer :
                    cmpt_outer += 1
       

                if cmpt_inner == cmpt_outer :

                    
                    fin = el2
                    break

            for i in range(deb,fin+1) :
            
                tmp.append(tree[i])
                
            tmp2 = "".join(tmp)
            noeuds_list.append(tmp2)
       
    
    ###### get noeuds_list without ( 

    noeuds_list2 = []
    for nn in noeuds_list :
        string = nn
        string = re.sub("\(|\)|","",string)
        noeuds_list2.append(string)
    
    
    noeuds_list3 = [] 
    
    for nnn in noeuds_list2 :
        ss = nnn.split(",")
        noeuds_list3.append(ss)

   
    return noeuds_list3

def get_taxons_name (tree) :

    test_sp = tree.split(",")
    taxons2 = []

    for tax in test_sp : 
        string = tax
        string = re.sub("\(|\)|","",string)
        taxons2.append(string)
        

    return taxons2

def get_combin (tax_name, nb) :
    combin = combinations(tax_name, nb)
    combin = list(combin)

    return combin

def get_alternative (noeuds, tax_name) : 
        
    nb_max = len(tax_name)
    
    alter2 = []
    
    d_sp = noeuds
    
    for nb in range(2,nb_max+1) : 
        combin = get_combin(tax_name, nb)
    
        for ii in combin :
             cmpt = 0
             cmpt2 = 0
             cmpt3 = 0
             for iii in ii :
                 for d in d_sp :
                     if d == iii :
                         cmpt += 1
                         
                     if iii not in d_sp :
                         cmpt2 += 1
                         
                     if iii in d_sp :

                         cmpt3 += 1                
                         
             if cmpt < len(d_sp) and cmpt2 >= 1 and cmpt3 >= 1:
                 alter2.append(ii)
    
    return alter2
    
def get_results_csv_name (data ) :

    ### lire tout les noms :
    names = data['Sequence names'].tolist()
    names2 = []
    for i in names :
        string = i
        string2 = string.split("+")
        names2.append(string2)
    for ii in range(len(names2)) :
        for iii in range(len(names2[ii])) :
            names2[ii][iii] = names2[ii][iii].strip()
    
    return names2
    
    
    
def matching_in_reference (name_ref , noeuds) :
    
        for sublistb in name_ref :
            if (set(noeuds) == set(sublistb)) :
                return sublistb




def match_or_not (data , noeuds) :


    #for index, row in data.iterrows():
    for label, content in data['Sequence names'].items():
        content = content.split("+")
        for el in range(len(content)) : 
            content[el] = content[el].strip()
        if (set(noeuds) == set(content)) :
            #print(label+2)
            return label
    
    
def get_line_in_ref (row_in_data , data) :

    if type(row_in_data) == int :
        good_line = data.iloc [row_in_data]
        good_line2 = good_line.tolist()
        #print(good_line2)
        return good_line2
        #good_line.to_csv("matching_nodes.csv")
        #with open("matching_nodes.csv", 'w') as f:
            #f.write(good_line)
            #f.write("\n")
        #return good_line


def create_csv (name_base) :

    csv_name = name_base + "_alternatives_output.csv"

    with open(csv_name, 'w') as f:
        pass
    return csv_name    



#def print_in_csv (ref_line) :

def is_bip_alternatives (data , noeuds , dico_alternatives) :

    
    #print(noeuds)
    noeud_ref = set(noeuds)
    
    taille_noeud = len(noeuds)
    #noeuds2 = ",".join(noeuds)
    tmp = []
    #label_ref = []
    label_ref = "None"
    for label, content in data['Sequence names'].items():
        content = content.split("+")
        for el in range(len(content)) : 
            content[el] = content[el].strip()
        
        noeud_alt = set(content)
        
        if noeud_alt == noeud_ref :
        
            label_ref = label
            #print(label_ref)
        
        cmpt_il_est = 0
        cmpt_un_reste = 0
        for nd in noeud_alt :
        
            #savoir si il y sont pas tous :
        
            if nd in noeud_ref :
                cmpt_il_est += 1
                
            # savoir si ya au moins un du reste     
                
            if nd not in noeud_ref :
                cmpt_un_reste += 1 
            
        if cmpt_il_est < taille_noeud and cmpt_il_est >= 1 and cmpt_un_reste >= 1 :
        
            tmp.append(label)
    
    
    if label_ref != "None" :
        dico_alternatives[label_ref] = []
        for lab in tmp :        
            dico_alternatives[label_ref].append(lab)   

    return dico_alternatives   





def get_win_nucl (nb_col, window_size, step , genome_len) :

     
    
    win_nucl =[]
    i_deb = 1
    i_fin = window_size 
    stepp = step  
    i_milieu = ((i_deb+i_fin)-1)/2
    i_pas = i_milieu + stepp
    for i in range(1,(nb_col+1)):
        #print(i)
        if i == 1 : 
            win_nucl.append(int(window_size/2))
            i_milieu = i_milieu + stepp
            i_deb = i_deb + stepp
            i_fin = i_fin + stepp
            i_pas = i_pas + stepp
        if i == (nb_col-1) :
            pos = i_milieu
            int_pos = int(float(i_milieu))
            str_pos = str(int_pos)
            win_nucl.append(str_pos)
            i_milieu = i_milieu + stepp
            i_deb = i_deb + stepp
            i_fin = i_fin + stepp
            i_pas = i_pas + stepp
            break
            
        else : 
            pos = i_milieu
            int_pos = int(float(i_milieu))
            str_pos = str(int_pos)
            win_nucl.append(str_pos)
            i_milieu = i_milieu + stepp
            i_deb = i_deb + stepp
            i_fin = i_fin + stepp
            i_pas = i_pas + stepp
        
    return win_nucl



def get_cool_frag ( v, data , win_nucl) :

    good_line = data.iloc[v]
    data_list = good_line.tolist()    
    data_list2 = data_list[3:]
    
    
    frag_in_window = []
    
    frag_tmp = [] 
    cmp = 0
    aa = False
    #print(len(data_list2))
    for index,value in enumerate(data_list2) :
        #print(index)
        #print(index)
        #print(value)
        if value < 50 :
            pass
        if value >= 70 :
            if aa == False :
                frag_tmp.append(index) ############### ===== debut 
                aa = True
            last_70 = index
        

            
        if value >=50 and value <70 :  
        
            if index != len(data_list2) -1 :

                if aa == True : 
                    if data_list2[index+1] < 50 : 
                
                        aa = False
                        frag_tmp.append(last_70)
                        frag_in_window.append(frag_tmp)
                        frag_tmp = []


        if index != 0 :

            if value <50 and data_list2[index-1] >= 70 :
            
                frag_tmp.append(index-1)
                frag_in_window.append(frag_tmp) ################# fin
                frag_tmp = []
                aa = False
                #cmpt = 0
            
        if index == len(data_list2) -1 :
            #print(index)
        
            if aa == True :
                frag_tmp.append(last_70)
                frag_in_window.append(frag_tmp)
            
                break
        #print(aa)

    #print("ligne numero : ")
    #print(v)
    #return frag_in_window
            
    frag_in_winnucl = []
    
    for fr in range(len(frag_in_window)) :

        deb = frag_in_window[fr][0]
        fin = frag_in_window[fr][1]
        
        deb_nucl = win_nucl[deb]
        fin_nucl = win_nucl[fin]
        int_deb = int(float(deb_nucl))
        int_fin = int(float(fin_nucl))
        str_deb = str(int_deb) 
        str_fin = str(int_fin)
        str_all = str_deb + "-" + str_fin 
        frag_in_winnucl.append(str_all)

    #print(frag_in_window)
    #print(frag_in_winnucl)
    return frag_in_winnucl

    
     
   
def main () :

    ####### INIT #######
    args = arguments()
    data = pd.read_csv(args.results_file)
    name_base = os.path.basename(args.newick_file)
    name_base = name_base.split(".")
    name_base= name_base[0]
    csv_name = create_csv(name_base)
    nb_col = number_of_columns(data)
    nb_of_row = number_of_row(data)
    tree = get_tree(args.newick_file)
    dico_alternatives = {}
    
    
    window_size = args.window_size
    step = args.step
    genome_len = args.genome_len
    
    win_nucl = get_win_nucl (nb_col, window_size, step , genome_len)
    
    
    #head = data.iloc[0]
    #print(head)
    #print(len(win_nucl))
    head = list(data)
    ###### GET NODES #####
    noeuds_list = get_noeuds (tree)
    tax_name = get_taxons_name (tree)
        
    name_ref = get_results_csv_name (data)        
    
    
    ###### GET ALTERNATIVES  + GET FRAGMENTS #######
    for noeuds in noeuds_list :
        is_bip_alternatives (data , noeuds , dico_alternatives )
    
    
    win_nucl.insert(0,"Median positions")
    win_nucl.insert(0,"")
    win_nucl.insert(0,"")
    
    with open(csv_name, 'a') as f :
        writer = csv.writer(f , lineterminator ="\n", delimiter=',')
        writer.writerow(win_nucl)
        writer.writerow("")
        writer.writerow(head)
        writer.writerow("")
        
        
    del win_nucl[0]
    del win_nucl[0]
    del win_nucl[0]
    
    cmpt1 = 1
    for key, value in dico_alternatives.items() :
    
        
    
        cmpt2 = 1
    
        if len(value) != 0 :
    
            ligne_ref = get_line_in_ref (key , data)
            pref = "Reference Tree - Node N°" + str(key+1)
            ligne_ref.insert(0,pref)
            del ligne_ref[1]
            cool_frag_ref = get_cool_frag ( key, data, win_nucl)
            pref2 = "GRPS related to bipartition N°" + str(key+1) + ","
            cool_frag_ref.insert(0,pref2)
            
            
            with open(csv_name, 'a') as f :
                
                writer = csv.writer(f, lineterminator ="\n")
                #f.write("Reference node " + str(cmpt1))
                f.write("\n")
                writer.writerow(ligne_ref)
                #f.write("Fragments reference node " + str(cmpt1))
                #f.write("\n")
                writer = csv.writer(f , lineterminator ="\n" , delimiter=' ' )
                writer.writerow(cool_frag_ref)
                f.write("\n")
                f.write("Phylogenetic signal(s) in conflicts with node N°" + str(key+1))
                #f.write("\n")
                
            cmpt1 += 1
            for v in value :
                ligne_alt = get_line_in_ref (v , data)
                pref3 = "Bipartition N°" + str(v+1)
                ligne_alt.insert(0,pref3)
                del ligne_alt[1]
                cool_frag = get_cool_frag ( v, data, win_nucl)
                pref4 = "GRPS related to bipartition N°" + str(v+1) + ","
                cool_frag.insert(0,pref4)
                with open(csv_name, 'a') as f :
                
                    writer = csv.writer(f , lineterminator ="\n")
                    #f.write("Alternatives " + str(cmpt2))
                    f.write("\n")
                    writer.writerow(ligne_alt)
                    #f.write("Fragments alternatives " + str(cmpt2))
                    #f.write("\n")
                    writer = csv.writer(f , lineterminator ="\n" , delimiter=' ')
                    writer.writerow(cool_frag)
                
                cmpt2 += 1 
                    
                    
                    
            with open(csv_name, 'a') as f :
                    f.write("\n")
                    #writer = csv.writer(f , lineterminator ="\n")
                    #writer.writerow("")
                    
    


    print("Your alternatives csv file is ready. You can find it in the current file !") 
    
    
    
    

    
    
    
if __name__ == '__main__':
    main()

        
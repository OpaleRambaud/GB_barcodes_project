"""

This set data module contains all the functions to prepare the data for the barcodes.

The input file is result of SWB program (csv file).
The ouput is a clean and sorting csv file who can be use to build barcodes.

"""





########## IMPORT : 


from Bio import SeqIO
import string 
import csv
import pandas as pd


###### DATA SETTING POST BSW :

###### GET GENOME LEN : 

      
def get_genome_len (fasta_file) :

    original_file = str(fasta_file)
    with open(original_file) as original :
        records = SeqIO.parse(original_file, 'fasta')
        for record in records:
            sequ = record.seq
            genome_len = len(sequ)
            break
        
    return genome_len
    
###################### FILTERING AND SORTING : 



def filtering_sup (csv_file, filter_value) : 

    """
    This function allows to filter the results of the bsw program by choosing all lines with at least one 
    bootstrap superior at your filter value.
    
    Input : results csv file, the filter value.
    Ouput : the same file but filtered.  
    """

    data = pd.read_csv(csv_file) ########## attention argument
    l = []
    for i in range(1,len(data.columns)) :
        l.append(str(i))
        
    for j in l :
        data[j] = data[j].astype(int)    
    data['max value'] = data.max(axis=1)
    data_sup = data.loc[data["max value"] >= filter_value]  ###### attention arguement 
    del data_sup["max value"]
    del data["max value"]
    data_sup.to_csv("data_filtered_sup_" + str(filter_value) + ".csv", index = False) 
    
    filtered = "data_filtered_sup_" + str(filter_value) + ".csv"
    
    return filtered
    
    

def sorted_by_bt (filtered) :
    
    data = pd.read_csv(filtered)
    data['mean value'] = data.mean(axis=1)
    sorted_data = data.sort_values(by=['mean value'], ascending=False)
    del data["mean value"]
    del sorted_data["mean value"]
    sorted_data.to_csv("data_filtered_sup_sorted.csv", index = False)
    
    sorted = "data_filtered_sup_sorted.csv"
    return sorted       


###### GET NAMES : 

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
        

def name_list_to_dico (name_list) :

    """
    This function allows you to transform the list with the names of the taxons into a dictionnary.
    
    Input : the names list.
    Ouput : a dict with the names associated with a number.
    """ 
    
    dic_name = {}
    num_name = 1
    for i in name_list : 
        dic_name[num_name] = i
        num_name += 1 
    
    return dic_name
    print(dic_name)   



def translate_stars_to_named (sorted, dic_name) : 

    """
    This function allows to translate the column with dashes and stars that 
    represents the taxa present or not in the analysis in the csv file by 
    the corresponding names from the name dictionary .
    
    Input : The name dictionnary and the csv results file.
    Ouput : a csv file with the name for each lines of the results csv file.
    """ 
    # Extraction colonne
    
    name_file = "name_" + sorted
    
    with open(sorted) as f:
        lst1 = [row1.split()[0] for row1 in f];
        lst2 = [row2.split(",") for row2 in lst1];
        lst3 = [row3[0] for row3 in lst2];
        lst4 = lst3[1:];

        # Liste propre
        lst = [row.replace('"','') for row in lst4];

    # Resultat
    res_lst = [];

    for s in lst:
        tmp_lst =[];
        for i in range(len(lst[1])):
            if s[i] == "*":
                tmp_lst.append(dic_name[i+1]);
        res_lst.append(' + '.join(tmp_lst))


    with open(sorted, 'r') as infile, open(name_file, 'w') as outfile:
        writer = csv.writer(outfile, lineterminator='\n')
        aa = ["Sequence names"]
        writer.writerow(aa)
        for val in res_lst:
            writer.writerow([val])  
            
    return name_file
 


def unnamed_to_named (sorted, name_file , name_base) : ######### attention arguments.

    """
    This function allows to concatenate the csv file with the names and the results csv file.
    
    Input : csv with the names and resulats csv.
    Ouput : concatenate csv 
    """
    
    data = pd.read_csv(sorted)
    #print(data)
    names = pd.read_csv(name_file) #### mettre en variable !! 
    data2 = pd.concat([names, data], axis=1)
    nb_row = len(data2.index)
    nb_row2 = []
    for n in range(1,nb_row +1 ) :
        nb_row2.append(n)
    data2.insert(0, "Bipartition number", nb_row2)
    l = list(data2)
    to_change = l[2]
    #data2.rename(columns = {'Names':'Sequence names'}, inplace = True)
    data2.rename(columns = {to_change :"Bipartitions"},  inplace=True)
    #print(list(data2))
    data2.to_csv(name_base + "_output_bp_sup_70.csv", index = False)
    
    named_file = name_base + "_output_bp_sup_70.csv"
    return named_file 
    
    




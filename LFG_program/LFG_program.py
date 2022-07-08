######### IMPORT ########

import pandas as pd

import argparse
import os



###### FUNCTIONS #######


def arguments():


    parser = argparse.ArgumentParser()

    # Mandatory arguments

                        
    parser.add_argument("-r", "--results_file", dest="results_file",
                        type=str, required=True,
                        help="results_file is .csv file with the results of SWB program")                        

    return parser.parse_args()



    

def get_log_file (data) :


    first = data[["Unnamed: 0","1"]]
    column_list = data.columns
    nb_col = (len(column_list))
    nb_rows = (len(data.index) +1) 


    rows = [i for i in range (1, nb_rows)] 
    col = [i for i in range(1,nb_col)]

    with open ("./log_files/windows.txt", "w") as f:  
        for co in col :
            f.write(str(co))
            f.write("\n")
            
    first2 = first.loc[data["1"] != 0]

    all_tax = data.iloc[0][0]

    for co in col :
        tmp = data[["Unnamed: 0",str(co)]]
        tmp2 = tmp.loc[data[str(co)] != 0] #enlever les lignes avec des zéros
        tmp3 = tmp2.loc[data["Unnamed: 0"] != str(all_tax)]
        st = tmp3.to_string(index=False, header=False, justify="start")
        with open ("./log_files/"+str(co)+".log", "w") as f : 
            f.write(st)
            
            
    for co in col :
        with open("./log_files/"+str(co)+".log", 'r') as fin: 
            lines = fin.readlines()
            del lines[0]
        with open("./log_files/"+str(co)+".log", 'w') as fout: 
            for line in lines:
                fout.write(line.replace('-', '.'))


    for co in col :
        with open("./log_files/"+str(co)+".log", 'r') as fin: 
            lines = fin.readlines() 
        with open("./log_files/"+str(co)+".log", 'w') as fout: 
            for line in lines:
                fout.write(line[1:])   



def main () :

    args = arguments()
    
    data = pd.read_csv(args.results_file)
    
    
    if not os.path.exists('./log_files'):
        os.makedirs('./log_files')
    
    get_log_file(data)
    
    

######## MAIN #######

if __name__ == '__main__':
    main()            
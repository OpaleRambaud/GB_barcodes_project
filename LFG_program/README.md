# Log_files_generation program 

## Related project : GB_barcodes_project

Copyright (C) 2022 Alexandre Hassanin MNHN


__Authors :__

Opale Rambaud (under the direction of  : Alexandre Hassanin)


__Contact :__

If you have any questions about this script please send an email at : alexandre.hassanin@mnhn.fr

--------------------------------------------------------------------------------------------------------------------------------------------


## Quick description of the program : 

This program generates the log files necessary for the supertri program from the SWB program results file. One log file will be obtained per analysis window. 
We find in a .log file the column representing the concerned taxa for each bipartition and the bootstrap result for this window. Only the non-zero boostrap are kept. 

The outputs of this program are: a .log file for each analysis window and a windows file containing the total number of analysis windows. 


## Language :

This script is in Python 3.7.3

## Prerequisites : 

The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.
Please make sure run this script with the Phylo environment using for all programs of the GB_barcodes_project.


## Using the program : 

To use the program, you must be in the "supertri_program" directory and run the following command :

```
python main_supertri.py -r <SWB_FILE>
```

With the following arguments:

- *SWB_FILE* : The file in .csv format containing the results of the SWB program. 
(The name of the results file is : "name_of_the_alignment_SWB_ws_s.csv").


##### Example of use : 

```
python main_supertri.py -r alpha_Rhinacovirus_SWB_ws2000_s50.csv
```


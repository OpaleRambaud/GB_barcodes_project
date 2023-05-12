# CGB program 

## Related project : GB_barcodes_project

Copyright (C) 2022 Sorbonne Université / Institut de Systématique, Évolution, Biodiversité (ISYEB) / Hassanin Rambaud

__Authors :__

Alexandre Hassanin
Opale Rambaud 



__Contact :__

If you have any questions about this script please send an email at : alexandre.hassanin@mnhn.fr or opale.rambaud@gmail.com

--------------------------------------------------------------------------------------------------------------------------------------------


## Quick description of the program : 

This program generate colored barcode from a file containing the areas you want to color. 

/!\ important note : you have to give a csv file with the informations of the barcode you want to color : the number of
the bipartition, the areas to color and the number of the color.
Please use the exemple_file as a example to format your file.

The available colors are in the following list : 

1 : aliceblue 
2 : antiquewhite 
3 : aqua 
4 : aquamarine 
5 : azure 
6 : beige 
7 : bisque 
8 : black 
9 : blanchedalmond 
10 : blue 
11 : blueviolet 
12 : brown 
13 : burlywood 
14 : cadetblue 
15 : chartreuse 
16 : chocolate 
17 : coral 
18 : cornflowerblue 
19 : cornsilk 
20 : crimson 
21 : cyan 
22 : darkblue 
23 : darkcyan 
24 : darkgoldenrod 
25 : darkgray 
26 : darkgreen 
27 : darkgrey 
28 : darkkhaki 
29 : darkmagenta 
30 : darkolivegreen 
31 : darkorange 
32 : darkorchid 
33 : darkred 
34 : darksalmon 
35 : darkseagreen 
36 : darkslateblue 
37 : darkslategray 
38 : darkslategrey 
39 : darkturquoise 
40 : darkviolet 
41 : deeppink 
42 : deepskyblue 
43 : dimgray 
44 : dimgrey 
45 : dodgerblue 
46 : firebrick 
47 : floralwhite 
48 : forestgreen 
49 : fuchsia 
50 : gainsboro 
51 : ghostwhite 
52 : gold 
53 : goldenrod 
54 : gray 
55 : green 
56 : greenyellow 
57 : grey 
58 : honeydew 
59 : hotpink 
60 : indianred 
61 : indigo 
62 : ivory 
63 : khaki 
64 : lavender 
65 : lavenderblush 
66 : lawngreen 
67 : lemonchiffon 
68 : lightblue 
69 : lightcoral 
70 : lightcyan 
71 : lightgoldenrodyellow 
72 : lightgray 
73 : lightgreen 
74 : lightgrey 
75 : lightpink 
76 : lightsalmon 
77 : lightseagreen 
78 : lightskyblue 
79 : lightslategray 
80 : lightslategrey 
81 : lightsteelblue 
82 : lightyellow 
83 : lime 
84 : limegreen 
85 : linen 
86 : magenta 
87 : maroon 
88 : mediumaquamarine 
89 : mediumblue 
90 : mediumorchid 
91 : mediumpurple 
92 : mediumseagreen 
93 : mediumslateblue 
94 : mediumspringgreen 
95 : mediumturquoise 
96 : mediumvioletred 
97 : midnightblue 
98 : mintcream 
99 : mistyrose 
100 : moccasin 
101 : navajowhite 
102 : navy 
103 : oldlace 
104 : olive 
105 : olivedrab 
106 : orange 
107 : orangered 
108 : orchid 
109 : palegoldenrod 
110 : palegreen 
111 : paleturquoise 
112 : palevioletred 
113 : papayawhip 
114 : peachpuff 
115 : peru 
116 : pink 
117 : plum 
118 : powderblue 
119 : purple 
120 : rebeccapurple 
121 : red 
122 : rosybrown 
123 : royalblue 
124 : saddlebrown 
125 : salmon 
126 : sandybrown 
127 : seagreen 
128 : seashell 
129 : sienna 
130 : silver 
131 : skyblue 
132 : slateblue 
133 : slategray 
134 : slategrey 
135 : snow 
136 : springgreen 
137 : steelblue 
138 : tan 
139 : teal 
140 : thistle 
141 : tomato 
142 : turquoise 
143 : violet 
144 : wheat 
145 : white 
146 : whitesmoke 
147 : yellow 
148 : yellowgreen 

You can find a picture with the colors in the current file. 
## Language :

This script is in Python 3.7.3

## Prerequisites : 

The use of [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) is strongly recommended.
Please make sure run this script with the Phylo environment using for all programs of the GB_barcodes_project.


## Using the program : 

To use the program, you must be in the "CGB_program" directory and run the following command :

```
python CGB_program.py -bp <BIPARTITION_FILE>  -al <ALIGNMENT_LENGTH> -sc <SCALE> -gr <GRADUATION>
```

With the following arguments:


- *BIPARTITION_FILE* : The file in csv format containing the informations about the bipartition you want to color. 
- *GENOME_ALIGNMENT_LENGTH*: The length in nucleotides of the alignement used in the SWB program.

OPTIONNALS :

- *SCALE* : If you want a scale in your barcode set this argument to 1. The default value is 0.
- *GRADUATION* : If you set a scale define the graduation value for your scale . The default value is 4000.

##### Example of use : 

```
python CGB_program.py -bp cds2.csv -al 30100 -sc 1 -gr 4000
```
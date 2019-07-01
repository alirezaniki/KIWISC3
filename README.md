KIWISC3
------
A Bash code to link Seiscomp3 to KIWI tools for automatic (Online) source analysis.

New version of Source_Analysis with following features released:
1- Precedure for a quick approximation of Mw
2- 2 methods to execlude high-misfit data from inversion step2

Requirements
------------

- Seiscomp3, KIWI, Pyrocko, GMT 5 

Notes
-----

Create these directories in the KIWISC3 main directory:

1- GFDB = put your Greens Functions in this Folder

2- RESP = Put your Response files in this Folder

3- RESULTS/SUMMARY/Map_All (mkdir -p RESULTS/SUMMARY/Map_All)


- Set the Proper Paths in both main codes.

- You may need to alter the code (Source_Analysis lines 134 - 156) to define your own GFDB's in specific conditions.

- Response files must be stored in RESP.$NET.$STA.$LOC.$CHAN name format.

- Read the README file in RESULTS/SUMMARY/Map_All dir.

This Readme file is incomplete. Contact me for more details.


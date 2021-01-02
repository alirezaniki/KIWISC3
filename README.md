Publication
------------

Towards a regional, automated full moment tensor inversion for medium to large magnitude events in the Iranian plateau (doi: 10.1007/s10950-020-09967-8)

https://rdcu.be/b87AN

KIWISC3
------
A Bash code to link Seiscomp3 and KIWI tools for automatic (Online) source analysis.

New version of Source_Analysis code (2020,Feb 5) with following features released:

1- Procedure for a quick approximation of Mw before source analysis.

2- Two methods to execlude high-misfit data from inversion step2.

2-1 Omitting a range of High_Misfit data considering a minimum allowed number of traces for step2.

2-2 Keeping a range of best fitted data considering a minimum allowed number of traces for step 2 (default).


Requirements
------------

- Seiscomp3, KIWI, Pyrocko, GMT 5 

Notes
-----

- Create these directories in the KIWISC3 main directory:

1- GFDB = put your Greens Functions in this Folder

2- RESP = Put your Response files in this Folder

3- RESULTS/SUMMARY/Map_All (mkdir -p RESULTS/SUMMARY/Map_All)


- Set the Proper Paths in both main codes.

- You may need to alter the code (Source_Analysis lines 141 - 163) to define your own GFDB's in specific conditions.

- Response files must be stored in RESP.$NET.$STA.$LOC.$CHAN name format.

- Read the README file in RESULTS/SUMMARY/Map_All dir.

This Readme file is incomplete. Contact me for more details.

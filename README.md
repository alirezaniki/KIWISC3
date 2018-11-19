# KIWISC3
A Bash code to link Seiscomp3 and KIWI tools for automatic (Online) source analysis.

# Requirements

- Seiscomp3, KIWI, Pyrocko, Obspy, GMT 5 

# Notes

Create these directories in the KIWISC3 main directory:

1- GFDB = put your Greens Functions in this Folder

2- RESP = Put your Response files in this Folder

3- RESULTS

- Set the Proper Paths in both main codes.

- You may need to alter the code (Source_Analysis lines 28 - 48) to define your own GFDB's in specific conditions.

- Response files must be stored in RESP.$NET.$STA..$CHAN name format.

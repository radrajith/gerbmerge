# gerbmerge
A detailed explanation of how i used gerbmerge to combine multiple eagle board files for using with fusionpcb services.

I used gerbmerge as a way to bring down the cost of ordering pcb for a group of friends while taking ESE 323 - Modern prototying and PCB design class at Stony Brook University. 

*The gerbmerge code is not written by me. I am creating this to give a detailed tutorial on how to use it, and not go through the same process of looking all over internet. *

#What is Gerbmerge?
Since eagle cad design software has a limitation of 10cmx10cm board layout, multiple board cannot be combined together without upgrading to a paid version. To get around this limitation, We can combine the gerber files generated from the eagle and combine them rather than combining the board files. By combining the gerber files, we also avoid the hectic task of renaming all the components to have different names. (We combined boards of 10 people and checking each person's board for name conflict is an annoying and time consuming task). Gerbmerge is a software written in python that will combine multiple gerber files with the least area using algorithms to provide a one super board. 

# Downloading Python
Since gerbmerge is written in pythong, If you dont have python already installed, download it. At the time of this tutorial I was using python version 2.7
[python download link](https://www.python.org/downloads/)

#Downloading Gerbmerge

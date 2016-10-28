testestestest
# gerbmerge
A detailed explanation of how i used gerbmerge to combine multiple eagle board files for using with fusionpcb services.

I used gerbmerge as a way to bring down the cost of ordering pcb for a group of friends while taking ESE 323 - Modern prototying and PCB design class at Stony Brook University. 

*The gerbmerge code is written by ruggedcircuits.com. I am creating this to give a detailed tutorial on how to use it, and not go through the same process of looking all over internet. *

#What is Gerbmerge?
Since eagle cad design software has a limitation of 10cmx10cm board layout, multiple board cannot be combined together without upgrading to a paid version. To get around this limitation, We can combine the gerber files generated from the eagle and combine them rather than combining the board files. By combining the gerber files, we also avoid the hectic task of renaming all the components to have different names. (We combined boards of 10 people and checking each person's board for name conflict is an annoying and time consuming task). Gerbmerge is a software written in python that will combine multiple gerber files with the least area using algorithms to provide a one super board. 

# Downloading Python
Since gerbmerge is written in pythong, If you dont have python already installed, download it. At the time of this tutorial I was using python version 2.7
[python download link](https://www.python.org/downloads/)

#Downloading and Installing Gerbmerge
After installing python, go ahead and download gerbmerge file

[zip file link](https://github.com/radrajith/gerbmerge/blob/master/gerbmerge-master.zip)

or if you directly want to get it from the source i got it from [click here](https://github.com/unwireddevices/gerbmerge)

![github download](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/github%20source%20download.PNG?raw=true)

The instruction on unwireddevices github page are pretty good, follow  that to install it. If you are not comfortable with it, use the picture guided instruction to install gerbmerge on your computer. 
 
once the file is downloaded unzip it. 

go to where the file was unzipped, in this case the downloads folder. Go to the address bar and type 'cmd' (without quotes).
![openning command prompt](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/opening%20command%20line.png?raw=true)
The command line window will open up. 

Type 'python setup.py install', this command will install gerbmerge software on your computer. 
						
![installing gerbmerge](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/install.png?raw=true)

you can confirm weather gerbmerge has installed by going to the python2.7>Lib>site-packages and now you should see gerbmerge folder. 

![gerbmerge folder 1](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/gerbmerge_folder_1.png?raw=true)
![gerbmerge folder 2](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/germerge_folder_2.png?raw=true)

#Combining gerber files 

If you have not created the gerber files already, [refer here](https://radrajith.github.io/ESE_323_PCB_Design/) for the instructions to obtain the gerber files from eagle. 
make sure the drills files are saved as .txt not .drd

##Creating directory for files to be combined
To avoid problems with python not being able to find directory, all the files will be placed in the python2.7 directory. Follow the steps below
 
* create a new directory called project_files
[project_files](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/projectfiles.png?raw=true)
* create a new folder for each gerber file you want to combine. For instance, create folders called raj, frank, jerey.  (the names you enter for the folder here will be the name that are used by the program to combine the files)
[all files](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/multiple_folders.png?raw=true)
*put all the files that are generated by the cam job and place it under each folder. For instance the cam job files of each person was assigned to their respective folders
**confirm if all these files are inside the folder - .bor,.GBL,.GBO,.GBP,.GBS,.GML,.GTL,.GTO,.GTP,.GTS,.TXT
[cam files](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/camfiles.png?raw=true)

##Creating configuration file
Download the configuration file from [here](https://github.com/radrajith/gerbmerge/blob/master/file.cfg)

open the configuration file (file.cfg) in any text editor, i used notepad++. 

###Carefully follow the instructions below and modify the **file.cfg** file. **And remember the '#' symbol is used to indicate comments in the code.** 
*Look for these lines* 
```
# Change projdir to wherever your project files are, for example:
#
#   projdir = project_files
#
# or relative pathname from where you are running GerbMerge
#
#   projdir = testdata
#
# or if all files are in the current directory (as in this example):
#
#   projdir = .
projdir = project_files

# For convenience, this is the base name of the merged output files.
MergeOut = merge
```
*If you named your folder something else other than 'project_files', change it to the appropriate name.
*The output file after running the gerbmerge will output the files with the name merge, feel free to change that to whatever name you want. 

*Scroll down all the way to bottom, and then copy the below code for as many files you want to combine. In my case I had 10 different gerber files to merge, so i copy pasted the below code 10 times. 
```[raj]

# You can set any options you like to make generating filenames easier, like
# Prefix. This is just a helper option, not a reserved name. Note, however,
# that you must write %(prefix)s below, in ALL LOWERCASE.
#
# Note how we are making use of the 'projdir' string defined way up at the top
# in the [DEFAULT] section to save some typing. By setting 'projdir=somedir'
# the expression '%(projdir)s/proj1' expands to 'somedir/proj1'.
Prefix=%(projdir)s/raj/Final Project Designs_v1

# List all the layers that participate in this job. Required layers are Drills
# and BoardOutline and have no '*' at the beginning.  Optional layers have
# names chosen by you and begin with '*'. You should choose consistent layer
# names across all jobs.
*TopLayer=%(prefix)s.GTL
*BottomLayer=%(prefix)s.GBL
*TopSilkscreen=%(prefix)s.GTO
*BottomSilkscreen=%(prefix)s.GBO
*TopSoldermask=%(prefix)s.GTS
*BottomSoldermask=%(prefix)s.GBS
Drills=%(prefix)s.TXT
BoardOutline=%(prefix)s.BOR

# If this job does not have drill tool sizes embedded in the Excellon file, it
# needs to have a separate tool list file that maps tool names (e.g., 'T01') to
# tool diameter. This may be the global tool list specified in the [Options]
# section with the ToolList parameter. If this job doesn't have embedded tool
# sizes, and uses a different tool list than the global one, you can specify it
# here.
#ToolList=proj1.drl

# If this job has a different ExcellonDecimals setting than the global setting
# in the [Options] section above, it can be overridden here.
ExcellonDecimals = 5
# You can set a 'Repeat' parameter for this job when using automatic placement
# (i.e., no *.def file) to indicate how many times this job should appear in
# the final panel. When using manual placement, this option is ignored.
Repeat = 1

################################################################
```
*change the name from 'raj' to whatever name you have for the folder. 
![name](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/name.PNG?raw=true)

*change the name of the gerber file name from 'Final Project Designs_v1' to whatever name you have for the gerber file. 
![foldername](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/foldername.PNG?raw=true)

once the above changes have been made, save the file and place it in the python2.7 folder(same location where 'project_files' folder is located)

#Running the Gerbmerge program. 
go to the python2.7 folder if you are not already there. Open up the command window from within the folder. 
[openning command line](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/opening%20command%20line.png?raw=true)

after openning the command prompt, type in 'gerbmerge file.cfg' and press enter
[gerbmerge run](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/entering%20cmd%20command.png?raw=true)

the following lines will be displayed, type 'y' and press enter.
[cmd 1](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/entering%20command%202.png?raw=true)
[cmd 2](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/entering%20command%203.png?raw=true)
the program will run forever trying to find the best placement to minimized the space required. I usually let it run for 20-30s before pressing ctrl-c to stop the process and output the files. 
[cmd 3](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/entering%20command%204.png?raw=true)
[cmd 4](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/entering%20command%205.png?raw=true)




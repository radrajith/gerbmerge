# Gerbmerge
A detailed explanation of how I used gerbmerge to combine multiple eagle boards for [fusionpcb](https://www.seeedstudio.com/fusion_pcb.html) manufacturing.

Softare Notes: 
* [Eagle7.6](https://cadsoft.io/) - CAM file format(s) 
	* Gerber_RS274X  
	* Excellion for drill holes
* [Python](https://www.python.org/downloads/)
	* Python 2.4 or higher
	* **Not Python 3, it is incompatible with gerbmerge**
* [SimpleParse](http://simpleparse.sourceforge.net/)
	* version 2.1.0 or later	
	

I used gerbmerge as a way to bring down the cost of ordering pcb for a group of friends while taking ESE 323 - Modern prototying and PCB design class at Stony Brook University. 

*The gerbmerge code is written by ruggedcircuits.com. I am creating this to give a detailed tutorial on how to use it, and not go through the same process of looking all over internet.*

#What is Gerbmerge?
Gerbmerge is software written in python that will combine multiple gerber files into one super board. Gerbmerge offers both manual and automatic (optimization algorithms) as means of board placement.

For this project, the automatic operation was used.

#Why Gerbmerge?
Because eagle cad design software has a limitation of 100x80mm routing area (express) or 160x100mm routing area(edu) , multiple boards cannot be combined together without requiring to upgrade a paid version. To work around this limitation, we can combine the gerber files generated from the eagle instead. By combining the gerber files, we also avoid the problems caused by the panelizing script which redefines all the components to different names. (We combined boards of 10 people and checking each person's board for name conflict is an annoying and time consuming task).

# Downloading Python And Simpleparse
Since gerbmerge is written in python, If you don't have python already installed, download it. At the time of this tutorial I was using python version 2.7
[python download link](https://www.python.org/downloads/)

>SimpleParse is a BSD-licensed Python package providing a simple and fast parser generator using a modified version of the mxTextTools >text-tagging engine.

[SimpleParse download link](http://simpleparse.sourceforge.net/)

#Downloading and Installing Gerbmerge
After installing python, go ahead and download gerbmerge file [zip file link](https://github.com/radrajith/gerbmerge/blob/master/gerbmerge-master.zip)

Or if you directly want to get it from the source I forked it from [click here](https://github.com/unwireddevices/gerbmerge).

![github download](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/github%20source%20download.PNG?raw=true)

The instruction on unwireddevices github page are pretty good, follow that to install it. If you are not comfortable with it, use the picture guided instruction to install gerbmerge on your computer. 
 
Once the file is downloaded unzip it. 

Go to where the folder containing unzipped files (in this case the downloads folder). Run command prompt by going to the address bar and typing ```cmd``` .
![openning command prompt](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/opening%20command%20line.png?raw=true)

The command line window will open up. 
Typing ```python setup.py install```, will install gerbmerge software on your computer. 
						
![installing gerbmerge](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/install.png?raw=true)

You can check if gerbmerge was installed correctly by going to "python2.7>Lib>site-packages" (see gerbmerge folder). 

![gerbmerge folder 2](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/germerge_folder_2.png?raw=true)

#Combining Gerber Files 

If you have not created the gerber files already, [refer here](https://radrajith.github.io/ESE_323_PCB_Design/) for the instructions to obtain the gerber files from eagle. 
**Confirm that the drills file extensions are saved as .txt not .drd**

##Creating Directory for Files to be Combined
To avoid problems with python not being able to find directory, all the files will be placed in the python2.7 directory. Follow the steps below
 
* Create a new directory called ```project_files```
![project_files](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/projectfiles.png?raw=true)

* Create a new folder for each gerber file you want to combine. For instance, create folders called A, B, C, etc. (the names used for the folders here, will be the same names that will be used by the program to combine the files)
![all files](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/multiple_folders.png?raw=true)
* Place CAM files into each respective folder. For instance, place the CAM job files of each assigned person to their respective folders

* Check if all these files are each folder inside the folder - **.BOR,.GBL,.GBO,.GBP,.GBS,.GML,.GTL,.GTO,.GTP,.GTS,.TXT** (11)
![cam files](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/camfiles.png?raw=true)
*Failure to do so will result in an error.*

##Creating Configuration File
Download the configuration file from [here](https://github.com/radrajith/gerbmerge/blob/master/file.cfg)

Then open the configuration file (file.cfg) in any text editor, I used [notepad++](https://notepad-plus-plus.org/download/v7.1.html). 

###Carefully follow the instructions below and modify the ```**file.cfg**``` . **Note the '#' symbol is used to indicate comments in the code.** 
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
*If you named your folder something else other than 'project_files', change it to the appropriate name.*

The output file(s) after running gerbmerge will all be named merge(.extension), feel free to rename it to whatever you want. 

If you want to change the spacing between the each boards, modify this x and y spacing
![xyspacing](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/xyspacing.PNG?raw=true)

Next, scroll down all the way to bottom, and then copy the code below for as many boards you want to combine. (In my case I had 10 different gerber files to merge, so I copy pasted the below code 10 times.) 
```
[raj]

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
* Correct the lines, ```[raj]``` and ```Prefix=%(projdir)s/raj/Final Project Designs_v1``` to correspond whatever folder/names are being used. See:
![foldername](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/foldername.PNG?raw=true)

Once the above changes have been made, save the file and place it in the python2.7 folder(same location where 'project_files' folder is located).

#Running the Gerbmerge Program. 
Go to the python2.7 folder if you are not already there. Once again open up the command window from within the folder by going to the address bar and typing ```cmd```. 
![openning command line](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/opening%20command%20line.png?raw=true)

After openning the command prompt, type in ```gerbmerge file.cfg``` and press enter.
![gerbmerge run](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/entering%20cmd%20command.png?raw=true)

The following lines will be displayed, type ```y``` and press enter.
![cmd 1](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/entering%20command%202.png?raw=true)
![cmd 2](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/entering%20command%203.png?raw=true)
The program will then run forever trying to find the best placement to minimized the space required. I usually let it run for 20-30s before pressing ctrl-c to stop the process and output the files. 
![cmd 3](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/entering%20command%204.png?raw=true)
![cmd 4](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/entering%20command%205.png?raw=true)
Now you should see the all the files with merge2.(extension) generated in the python2.7 folder. 
![mergefiles](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/mergedFiles.png?raw=true)

Since I am using seeedstudio's fusionpcb manufacturing service, I will now have to modify the drill file to meet their specification(s). The drill file output and the .fab file output do not meet their requirements, for this reason the program ```drillfix.py``` program was written/used. This program will be used to automatically correct the drill file to meet the specifications.

#How to Use Drillfix.py 
* Download the ``drillfix.py`` from [here](https://github.com/radrajith/gerbmerge/raw/master/ese323_drillfix.py). save it to the python2.7 folder.
* Open command prompt on this folder and type in ``python drillfix.py`` and press enter.
![drillfix](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/drillfix.png?raw=true)

Now there will be file called merge2_corrected.txt file. 
![merge2corrected](https://github.com/radrajith/gerbmerge/blob/master/tutorial%20pics/mergecorrect.png?raw=true)

* delete the merge2.TXT file
* rename the merge2_corrected.TXT file to merge2.TXT
* rename the merge2.fab to merge2.GML

All the files are now ready.

#Uploading to Fusionpcb
Copy **.GML, .GBL, .GBS, .GBO, . GTL, .GTO, .GTS, .TXT** (8) files in a folder and create a zip file of it. 

Open your browser, go to [fusion pcb](https://www.seeedstudio.com/new-fusion-pcb.html) (if the link is dead, search for fusionpcb services) and upload this zip file. Click gerber view and now you should be able to see all the layers of the superboard (all gerber files merged).


#Errors
##RuntimeError: only 26 different tool sizes supported for fabrication drawing
This error occurs when the combined files resulted in than 26 distinct drill hole sizes. (26 is number set by config/manufacturer) 
![drillhole error](https://github.com/radrajith/gerbmerge/blob/master/tutorial%2520pics/error1drill.PNG?raw=true)

###Solution
* This problem can be fixed by rounding up the least used drill sizes to lessen the number of different sized drills. First, open the drill file, in our case ```merge2.txt``` file to find:
```
T01C0.012000
T02C0.023810
T03C0.025590
...
T23C0.078740
T24C0.086610
T25C0.089000
T26C0.125980
```
Here we have 26 different sizes here (T01-T26). The number after the ``.`` is the drill/hole size(inches). Example, "T02C0.023810" would be refered to as drill 2 of size .23810 inches. **Note that drill sizes here refer to all types of holes (through-holes, vias, and etc. Not just screw-holes)**.

Next, look through the drill file ```merge2.txt``` to determine which drills were least used. 
As an example see:
```
T16
X773340Y516260
X783340Y516260
T17
X989010Y458590
X989010Y510320
T18
X184410Y50670
X164720Y51220
X164720Y11220
X184410Y10670
X161560Y374840
X181560Y374840
X181930Y253050
X161930Y253050
X960390Y436190
X1000390Y436190
X1000780Y577330
X960780Y577330
T19
X360830Y106220
X360040Y78270
X400040Y78270
X400830Y106220
X557310Y135730
X557070Y172150
X597070Y172150
X597310Y135730
X342330Y583940
X382330Y583940
X381740Y491460
X341740Y491460
X493220Y469130
X493220Y449450
X563300Y449450
X563300Y469130
```
Drill sizes T16(2 drills) and T17(2 drills) are not used as much relative to T18(12 drills) or T19(15) drills. 

Locate them through Eagle's board-view to resize to next biggest size listed in drill file /```merge2.txt```. Fix them on the board and rerun the whole process. If you have trouble locating the drill/through holes/vias, make a copy of the drill file isolating the least used drills. Then load that copy onto a gerber viewer to visually see which drill holes/vias needs fixing.

##ImportError: No module named simpleparse.parser
>SimpleParse is a BSD-licensed Python package providing a simple and fast parser generator using a modified version of the mxTextTools >text-tagging engine.

[SimpleParse download link](http://simpleparse.sourceforge.net/)

##SyntaxError: Missing parentheses in call to 'print'
Are you using python 3 and up? Try again with python 2.7

--frankie finish the rest, talk about kawing program and how it helped find which board has used weird values and how we used the drill hits(one of the pics i uploaded should have the drill hits view).




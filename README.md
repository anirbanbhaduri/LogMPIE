# LogMPIE
QIIME and MOTHUR

There are many sophisticated pipelines and tools available to analyse the 16S rRNA data. Among them, QIIME (Quantitative Insights into Microbial Ecology) and MOTHUR are few of the established pipelines available.These open source softwares can be downloaded from their respective sites. QIIME and MOTHUR differ in many ways from their installation to development strategy, languages used in softwares, methods or functions used, their accessibility, their functioning, result visualization, database used and the time required for the process. So at end a comparison can be done according to pipeline used.

QIIME installation:
QIIME requires lot of dependencies so its installation can be little challenging. According to the online tutorials, it can be installed in many ways like building virtual machines or with minimum base installation or at end the complete installation which is most challenging among these three as it needs lot of external dependencies like Python, Numpy, PyCogent, biom-format, PyNast, uclust, greengene datafile, fasttree, usearch, blast, cd-hit etc.The following link explains the detailed installation of QIIME:
http://qiime.org/1.9.0/install/install.html. 
After installing QIIME, you can test its installation by following command: print_qiime_config.py -tf. If output shows no error that means the software is properly installed in the system. Now you can run QIIME. 

MOTHUR installation:
There are many links available online to download and install MOTHUR on the system. This software can be easily downloaded from the following link : https://github.com/mothur/mothur/releases/tag/v1.40.5. Its installation is easy as it needs less dependencies and mostly are pre-installed in the system. After downloading, decompress it and run the command "make" to build necessary environment. At the end "./mothur" executes the package without any error. You can also add path by editing .bashrc and addding following command to it: PATH=~/path_to_mothur_binary_folder:${path}. Add your real path in place of path_to_mothur_binary_folder.



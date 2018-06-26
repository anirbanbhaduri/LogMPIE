# LogMPIE
Microbiome Processing Pipeline

The pipeline is a combination of python scripts which process the 16S rRNA data through two different bioinformatics pipelines, QIIME and MOTHUR. The script "Main.py" demands user to input the tool he/she requires for their data analysis and then accordingly it will call QIIME (Qiime.py) or MOTHUR (Mothur.py).

QIIME (Quantitative Insights into Microbial Ecology) requires lot of dependencies. It can be installed through following link: http://qiime.org/1.9.0/install/install.html. 
MOTHUR can be easily downloaded from the following link : https://github.com/mothur/mothur/releases/tag/v1.40.5. 
Please make sure that you follow the proper license terms before downloading these softwares. These two come under GNU GENERAL PUBLIC LICENSE.
The scripts will run only if both softwares are properly installed and configured in the system. 

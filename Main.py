#!/usr/bin/env python
import numpy as np
import pandas as pd
import os
import glob
import subprocess
print "**PLACE ALL YOUR RAW FASTQ FILES AT ONE PLACE IN A FOLDER FOR ANALYSIS.**"
print("Select one of the Analysis pipeline. MOTHUR takes much longer time for analyis then QIIME so select options accordingly. ")
print("1.QIIME")
print("2.MOTHUR")
choice = int(input("Enter choice(1/2/):"))
if choice == 1:
	subprocess.call(['python', 'Qiime.py'])
if choice == 2:
	subprocess.call(['python', 'Mothur.py'])

	
	
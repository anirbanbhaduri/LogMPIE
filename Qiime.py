#!/usr/bin/env python
import numpy as np
import pandas as pd
import os
import glob

user_input1 = raw_input("Enter the path of your raw data: ")
rootdir = user_input1


user_input2 = raw_input("Enter the path for your results: ")
rootdir1 = user_input2


user_input3= raw_input("Enter the quality score for scanning FASTQ files: ") or 27
quality = user_input3


user_input4= raw_input("Enter the Reference FASTA file name with its precise location:  ")
file1 = user_input4

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		os.system("pwd")
        	str0 = rootdir+file
        	file_id = file.replace('.fastq','')
        	file_id = file_id.replace('_', '.')
        	slout_input = "slout" + file_id + '/'
        	otus_input  = "otus" + file_id + '/'
        	table_input = "table" + file_id + '.txt'
        	os.system("split_libraries_fastq.py -i %s"%str0 + " --sample_ids %s"%file_id + " -o %s"%slout_input + " -q %s"%quality + " --barcode_type 'not-barcoded'  --phred_offset 33")
        	os.system("pick_closed_reference_otus.py -i %s"%(rootdir1+slout_input) + "seqs.fna  -r %s"%file1 + " -o %s"%otus_input)
        	str1 = "biom convert -i  %s"%(rootdir1+otus_input) + "otu_table.biom -o %s"%(rootdir1+table_input) + "--to-tsv --header-key taxonomy"
        	os.system("biom convert -i  %s"%(rootdir1+otus_input) + "otu_table.biom -o %s"%(rootdir1+table_input) + " --to-tsv --header-key taxonomy")

		path = r'rootdir1'
		allFiles = glob.glob(path + "/*.txt")
		for f in allFiles:
			df = pd.read_csv(f,delimiter="\t", header=None)    
    			print f
			

















			
		


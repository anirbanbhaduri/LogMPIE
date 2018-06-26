#!/usr/bin/env python
import os
from subprocess import call

user_input1 = raw_input("Enter the path of your input data directory: ")
rootdir=user_input1
print rootdir


user_input2= raw_input("Enter the name of Reference FASTA file with its precise location:  ")
file1 = user_input2

user_input3 = raw_input("Enter the name of Taxonomy file with its precise location:  ")
file2 = user_input3


for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		os.system("pwd")
        	str0 = rootdir+file
		file_id = file.replace('.fastq','')
        	file_id = file_id.replace('_', '.')
        	slout_input = file_id + '.fasta'
        	call(["mothur", "#fastq.info(fastq=%s)" % str0])
		os.system("cat " + (rootdir+slout_input) + "  >> merge.fasta")
		call(["mothur", "#unique.seqs(fasta=merge.fasta)"])
		call(["mothur", "#count.seqs(name=merge.names)"])
		call(["mothur", "#align.seqs(fasta=merge.unique.fasta, reference= %s"%file1 + ", processors= 8)"])
		call(["mothur", "#filter.seqs(fasta=merge.unique.align, vertical=T, processors= 8)"])
                call(["mothur", "#classify.seqs(fasta=merge.unique.filter.fasta, reference= %s"%file1 + ", taxonomy= %s"%file2 + ", cutoff=95, method=bayesian, processors= 8)"])
		call(["mothur", "#cluster.split(fasta=merge.unique.filter.fasta, count=merge.count_table, taxonomy=merge.unique.filter.silva.bayesian.taxonomy, splitmethod=classify, taxlevel=3, cutoff= 0.8)"])
		call(["mothur", "#classify.otu(list=merge.unique.filter.opti_mcc.list, count=merge.count_table, taxonomy=merge.unique.filter.silva.bayesian.taxonomy)"])























#for filename in os.listdir(rootdir):
#	#print filename
#	call(["mothur", "#fastq.info(fastq=%s)" % filename])
#	os.system("cat " + '.fasta' + " >> merge.fasta")
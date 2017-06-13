#! /bin/python3.4
import sys
import argparse
import random	

def generateDNA(dna_len):
	nucl_list=['A','C','G','T']
	dna_list={}
	for i in range(0,dna_len):
		dna_id = random.randint(1,len(dna_list))
		#append random generated nucleotide
		dna_list=dna_list.append(nucl_list[dna_id]) 
	#joint the sequencing
	dna_list=''.join(dna_list)
	return outputFASTA(dna_list)

def outputFASTA(dnaseq):
	print('>myrandomsequence \n', dnaseq)

def printDNA():
	return 



if __name__ == '__main__':
	
	seq_len = int(input('Enter the sequence length:  '))
	generateDNA(seq_len)
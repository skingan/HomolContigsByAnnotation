#!/usr/bin/env python

# Sarah B. Kingan
# 19 August 2016
# 
# Pacific Biosciences
# Applications Lab

###########################################################################################################

# import libraries
from argparse import ArgumentParser
import csv

###########################################################################################################

# define command line arguments, program description, and help
desc ='''Identify pairs of contigs that share one or or more annotated genes.
	These contigs may represent homologous genomic regions with divergent haplotypes.'''
parser = ArgumentParser(description=desc)
parser.add_argument("GeneBed", help="bed file with gene spans")
parser.add_argument("ContigLengths", help="tab-delimited text with contigName contigLength")
args = parser.parse_args()


###########################################################################################################

# get filenames
BED_file = args.GeneBed
Len_file = args.ContigLengths

###########################################################################################################

# define functions

def BED2Dict(bed_file):
# import BED data into dict
# key = contigID
# value = list of gene IDs  
	my_dict= {}
	with open(bed_file, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		for row in reader:
			if (row[0] in my_dict):
				my_dict[row[0]].append(row[4]) 
			else:
				my_dict[row[0]] = [row[4]]
	return my_dict

def Len2Dict(length_file):
# key = contigID
# value = contigLength  
        my_dict= {}
        with open(length_file, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter='\t')
                for row in reader:
			my_dict[row[0]] = row[1]
        return my_dict




def intersection(list1, list2):
# find intersection between two gene lists
	return set(list1).intersection(list2)


###########################################################################################################

# program body

# make dictionary of BED file data and contig length data
contigGene_dict = BED2Dict(BED_file)
contigLength_dict = Len2Dict(Len_file)

# print header
header = ['Contig1', 'Contig2', 'Length1', 'Length2', 'N_shared_genes', 'gene_IDs']
print '\t'.join(str(h) for h in header)

# pairwise comparison of all contigs
contigID_list = contigGene_dict.keys()
for i in range(len(contigID_list)):
	for j in range(i):
		sharedGenes = list(intersection(contigGene_dict[contigID_list[i]],contigGene_dict[contigID_list[j]]))
		if len(sharedGenes) > 0:
			length1 = 'NA'
			length2 = 'NA'
			if contigLength_dict[contigID_list[i]]:
				length1 = contigLength_dict[contigID_list[i]]
			if contigLength_dict[contigID_list[j]]:
                                length2 = contigLength_dict[contigID_list[j]]
			if int(length1) > int(length2):
				output = [contigID_list[i], contigID_list[j], length1, length2]
                        if int(length2) > int(length1):
                                output = [contigID_list[j], contigID_list[i], length2, length1]
			output.extend([len(sharedGenes), ",".join(str(g) for g in sharedGenes)])
			print '\t'.join(str(o) for o in output)	




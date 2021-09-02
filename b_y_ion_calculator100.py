#!/usr/bin/python
#NKS code for b_y_ion_calculator
#06/08/2019
import csv
import re
from pyteomics import mzid, auxiliary
import timeit
import subprocess
import sys
#b/y ion calculate

time_diff = open('time_difference_100.txt','w')

t = timeit.default_timer()
time_diff.write('for 100 peptide')
time_diff.write('\n')
t0 = str(t)
time_diff.write(t0)
time_diff.write('\n')

print("start_time_in second=",t)

pepseq = open('peptide_seq_100.txt')
resultfile = open('peptide_seq_100_b_y_ion.txt','w')

for pepseq1 in pepseq:
	resultfile.write(pepseq1)
	peptideseqseq = pepseq1.rstrip()
	H =  float('1.0078250')
	H2O = float('18.01057') #	18.01057,	18.02
	PROTON = float('1.00728')
	firstaminoacide = peptideseqseq[:1]
	lastaminoacide = peptideseqseq[-1:]
	#weights = {'A': 71.0779, 'C': 103.13802, 'D': 115.08782, 'E': 129.1147,'F': 147.17578,'G': 57.05114, 'H': 137.1403, 'I': 113.15886, 'K': 128.1733, 'L': 113.15866,'M': 131.19178, 'N': 114.1035, 'P': 97.1159,'Q': 128.12994, 'R': 156.1867,'S': 87.07742, 'T': 101.1043, 'V': 99.13178, 'W': 186.21242, 'Y': 163.17518}
	#monoisotopic waight
	weights = {'A': 71.037114, 'C': 103.00919	, 'D': 115.02694, 'E': 129.04259,'F': 147.06841,'G': 57.021464, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406,'M': 131.04048, 'N': 114.04293	, 'P': 97.052764,'Q': 128.05858, 'R': 156.10111,'S': 87.032029, 'T': 101.04768, 'V': 99.068414, 'W': 186.07931, 'Y': 163.06333}

	lists= []
	sumofseq = float('1.0081')
	
	weight = sum(weights[p] for p in peptideseqseq)
	

	b_ion_first_amino_acide_weight = weights[firstaminoacide] +H
	#print('b_ion_first_amino_acide_weight',b_ion_first_amino_acide_weight)
	b_ion_mass_total_mass = weight+H
	#print('b_ion_mass_total_mass = ',b_ion_mass_total_mass)

	y_ion_last_amino_acide_weight = weights[lastaminoacide] + H2O + H
	#print('y_ion_last_amino_acide_weight', y_ion_last_amino_acide_weight)

	y_ion_first_amino_acide_weight = b_ion_mass_total_mass + H2O 
	#print('y_ion_first_amino_acide_weight', y_ion_first_amino_acide_weight)


	for q in peptideseqseq:
		aminoacidemass =float(weights[q])
		sumofseq = sumofseq+aminoacidemass
		sumofseq = format(sumofseq)
		lists.append(sumofseq)
		sumofseq = float(sumofseq)
	print('lists',lists)
	lists1 = str(lists)
	resultfile.write(lists1)

	lists.reverse() 
	z = y_ion_first_amino_acide_weight
	#print(z)

	revlist = []
	revlist.append(z)
	minuofseq1 = float('0')
	minuofseq = z
	for rev in peptideseqseq:
		aminoacidemass1 =float(weights[rev])
		minuofseq = minuofseq- aminoacidemass1
		minuofseq = format(minuofseq)
		revlist.append(minuofseq)
		minuofseq = float(minuofseq)
	revlist1 = revlist.pop()
	print('revlist',revlist)
	revlist1 = str(revlist)
	resultfile.write(revlist1)
	resultfile.write('\n')



t1 = timeit.default_timer()
t11 = str(t1)
time_diff.write(t11)
time_diff.write('\n')
print("end_time_in second=",t1)
print('total time = ', t1-t)
time_diff_for_100 = t1-t
time_diff_for_100 = str(time_diff_for_100)
time_diff.write('time_diff_for_100')
time_diff.write('\n')
time_diff.write(time_diff_for_100)
time_diff.write('\n')

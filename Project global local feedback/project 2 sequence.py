# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:04:18 2023

@author: Zirui Zhang
"""
import random
#sequence design: 4 sequences(2x tpye1 + 2 x type2) with 4 mapping trials (2x target + 1 sround + 1 border)

stim_list_full = ['full','near_noise', 'near']
stim_list_occ = ['3/4 image', 'near_noise', 'near']
sequence_list = ["t1","t1", "t2", "t2"]
mapping_list = ['tar_1', 'tar_2', 'sround', 'border']
random.shuffle(mapping_list)
random.shuffle(sequence_list)
random.shuffle(stim_list_full)
random.shuffle(stim_list_occ) 

for i in mapping_list:
    poi = int(mapping_list.index(i))*2 + 1
    sequence_list.insert(poi, i) # insert one mapping trial after each sequence 
print(sequence_list)
    
for trial in sequence_list:
    if trial == 't1':
        for i in stim_list_full:
            if i == 'full':
                print('full')
            if i == 'near_noise':
                print('near_noise')
            if i == 'near':
                print('near')
    if trial == 't2':
        for i in stim_list_occ:
            if i == '3/4 image':
                print('3/4 image')
            if i == 'near_noise':
                print('near_noise')
            if i == 'near':
                print('near')
    if trial == 'tar_1':
        print ('tar')
    if trial == 'tar_2':
        print ('tar')
    if trial == 'sround':
        print('sround')
    if trial == 'border':
        print("border")


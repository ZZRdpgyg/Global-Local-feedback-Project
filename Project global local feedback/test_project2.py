#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:47:53 2023

@author: zhangzirui
"""

from psychopy import visual, core, event, gui
#import os
import numpy as np
import random
from datetime import datetime
import timeit


data = {}
data['expname'] = 'my test experiment'
data['participantid'] = ''
data['gender']=''
data['expdate'] = datetime.now().strftime('%Y%m%d_%H%M')
dlg = gui.DlgFromDict(data, title='Input data', fixed = ['expname','expdate'],order = ['expname','expdate','participantid','gender'])
if not dlg.OK:
    print ('User cancelled the experiment')
    core.quit() 
print(data) 
filename = 'part_{}_{}.csv'.format(data['participantid'],data['expdate'])   
stim_path = '/Users/zhangzirui/Desktop/Pictures/'
#.................

mm = np.array([[-1,-1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], 
               [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])

mc = np.array([[-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
               [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], 
               [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], 
               [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], 
               [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])
win = visual.Window([1024,768],fullscr=False, allowGUI=True, units='pix', color= (0,0,0))
cross = visual.TextStim(win, '+', color=(1.0,1.0,1.0),pos=(0,0))#white cross
cros_r = visual.TextStim(win, '+', color=(1,-1,-1), pos= (0,0)) #red cross
induct = visual.TextStim(win, text= 'welcome to our experiment', pos = (0,0))
ending = visual.TextStim(win,text = 'The end Thank you', pos= (0,0))

occluder_white   = visual.ShapeStim(win, vertices=[[0, 0], [400, 0], [400, -300], [0, -300]], lineColor = 'white', fillColor = 'white', units='pix')

occ = visual.ImageStim(win, stim_path + 'AAA.png', size = (800,600), pos = (0,0),units = 'pix')
#occ_ = visual.ImageStim(win, stim_path + '27-occluded-images/Gist_bw-{}png'.format(i), size = (800,600), mask=mm,pos = (0,0),units = 'pix')





induct.draw()

#cross.draw()
win.flip()
core.wait(2)



#........................main experiment........................


stim_list = [1,2,3,4,5,6]
noise_list = [i for i in range (2,17)]
random.shuffle(noise_list)


for i in stim_list:
    if i ==1:
        con_1 = visual.TextStim(win, text= 'Image with occluder', pos = (0,0))
        con_1.draw()
        win.flip()
        core.wait(2)
        
        for i in range(15):
            occ.draw()
            occluder_white.draw()
            cross.draw()
            win.flip()
            core.wait(0.2)
            cross.draw()
            win.flip()
            core.wait(0.2)
        
        cross.draw()
        win.flip()
        core.wait(3)
    if i == 2:
        con_2 = visual.TextStim(win, text= 'Full Image', pos = (0,0))
        con_2.draw()
        win.flip()
        core.wait(2)
        for i in range(15):
            occ.draw()
            cross.draw()
            win.flip()
            core.wait(0.2)
            cross.draw()
            win.flip()
            core.wait(0.2)
        
        cross.draw()
        win.flip()
        core.wait(3)
    if i == 3:
        con_2 = visual.TextStim(win, text= 'Far + noise', pos = (0,0))
        con_2.draw()
        win.flip()
        core.wait(2)
        for i in noise_list:
            noise_img = visual.ImageStim(win, stim_path + '27-occluded-images/Gist_bw-{}.png'.format(i), size = (800,600), mask=mm,pos = (0,0),units = 'pix')
            occ.draw()
            noise_img.draw()
            occluder_white.draw()
            cross.draw()
            win.flip()
            core.wait(0.2)
            cross.draw()
            win.flip()
            core.wait(0.2)
        
        cross.draw()
        win.flip()
        core.wait(3)
    if i == 4:
        con_2 = visual.TextStim(win, text= 'Near + noise', pos = (0,0))
        con_2.draw()
        win.flip()
        core.wait(2)
        for i in noise_list:
            noise_img = visual.ImageStim(win, stim_path + '27-occluded-images/Gist_bw-{}.png'.format(i), size = (800,600),pos = (0,0),units = 'pix')
            occ_ = visual.ImageStim(win, stim_path + 'AAA.png', size = (800,600), mask=mm,pos = (0,0),units = 'pix')
            
            noise_img.draw()
            occ_.draw()
            occluder_white.draw()
            cross.draw()
            win.flip()
            core.wait(0.2)
            cross.draw()
            win.flip()
            core.wait(0.2)
    if i ==5:
        con_1 = visual.TextStim(win, text= 'Near', pos = (0,0))
        con_1.draw()
        win.flip()
        core.wait(2)
        occ_ = visual.ImageStim(win, stim_path + 'AAA.png', size = (800,600), mask=mm,pos = (0,0),units = 'pix')
        for i in range(15):    
            occ_.draw()
            occluder_white.draw()
            cross.draw()
            win.flip()
            core.wait(0.2)
            cross.draw()
            win.flip()
            core.wait(0.2)
    if i ==6:
        con_1 = visual.TextStim(win, text= 'Far', pos = (0,0))
        con_1.draw()
        win.flip()
        core.wait(2)
        occluder = visual.ImageStim(win, stim_path + 'grey.png', size = (800,600), mask=mm,pos = (0,0),units = 'pix')

        for i in range(15):
            occ.draw()
            occluder.draw()
            occluder_white.draw()
            cross.draw()
            win.flip()
            core.wait(0.2)
            cross.draw()
            win.flip()
            core.wait(0.2)
        cross.draw()
        win.flip()
        core.wait(3)
        cross.draw()
        win.flip()
        core.wait(3)
        
            
        
        



win.close()        






























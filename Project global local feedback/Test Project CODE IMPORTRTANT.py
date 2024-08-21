from psychopy import visual, core, event, gui
#import os
import numpy as np
import random
from datetime import datetime
import timeit

data = {}
data['expname'] = 'Near condition experiment'
data['participantid'] = ''
data['run']=''
data['expdate'] = datetime.now().strftime('%Y%m%d_%H%M')
dlg = gui.DlgFromDict(data, title='Input data', fixed = ['expname','expdate'],order = ['expname','expdate','participantid','run'])
if not dlg.OK:
    print ('User cancelled the experiment')
    core.quit() 
print(data) 
filename = 'part_{}_{}.csv'.format(data['participantid'],data['expdate'])   

path = './'
stim_path = path + 'stim/'
data_path = path + 'data/'
filename = '{}_{}.txt'.format(data['participantid'],data['expdate'])  
logFile = open(data_path + filename, 'w')
logFile.write('onset\tevent\n')
print('onset\tevent')


#0.58 for 50% : 50% contextual areas
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
               
## masks (we can use them instead of having different images for occluder and context)
mask_con = np.array([[ 1,-1],[ 1, 1]])
mask_occ = np.array([[-1, 1],[-1,-1]])
mask_bor = np.array([[-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])

win = visual.Window([1024,768],fullscr=False, allowGUI=True, units='pix', color= (0,0,0))
cross = visual.TextStim(win, '+', color=(1.0,1.0,1.0),pos=(0,0))#white cross
cros_r = visual.TextStim(win, '+', color=(1,-1,-1), pos= (0,0)) #red cross
cros_p = visual.TextStim(win, '+', color = (0, 0.5, 1), pos = (0,0)) #pink cross
induct = visual.TextStim(win, text= 'welcome to our experiment', pos = (0,0))
ending = visual.TextStim(win,text = 'The end Thank you', pos= (0,0))

occluder_white   = visual.ShapeStim(win, vertices=[[0, 0], [400, 0], [400, -300], [0, -300]], lineColor = 'white', fillColor = 'white', units='pix')
city = visual.ImageStim(win, stim_path + 'city.jpg', size = (800,600), pos = (0,0),units = 'pix')
factory = visual.ImageStim(win, stim_path + 'factory.jpg', size = (800,600), pos = (0,0),units = 'pix')
city_n = visual.ImageStim(win, stim_path + 'city.jpg', size = (800,600), pos = (0,0), mask = mm,units = 'pix')
factory_n = visual.ImageStim(win, stim_path + 'factory.jpg', size = (800,600), pos = (0,0), mask= mm, units = 'pix')
noise_img_1 = visual.ImageStim(win, stim_path + '24-occluded-images/Gist_bw-1.jpg', size = (800,600),pos = (0,0),units = 'pix') 
noise_img_2 = visual.ImageStim(win, stim_path + '24-occluded-images/Gist_bw-2.jpg', size = (800,600),pos = (0,0),units = 'pix') 
noise_img_3 = visual.ImageStim(win, stim_path + '24-occluded-images/Gist_bw-3.jpg', size = (800,600),pos = (0,0),units = 'pix') 
checkerocc_1 = visual.ImageStim(win, stim_path + 'checker1.bmp', size = (800,600), pos = (0,0),units = 'pix',mask = mask_occ)
checkerocc_2 = visual.ImageStim(win, stim_path + 'checker2.bmp', size = (800,600), pos = (0,0),units = 'pix', mask = mask_occ)
checkercon_1 = visual.ImageStim(win, stim_path + 'checker1.bmp', size = (800,600), pos = (0,0),units = 'pix',mask = mask_con)
checkercon_2 = visual.ImageStim(win, stim_path + 'checker2.bmp', size = (800,600), pos = (0,0),units = 'pix', mask = mask_con)
checkerbor_1 = visual.ImageStim(win, stim_path + 'checker1.bmp', size = (800,600), pos = (0,0),units = 'pix',mask = mask_bor)
checkerbor_2 = visual.ImageStim(win, stim_path + 'checker2.bmp', size = (800,600), pos = (0,0),units = 'pix', mask = mask_bor)

stim_list_full = ['city','fact','cityn_noise','factn_noise', 'city_n', 'fact_n'] #full image sequence 
stim_list_occ = ['city_occ','fact_occ','cityn_noise','factn_noise', 'city_n', 'fact_n']#occluded image sequence
sequence_list = ["t1","t1", "t2", "t2"] #sequence types
mapping_list = ['tar_1', 'tar_2', 'sround', 'border'] #mapping trials
noise_list = [i for i in range (1,4)]*10 #noise image list
fix_change = [3,4,5]
random.shuffle(mapping_list)
random.shuffle(sequence_list)
random.shuffle(stim_list_full)
random.shuffle(stim_list_occ) 


for i in mapping_list:
    poi = int(mapping_list.index(i))*2 + 1
    sequence_list.insert(poi, i) # insert one mapping trial after each sequence


def key_press_city():
    tim = int(round(timeit.default_timer() - start_t)*1000)
    if i in ['city', 'city_n', 'city_occ', 'cityn_noise']:
        print(tim, 'city_response')
        logFile.write(str(int((timeit.default_timer()-start_t)*1000)) + '\t' + 'city_rp' + '\n')
        

    
def key_press_factory():
    tim = int(round(timeit.default_timer() - start_t)*1000)
    if i in ['fact','fact_occ', 'factn_noise']:
        logFile.write(str(int((timeit.default_timer()-start_t)*1000)) + '\t' + 'factory_rp' + '\n')
        print(tim, 'factory_response')

def key_press_focus_task():
    tim = int(round(timeit.default_timer() - start_t)*1000)
    if task == 'response':
        print(tim, 'response')
    

def full(image):
    fix_c = random.choice(fix_change)
    for idx in range(6):
        if idx == fix_c:
            tim = int((timeit.default_timer()-start_t)*1000)
            logFile.write(str(int((timeit.default_timer()-start_t)*1000)) + '\t' + 'task' + '\n')
            print(tim, 'task')
            for jdx in range(5):
                for j in range(24):
                    if 0 <= j < 12:
                        image.draw()
                        cros_p.draw()
                        win.flip()
                    if 12 <= j < 24:
                        win.flip() 
        else:
            for jdx in range(5):
                for j in range(24):
                    if 0 <= j < 12:
                        image.draw()
                        cross.draw()
                        win.flip()
                    if 12 <= j < 24:
                        win.flip() 
    tim = int(round(timeit.default_timer()-start_t)*1000)
    logFile.write(str(int(round(timeit.default_timer()-start_t)*1000)) + '\t' + str(i) + '\n')
    print(tim, i)
    
def near(image):
    fix_c = random.choice(fix_change)
    for idx in range(6):
        if idx == fix_c:
            tim = int((timeit.default_timer()-start_t)*1000)
            logFile.write(str(int((timeit.default_timer()-start_t)*1000)) + '\t' + 'task' + '\n')
            print(tim, 'task')
            for jdx in range(5):
                for j in range(24):
                    if 0 <= j < 12:
                        image.draw()
                        occluder_white.draw()
                        cros_p.draw()
                        win.flip()
                    if 12 <= j < 24:
                        win.flip()
        else:
            for jdx in range(5):
                for j in range(24):
                    if 0 <= j < 12:
                        image.draw()
                        occluder_white.draw()
                        cross.draw()
                        win.flip()
                    if 12 <= j < 24:
                        win.flip()
    tim = int(round(timeit.default_timer()-start_t)*1000)
    logFile.write(str(int(round(timeit.default_timer()-start_t)*1000)) + '\t' + str(i) + '\n')
    print(tim, i)

def occluder(image):
    fix_c = random.choice(fix_change)
    for idx in range(6):
        if idx == fix_c:
            print(idx)
            tim = int((timeit.default_timer()-start_t)*1000)
            logFile.write(str(int((timeit.default_timer()-start_t)*1000)) + '\t' + 'task' + '\n')
            print(tim, 'task')
            for jdx in range(5):
                for j in range(24):
                    if 0 <= j < 12:
                        image.draw()
                        occluder_white.draw()
                        cros_p.draw()
                        win.flip()
                    elif 12 <= j < 24:
                        win.flip() 
        else:
            for jdx in range(5):
                for j in range(24):
                    if 0 <= j < 12:
                        image.draw()
                        occluder_white.draw()
                        cross.draw()
                        win.flip()
                    elif 12 <= j < 24:
                        win.flip() 
    
    tim = int(round(timeit.default_timer()-start_t)*1000)
    logFile.write(str(int(round(timeit.default_timer()-start_t)*1000)) + '\t' + str(i) + '\n')
    print(tim, i)
    

def near_noise(image):# consider about the timing, we need to prepare the image first otherwise it will have 1s delay
    for b in noise_list:
        if b == 1:
            for j in range(24):
                if 0 <= j < 12:
                    noise_img_1.draw()
                    image.draw()
                    occluder_white.draw()
                    cross.draw()
                    win.flip()
                if 12 <= j < 24:
                    win.flip()
        if b == 2:
            for j in range(24):
                if 0 <= j < 12:
                    noise_img_2.draw()
                    image.draw()
                    occluder_white.draw()
                    cross.draw()
                    win.flip()
                if 12 <= j < 24:
                    win.flip()
        if b == 3:
            for j in range(24):
                if 0 <= j < 12:
                    noise_img_3.draw()
                    image.draw()
                    occluder_white.draw()
                    cross.draw()
                    win.flip()
                if 12 <= j < 24:
                    win.flip()
    tim = int(round(timeit.default_timer()-start_t)*1000)
    logFile.write(str(int((timeit.default_timer()-start_t)*1000)) + '\t' + 'noise' + '\n')
    print(tim, 'noise')                    
                        
def ISI(fixation_1, fixation_2): #with the fixation colour changed. ISI 12s 12 * 60frames
    fix_c = random.choice(fix_change)
    for idx in range(12):
        if idx == fix_c:
            print(idx)
            tim = int((timeit.default_timer()-start_t)*1000)
            logFile.write(str(int((timeit.default_timer()-start_t)*1000)) + '\t' + 'task' + '\n')
            print(tim, 'task')
            for jdx in range(60):
                fixation_2.draw()
                win.flip()
        else:
            for jdx in range(60):
                fixation_1.draw()
                win.flip()
            
    tim = int(round(timeit.default_timer()-start_t)*1000)
    logFile.write(str(int((timeit.default_timer()-start_t)*1000)) + '\t' + 'ISI' + '\n')
    print(tim, 'ISI')

def mapping(check1, check2, cross1, cross2):
    fix_c = random.choice(fix_change)
    for idx in range(0, 12): # 12 seconds checkerboard
        if idx == fix_c:
            print(idx)
            tim = int((timeit.default_timer()-start_t)*1000)
            logFile.write(str(int((timeit.default_timer()-start_t)*1000)) + '\t' + 'task' + '\n')
            print(tim, 'task')
            for kdx in range(0, 5):
                for jdx in range(0, 6):
                    check1.draw()
                    cross2.draw()
                    win.flip()

                for jdx in range(0, 6):
                    check2.draw()
                    cross2.draw()
                    win.flip()
        else:
            for kdx in range(0, 5):
                for jdx in range(0, 6):
                    check1.draw()
                    cross1.draw()
                    win.flip()

                for jdx in range(0, 6):
                    check2.draw()
                    cross1.draw()
                    win.flip()
    tim = int(round(timeit.default_timer()-start_t)*1000)
    logFile.write(str(int(round(timeit.default_timer()-start_t)*1000)) + '\t' + str(trial) + '\n')
    print(tim, trial)

def close_exp():
    win.close()
    logFile.close()

event.globalKeys.add(key='c',
                    func=key_press_city,
                    name='recoginse city')

event.globalKeys.add(key='f',
                     func=key_press_factory,
                     name='recoginse factory')

event.globalKeys.add(key='space',
                     func=key_press_focus_task,
                     name='response')

event.globalKeys.add(key='a',
                     func=close_exp,
                     name='shut down')


#........................experiment start.......................................
induct.draw()
win.flip()
event.waitKeys(keyList= ['return'])
start_t = timeit.default_timer()
logFile.write('0' + '\t' + 'begain' + '\n')
print('0' , 'begain')

#cross.draw() 
for idx in range(720):
    cross.draw()
    win.flip()
tim = int(round(timeit.default_timer()-start_t)*1000)
logFile.write(str(int(round(timeit.default_timer()-start_t)*1000)) + '\t' + 'start' + '\n')
print(tim, 'start')


for trial in sequence_list:
    if trial == 't1':
        for i in stim_list_full:
            if i == 'city':
                
                full(city)
                
            if i == 'cityn_noise':
                
                near_noise(city_n)
 
            if i == 'city_n':
                
                near(city_n)
                
            if i == 'fact':
                
                full(factory)
                
            if i == 'factn_noise':
               
                near_noise(factory_n)
                
            if i == 'fact_n':
               
                near(factory_n)
                
        ISI(cross, cros_r)
        
    if trial == 't2':
        for i in stim_list_occ:
            if i == 'city_occ':
                
                occluder(city)
                
            if i == 'cityn_noise':
                near_noise(city_n)
                
            if i == 'city_n':
                near(city_n)
                
            if i == 'fact_occ':
                
                occluder(factory)
                
            if i == 'factn_noise':
                
                near_noise(factory_n)
 
            if i == 'fact_n':
                
                near(factory_n)
        
        ISI(cross, cros_r)
    
    if trial == 'tar_1':
        mapping(checkerocc_1, checkerocc_2, cross, cros_r)
        ISI(cross, cros_r)
        
    if trial == 'tar_2':
        mapping(checkerocc_1, checkerocc_2, cross, cros_r)
        ISI(cross, cros_r)
        
    if trial == 'sround':
        mapping(checkercon_1, checkercon_2, cross, cros_r)
        ISI(cross, cros_r)
            
    if trial == 'border':
        mapping(checkerbor_1, checkerbor_2, cross, cros_r)
        ISI(cross, cros_r)

win.close()
logFile.close()

















from psychopy import visual, core

# Setup stimulus
win = visual.Window([400, 400])
ind = visual.TextStim(win, text= '-', pos = (0,0))
induct = visual.TextStim(win, text= '+', pos = (0,0))



for j in range(30):
    for j in range(24):
        if 0 <= j < 12:
            ind.draw()
            win.flip()
            i = i +1
            print(j)
        if 12 <= j < 24:
            
            win.flip()
            c = c + 1
            print(j)

print(i)
print(c)
    
        
        

    
import pygame as pg
import time
import threading

running = True;

################################################################

#pygame config
pg.init()

pg.font.init()

#application settings
frame_rate = 60

width , height = 800 , 800

surface = pg.display.set_mode((width , height))
    
clock = pg.time.Clock()

application_name = 'Sort Algorithm Bar Visualizer'

#bar
bar_separation = 2 #scaler
bar_width = 20 #px
bar_height_multiplier = 10 #px
bar_update_time = 0.01 #seconds

#paths
application_icon_path = 'images/application_logo.png';

#colors
blue = (0,203,255)
black = (0,0,0)

#####################

### DATA TO SORT ####

arr = [8,5,6,7,4,1,3,2,15,9,14,12,13,10,11]

n = len(arr)

################################################################

def pygame_get_details():
    print(pg.version.vernum)
    print(pg.version.SDL)
    
def application_set_icon():
    icon = pg.image.load(application_icon_path)
    pg.display.set_icon(icon)

def application_set_title():
    pg.display.set_caption(application_name)

def application_initialize():
    application_set_icon()
    application_set_title()

def application_quit():
    pg.quit()
    quit()

def application_catch_events():
    global bar_height_multiplier, bar_separation
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            application_quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                bar_height_multiplier += 5
            if event.key == pg.K_DOWN:
                bar_height_multiplier -= 5
            if event.key == pg.K_LEFT:
                bar_separation += 1
            if event.key == pg.K_RIGHT:
                bar_separation -= 1
                
                

def draw_bars():
    separation = 0
    for x in range(0,n):
        pg.draw.rect(surface , blue , ((20+bar_width*separation),height-20-(arr[x]*bar_height_multiplier),bar_width,1*bar_height_multiplier*arr[x]))
        separation = separation+bar_separation
        
def sort_array():

    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            time.sleep(bar_update_time)
    print(arr)
                
if __name__ == '__main__':
    pygame_get_details()
    
    #init()

    application_initialize()
    threads = []
    t = threading.Thread(target = sort_array) #multithreading
    threads.append(t)
    t.start()
    
    while running:

        surface.fill(black)

        draw_bars()

        application_catch_events()  
                
        clock.tick(frame_rate)
        pg.display.flip()


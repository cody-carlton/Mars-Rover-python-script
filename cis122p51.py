'''
Title: Project 5-1 – Mars Explore
Author: Cody Carlton
Credits: N/A
Description: turtle/robot collects data on Mars; report results
'''
from turtle import *
from random import randint

def rover_loc():
    '''
    return random number for rover location

    >>> rover_loc()
    125
    '''
    return (randint(-275, 275)) # passes on random integer to mars_explore()

def water_content():
    '''
    return random number for water content

    >>> water_content()
    150
    '''
    return randint(1, 290) # can only be positive integers

def temperature():
    '''
    return random number for temperature

    >>> temperature
    -50
    '''

    return randint(-178, 1) 

def mars_explore():
    '''
    function that takes return values from rover_loc twice for x and y positions
    traces location on turtle and takes return values from water_content and temperature
    and prints numbers under xpos, ypos, water and temp

    >>>mars_explore()
    
    draws in turtle canvas
    -50  90  150  -75

    '''
    xpos = rover_loc() # local variable assigment for horizontal position of rover
    ypos = rover_loc() # local variable assignment for vertical position of rover

    goto(xpos, ypos) # tells turtle to travel to the location set by xpos and ypos
    dot() # prints a dot at each x and y rover_loc location

   

    water = water_content()
    temp = temperature()

    print(xpos, '\t', # /t lines up our printed return values with mar_explore_main function
          ypos, '\t',
          water, '\t',
          temp)
    


def mars_explore_main():
    '''
    main function for mars_explore:
    set up print and graphical output
    then call mars_explore repeatedly
    >>> mars_explore_main()
    '''
    print('xpos', '\t',  # label for print output
          'ypos', '\t',  # note special char \t
          'water', '\t', # which acts like the
          'temp')        # tab key

 # set up graphical output
    reset()
    title('Mars Rover')
    display_color = 'blue'
    pencolor(display_color)
    dot(10, display_color) # mark rover's starting position
    
 # explore Mars
    for i in range(20): # calls function mars_explore 20 times
        
    
        mars_explore() 
    return


mars_explore_main()

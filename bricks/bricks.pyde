#Shea Galley, Patrick Melancon, Jonathan Wan

import random

x=25
y=550

def setup():
    global power_x, power_y
    size(580,600)
    background(14,47,130)
    power_x = random.randint(0, 14)
    power_y = random.randint(0, 8)

def draw():
    global power_x, power_y
    background(14,47,130)
    top_margin()
    border()
    slider()
    bricks(power_x, power_y)    

def top_margin():
    fill(0)
    rect(0,0,width,20)
    
def border():
    fill(91,91,92)
    rect(0,20,width,10)
    rect(0,20,10,height)
    rect(width-10,20,height,width)

def bricks(power_x, power_y):
    pushMatrix()
    translate(10,30)
    for i in range(14):
        pushMatrix()
        translate(i*40,0)
        for j in range(8):
            pushMatrix()
            translate(0,j*15)
            if i == power_x and j == power_y:
                powerup()
            else:
                redbricks()
            #noLoop()
            popMatrix()
        popMatrix()
    popMatrix()

def redbricks():
    fill(227,33,11)
    rect(0,0,40,15,7)
    
def slider():
    global x,y
    if keyPressed:
        if keyCode== LEFT:
            x=x-10
        if keyCode== RIGHT:
            x=x+10
    if x < 25:
        x = 25
    if x > 505:
        x = 505
    if mousePressed:
        x=mouseX
    if x < 25:
        x = 25
    if x > 480:
        x = 480

            
    fill(245,42,15)
    ellipse(x,y+13,25,25)
    ellipse(x+75,y+13,25,25)
    fill(91,91,92)
    rect(x,y,75,25)
    
def powerup():
    fill(255,0,230)
    rect(0,0,40,15,7)
    

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:48:23 2015

@author: LuizJR
"""

import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *

def f():
    fs, data = wavfile.read("musicwav.wav") # load the data
    a = data.T[0] # this is a two channel soundtrack, I get the first track
    #b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    #c = fft(b) # create a list of complex number
    #d = len(c)/2  # you only need half of the fft list
    #plt.plot(abs(c[:(d-1)]),'r')
    #savefig("musicwav.wav"+'.png',bbox_inches='tight')
    #plt.show()
    print (a[::27000])
    plt.plot(a[::10000])
    plt.show()

f()

import pygame
from pygame import *
y = 0
dir = 1
running = True
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
linecolor = 255, 0, 0
bgcolor = 0, 0, 0
 
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
screen.fill(bgcolor)
pygame.draw.line(screen, linecolor, (0, y), (width-1, y))
 
y += dir
if y == 0 or y == height-1: dir *= -1

pygame.display.flip()


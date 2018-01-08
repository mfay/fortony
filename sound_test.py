import pyglet
from time import sleep

music = pyglet.resource.media("alert.wav")
music.play()

sleep(10)
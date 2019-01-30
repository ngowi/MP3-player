#MP3 player, project 1
#Author: Michael Jordan
#Last modified: Jan 22,2019

from time import sleep
from pygame import mixer
print("\n\nMP3 player v1.0\n\n")

try:
    file = open("playlist","r+")
    album = file.read()
    file.close()   #closing file object
except IOError:
    print("Whoops! the playlist was not found")
    
track = album.split()
print("ALBUM: %s"%("DAMN by Kendrick Lamar"))
def player(track):
    mixer.init()
    mixer.music.load("DAMN/"+track+".mp3")
    mixer.music.play()
    return
for x in  track:
    player(x)
    sleep(120)
    


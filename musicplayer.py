#importing libraries 
import pygame
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import os

#creating window 
root=Tk()
root.title('MHM Python MP3 Music Player App ')
#initialize mhmmixer 
mixer.init()
#create ListBox for mp3 List
songs_list=Listbox(root,selectmode=SINGLE,bg="white",fg="blue",font=('arial',15),height=20,width=53,selectbackground="gray",selectforeground="aqua")
songs_list.grid(columnspan=9)
MUSIC_END = pygame.USEREVENT+1
pygame.init()

def check_event():
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            Next() # In your case, run self.__queue_song() and self.__set_new_selection()
    root.after(100,check_event) 

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    song = w.get(index)
    mixer.music.load(song)
    mixer.music.set_endevent(MUSIC_END)
    mixer.music.play()
    check_event()

#add many songs to the playlist of python mp3 player
def addsongs():
#to open a file
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for s in temp_song:
        #s=s.replace("/Users/mhmalekian/Documents/Music/","")
        songs_list.insert(END,s)
     
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
    
    
def Play():
    song=songs_list.get(ACTIVE)
    #song=f'/Users/mhmalekian/Documents/Music/{song}'
    mixer.music.load(song)
    mixer.music.set_endevent(MUSIC_END)
    mixer.music.play()
    check_event()

#to pause the song 
def Pause():
    mixer.music.pause()

#to stop the  song 
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song

def Resume():
    mixer.music.unpause()

#Function to navigate from the current song
def Previous():
    #to get the selected song index
    previous_one=songs_list.curselection()
    #to get the previous song index
    previous_one=previous_one[0]-1
    #to get the previous song
    temp2=songs_list.get(previous_one)
    #temp2=f'/Users/mhmalekian/Documents/Music/'
    mixer.music.load(temp2)
    mixer.music.set_endevent(MUSIC_END)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate new song
    songs_list.activate(previous_one)
    #set the next song
    songs_list.selection_set(previous_one)
    check_event()

def Next():
    #to get the selected song index
    next_one=songs_list.curselection()
    #to get the next song index
    next_one=next_one[0]+1
    #to get the next song 
    temp=songs_list.get(next_one)
    #        temp=f'C:/Users/DataFlair/python-mp3-music-player/{temp}'
    mixer.music.load(temp)
    mixer.music.set_endevent(MUSIC_END)
    mixer.music.play()
    
    songs_list.selection_clear(0,END)
    #activate newsong
    songs_list.activate(next_one)
     #set the next song
    songs_list.selection_set(next_one)
    check_event()




#font is defined which is to be used for the button font 
defined_font = font.Font(family='Helvetica')


def directorychooser():
 
    directory = filedialog.askdirectory()
    os.chdir(directory)
 
    listofsongs = []
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
            songs_list.insert(END,directory +'/'+files)
 
 
    mixer.init()
    mixer.music.load(directory +'/'+ listofsongs[0])
    mixer.music.set_endevent(MUSIC_END)
    mixer.music.play()
    check_event()
    
    mixer.time.delay(2000)


#Define ListBox Event
songs_list.bind('<<ListboxSelect>>', onselect)
#Directory Chooser
choose_but=Button(root,text="Choose Directory",width =13,command=directorychooser)
choose_but['font']=defined_font
choose_but.grid(row=1,column=0)

#play button
play_button=Button(root,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=1)

#pause button 
pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=2)

#stop button
stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=3)

#resume button
Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=4)

#previous button
previous_button=Button(root,text="Prev",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=5)

#nextbutton
next_button=Button(root,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=6)

#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)

mainloop()




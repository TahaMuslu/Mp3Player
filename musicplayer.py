import tkinter as tk
import fnmatch
import os
from pygame import mixer


# Pencerenin Oluşturulması
canvas=tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x500+450+100")
canvas.config(bg='black')

# Müziklerin Dosya Yolu
rootpath = "C:\\Users\\taha-\\Desktop\\Masaüstü\\müzik"
pattern = "*.mp3"

mixer.init()

# Butonların Simgelerinin Oluşturulması
prev_img = tk.PhotoImage(file="prev_img.png")
stop_img = tk.PhotoImage(file="stop_img.png")
play_img = tk.PhotoImage(file="play_img.png")
pause_img = tk.PhotoImage(file="pause_img.png")
next_img = tk.PhotoImage(file="next_img.png")


def select():
    if pauseButton["text"]!="Pause":
        mixer.music.unpause()
        pauseButton["text"] = "Pause"
    else:
        label.config(text=listBox.get("anchor"))
        mixer.music.load(rootpath+"\\"+listBox.get("anchor"))
        mixer.music.play()


def stop():
    mixer.music.stop()
    listBox.select_clear('active')


def playNext():
    pauseButton["text"] = "Pause"
    nextSong = listBox.curselection()
    nextSong = nextSong[0] + 1
    nextSongName = listBox.get(nextSong)
    label.config(text=nextSongName)
    mixer.music.load(rootpath+"\\"+nextSongName)
    mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(nextSong)
    listBox.select_set(nextSong)


def playPrevious():
    pauseButton["text"] = "Pause"
    nextSong = listBox.curselection()
    nextSong = nextSong[0] - 1
    nextSongName = listBox.get(nextSong)
    label.config(text=nextSongName)
    mixer.music.load(rootpath+"\\"+nextSongName)
    mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(nextSong)
    listBox.select_set(nextSong)


def pauseSong():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"



listBox = tk.Listbox(canvas, fg="limegreen", bg="black", width=80, font=('ds-digital', 14))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text=' ', bg='black', fg='yellow', font=('ds-digital', 18))
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor="center")


prevButton = tk.Button(canvas, text="Prev", image=prev_img, bg='black', borderwidth=0, command=playPrevious)
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg='black', borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text="Play", image=play_img, bg='black', borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text="Pause", image=pause_img,bg='black', borderwidth=0, command=pauseSong)
pauseButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", image=next_img, bg='black', borderwidth=0, command=playNext)
nextButton.pack(pady=15, in_=top, side='left')


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)


canvas.mainloop()

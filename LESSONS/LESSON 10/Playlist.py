#A Python program that creates a Playlist object with a parameterized constructor (name and genre), initializes an empty songs list as a default attribute, provides methods to add, remove, and display songs, fires a destructor when the playlist is deleted, and lets you control everything through a numbered menu loop.

class Playlist:
    def __init__ (self,name,genre):
        self.songs=[]
    def add (self,song_name):
        self.songs.append(song_name)
        print(song_name,"is added")
    def remove (self,song_name):
        self.songs.remove(song_name)
        print(song_name,"is deleted")
    def display (self):
        print(self.songs)
    def __del__(self):
        print("i am des")

Himansh_Playlist=Playlist("Himansh_Playlist","Road trip")
Himansh_Playlist.add("heat waves")
Himansh_Playlist.add("Matadora")
Himansh_Playlist.add("Kaccha ghada")
Himansh_Playlist.add("montagem rugada")
Himansh_Playlist.display()
Himansh_Playlist.remove("heat waves")
Himansh_Playlist.display()
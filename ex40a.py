class Song(object):
    def __init__(self):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happ_bday = Song(["Happy birthday to you",
                  "I dont want want to get sued",
                  "So I will stop here."])

bulls_on_parade =  Song(["They rally around the family",
                         "With pockets full of shells"])

happ_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


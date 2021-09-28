#takes two playlists and spits out one


from pytube import Playlist

print('input a playlist link')
E = True
while(E == True):
    try:
        p1 = Playlist(input())
        E = False
    except:
        print("Error with link, check your link and try again")

print("input a second playlist link")
E = True
while(E == True):
    try:
        p2 = Playlist(input())
        E = False
    except:
        print("Error with link, Check your link and try again")

playlist1 =[]
playlist2 =[]
for i in p1.videos:
    playlist1.append(i.title)

for i in p2.videos:
    playlist2.append(i.title)  


duplicates = []
complete = []
total = len(playlist1) + len(playlist2)
n = 0
if len(playlist1) > len(playlist2):
    for i in playlist1:
        for b in playlist2:
            if i == b:
                n = n +1
                duplicates.append(i)
                complete.append(i)
                playlist1.remove(i)
                playlist2.remove(b)
                print(n)
                
else:
    for i in playlist2:
        for b in playlist1:
            if i == b:
                n = n + 1
                duplicates.append(i)
                complete.append(i)
                playlist2.remove(i)
                playlist1.remove(b)
                print(n)

for i in playlist1:
    complete.append(i)
for i in playlist2:
    complete.append(i)

print("complete:")
for i in complete:
    print(i)
print("duplicates:")

for i in duplicates:
    print(i)


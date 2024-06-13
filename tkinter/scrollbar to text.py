import tkinter as tk

a = tk.Tk()

a.title("scrollbar to text")



b=tk.Text(a,height=8,width=40)
scroll = tk.Scrollbar(a)
b.configure(yscrollcommand=scroll.set)
b.pack(side=tk.LEFT)

scroll.config(command=b.yview)
scroll.pack(side=tk.RIGHT,fill=tk.Y)

insert = """
Kiss me hard before you go
Summertime sadness
I just wanted you to know
That, baby, you the best
I got my red dress on tonight
Dancin' in the dark, in the pale moonlight
 got that summertime, summertime sadness
Su-su-summertime, summertime sadness
Got that summertime, summertime sadness
Oh, oh, oh
You might also like
The 30th
Billie Eilish
So Long, London
Taylor Swift
The Tortured Poets Department
Taylor Swift
[Verse 2]
I'm feelin' electric tonight
Cruisin' down the coast, goin' 'bout 99
Got my bad baby by my heavenly side
I know, if I go, I'll die happy tonight

[Pre-Chorus]
Oh my God, I feel it in the air
Telephone wires above are sizzlin' like a snare
Honey, I'm on fire, I feel it everywhere
Nothin' scares me anymore (One, two, three, four)

[Chorus]
Kiss me hard before you go
Summertime sadness
I just wanted you to know
That, baby, you the best

[Post-Chorus]
I got that summertime, summertime sadness
Su-su-summertime, summertime sadness
Got that summertime, summertime sadness
Oh, oh, oh

[Bridge]
Think I'll miss you forever
Like the stars miss the sun in the morning sky
Later's better than never
Even if you're gone, I'm gonna drive (Drive)
Drive
[Breakdown]
I got that summertime, summertime sadness
Su-su-summertime, summertime sadness
Got that summertime, summertime sadness
Oh, oh, oh

[Chorus]
Kiss me hard before you go
Summertime sadness
I just wanted you to know
That, baby, you the best

[Post-Chorus]
I got that summertime, summertime sadness
Su-su-summertime, summertime sadness
Got that summertime, summertime sadness
Oh, oh, oh
"""

b.insert(tk.END,insert)
a.mainloop()





a.mainloop()
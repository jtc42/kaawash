import glob
import os

import kaa

# Load .txt files found in 'songs' folder
files = glob.glob("songs/*.txt") #Find all song files

# Open files and store contents in dictionary of song names
songs = {}
for f in files:
    with open(f, "r") as file:
        title = f[6:-4] # Cut crap out of file name
        raw = file.read()
        songs[title] = kaa.make_chordblocks(raw, buffer=True)

templates = ["template.html"]

for template in templates:
    _, extension = os.path.splitext(template)

    # Make songbook HTML book
    title = "Take on Me, Twice"
    html_book = kaa.make_book(songs, title, template)
    
    # Save generated songbook page as an HTML file
    with open("{0}{1}".format(title.lower().replace(' ', '_'), extension), "w") as file:
        file.write(html_book)

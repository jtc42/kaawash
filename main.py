import glob

import kaa

# Load .txt files found in 'songs' folder
files = glob.glob("songs/*.txt") #Find all song files

# Open files and store contents in dictionary of song names
songs = {}
for f in files:
    with open(f, "r") as file:
        title = f[6:-4] # Cut crap out of file name
        raw = file.read()
        songs[title] = kaa.core.make_chordblocks(raw)

# Make songbook HTML book
book = kaa.html.make_book(songs)

# Save generated songbook page as an HTML file
with open("index.html", "w") as file:
    file.write(book)

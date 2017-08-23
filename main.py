import glob
import os

import kaa

# List of book folder names to be compiled
books = ['Take on Me, Twice']

# List of template files to use
templates = ["template.tex", "template.html"]


# For each book to be generated
for book in books:
    
    # Get directory for files
    book_dir = os.path.join("books", book)
    
    # Load .txt files found in 'songs' folder
    files = glob.glob(os.path.join(book_dir, "*.txt")) #Find all song files
    
    # Open files and store contents in dictionary of song names
    songs = {}
    for f in files:
        with open(f, "r") as file:
            title = os.path.basename(f)[:-4] # Cut crap out of file name
            raw = file.read()
            songs[title] = kaa.make_chordblocks(raw, buffer=True)
    
    for template in templates:
        _, extension = os.path.splitext(template) # Get file extension of template
    
        # Make songbook HTML book
        book_code = kaa.make_book(songs, book, template)
        
        # Save generated songbook page as an HTML file
        save_name = "{0}{1}".format(book.lower().replace(' ', '_'), extension)
        save_file = os.path.join("books", save_name)
        
        with open(save_file, "w") as file:
            file.write(book_code)
            print("Generated '{}'".format(save_file))

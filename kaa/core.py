# Function to create  an array of "chordblocks" from a raw songfile string
"""
This can be considered the main interpreter. 
Anything clever like automatically filling in verse/chorus chords should go here.
This is essentially the step that converts the txt files into arrays of "chordblocks"
that then get converted into HTML tables.
"""
def make_chordblocks(raw):
    ly_lst = raw.split('\n') # Split raw text file into array of lines

    lines = [[ s.split(']') for s in l.split('[')] for l in ly_lst] # Split each line into an array of chord blocks
    
    #Handle first cells (makes all first cells the same length, even if data is missing)
    for line in lines:
        if len(line[0]) is not 0:
            line[0].insert(0,"")
    
    return lines
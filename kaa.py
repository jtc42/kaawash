from jinja2 import Template
import os


# Function to replace a particular index within a string
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])


# Function to create  an array of "chordblocks" from a raw songfile string
"""
This can be considered the main interpreter. 
Anything clever like automatically filling in verse/chorus chords should go here.
This is essentially the step that converts the txt files into arrays of "chordblocks"
that then get converted into HTML tables.
"""
def make_chordblocks(raw, buffer = False):
    ly_lst = raw.split('\n') # Split raw text file into array of lines

    lines = [[ s.split(']') for s in l.split('[')] for l in ly_lst] # Split each line into an array of chord blocks
    
    for line in lines:
        #Handle first cells (makes all first cells the same length, even if data is missing)
        if len(line[0]) is not 0:
            line[0].insert(0,"")
        
        # Pad out chords that fall off-syllable
        if buffer:
            for block in line: # For each syllable block
                try: # If zeroth character exists
                    if block[1][0] == " ": # If zeroth character is a space
                        block[1] = replace_str_index(block[1],index=0,replacement='\t') # Replace with a tab
                except:
                    pass
    
    return lines


# Function to create an HTML "book" of all song files in a properly formatted dictionary
def make_book(dictionary, title, template):
    template_path = os.path.join("templates", template)
    
    with open(template_path, "r") as template_file:
        model = Template(template_file.read(), trim_blocks=True)
        page = model.render(dictionary=dictionary, title=title)
                             
    return page
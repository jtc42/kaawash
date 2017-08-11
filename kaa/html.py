from . import core

# Function to make an HTML table of a single song line
def make_line(line):
    ca=[] # Create empty array for sections of HTML table code
    
    ca.append('<table>\n') # Create the table for this line
    
    #chords
    for i in range(2): # For chord cell and lyric cell positions
        ca.append('\t<tr>\n') # Create a new table row
        
        for pos in line: # For each chord block in the line
            buffer = '' # Default to no padding
            try: # Some empty table entries don't have a zero-index value
                if pos[i][0] == ' ': # In the cases above, this line would break
                    buffer = '        ' # If the lyric block starts with a space, pad out for chord
            except: # If there's no data in the element at all, use no buffer
                buffer = ''
            ca.append('\t\t<td>{}{}</td>\n'.format(buffer, pos[i])) # Add buffer and table cell content
        
        ca.append('\t</tr>\n') # End the table row
        
    ca.append('</table>\n') # End the table for this line

    str1 = ''.join(ca) # Make string from code table
    return str1 # Return table code for this line


# Function to make a collection of HTML tables from an entire song file
def make_song(chordblock):
    
    code_array = [make_line(line) for line in chordblock] # Pass each line's chord-block array to the interpreter
    
    str1 = ''.join(code_array) # Make string from array of returned table code
    return str1


# Function to create an HTML "book" of all song files in a properly formatted dictionary
def make_book(dictionary):
	# HTML header
    header_string="""<html>\n"""
    
	# Inline styling
	# TODO: Replace with external CSS?
    style_string="""<style>
    table { 
    	text-align: left;
    	border-spacing: 0;
    	border-collapse: collapse;
    	margin-bottom: 10px;
    }
    
    td{
    	padding:0; margin:0;
    	white-space:PRE;
    }
    </style>\n"""
    
	# HTML footer
    footer_string="""</html>"""
    
	# Go through each song in the dictionary and add to the 'songdata' table it's song table and title
    songdata = []
    for name, chordblock in dictionary.items():
        songdata.append("<h1>{}</h1>\n".format(name) + make_song(chordblock))
    
    page = header_string + style_string + ''.join(songdata) + footer_string
                                                 
    return page
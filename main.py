import glob

# Load .txt files found in 'songs' folder
files = glob.glob("songs/*.txt") #Find all song files

# Open files and store contents in dictionary of song names
songs = {}
for f in files:
    with open(f, "r") as file:
        title = f[6:-4] # Cut crap out of file name
        songs[title] = file.read()

# Function to make an HTML table of a single song line
def make_table(line):
    ca=[]
    #header
    ca.append('<table style="text-align: left;">\n')
    
    #chords
    for i in range(2):
        ca.append('\t<tr>\n')
        
        for pos in line:
            buffer = ''
            try: # Some empty table entries don't have a zero-index value
                if pos[i][0] == ' ': # In the cases above, this line would break
                    buffer = '        '
            except: # If there's no data in the element at all, use no buffer
                buffer = ''
            ca.append('\t\t<td>{}{}</td>\n'.format(buffer, pos[i]))
        
        ca.append('\t</tr>\n')
        
    ca.append('</table>\n')

    str1 = ''.join(ca) # Make string from code table
    return str1

# Function to make a collection of HTML tables from an entire song file
def make_song(raw):
    ly_lst = raw.split('\n')

    lines = [[ s.split(']') for s in l.split('[')] for l in ly_lst]
    
    #Handle first cells
    for line in lines:
        if len(line[0]) is not 0:
            line[0].insert(0,"")
    
    ca = [make_table(line) for line in lines]
    
    str1 = ''.join(ca) # Make string from code table
    return str1
        
# Function to create an HTML "book" of all song files in a properly formatted dictionary
def make_book(dictionary):
	# HTML header
    header_string="""<html>\n"""
    
	# Inline styling
	# TODO: Replace with external CSS?
    style_string="""<style>
    table { 
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
    for name, data in dictionary.items():
        songdata.append("<h1>{}</h1>\n".format(name) + make_song(data))
    
    page = header_string + style_string + ''.join(songdata) + footer_string
                                                 
    return page
    
# Make songbook HTML page
page = make_book(songs)

# Save generated songbook page as an HTML file
with open("index.html", "w") as file:
    file.write(page)
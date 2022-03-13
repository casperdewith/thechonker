# The Chonker
# a program to generate an html file out of a tsv dictionary table
# by Casper de With, 28 feb 2022

import csv
import re
import datetime

"""
dict with "word" as key and array of strings as value.
possible beginnings:

> is a reference; everything in the same cell is a hyperlink
    make sure that every link is a valid entry in dict!
    : is lingo colour, excepting semicolons
; is a separation (possibly bullet point?)
( must be italicised; everything in between, as well as a 

regex for references (p xxxxxxxxxx 1:23)

"""

# \(([pr]) ([0-9A-Za-z_-]{11}) (?:(\d*):)?(\d\d?):(\d\d)\)
# matches e.g. (r xlI1j2d9VJA 0:33)
# cap groups: 1 = r/p; 2 = id; 3-4-5 = h-m-s




terms = set(()) # set of all terms for easy look-up
d = [] # the dictionary

def linkify (w):
    r = ''
    for l in w:
        if l.isalpha() or l.isdigit(): r += l.lower()
        else: r += '-'
    return r
    
def testTsv ():
    # interpret tsv file into 2d array
    with open ("test.tsv") as ch:
       c = csv.reader(ch, delimiter="\t")
       for l in c:
         d.append([e for e in l if e != '']) # remove empty entries
    print(d)

print(terms)            

def replaceExRef (s):
    l = "https://youtu.be/" + s.group(2)
    if s.group(3) is None:
        l += "?t=" + str(60 * int(s.group(4)) + int(s.group(5)))
    else:
        l += "?t=" + str(3600 * int(s.group(3)) + 60 * int(s.group(4)) + int(s.group(5)))
    return '<a class="ex" title="YouTube link to this quote" href="' + l + '">↗' + s.group(1) + '</a>'

def replaceContext (s):
    return s.group(1) + '<i class="context">' + s.group(2) + '</i>'

def convertInRef (s):
    assert s[0] == '>', "Could not convert to InRef; first character not ‘>’ in " + s
    r = ""
    ts = [t.strip() for t in s[1:].split(';')] # individual terms to make links of
    for t in ts:
        if t not in terms: print("Term ‘" + t + "’ not in terms", sep="")
        r += '<a class="in lingo" title="Jump to this entry" href="#' + linkify(t) + '">→&nbsp;' + t + "</a> "
    return r

def convertColon (s):
    assert s[0] == ':', "Could not convert Colon; first character not ‘:’ in " + s
    return '<span class="lingo example">' + s[1:].strip() + '</span>'

def convertSemicolon (s):
    assert s[0] == ';', "Could not convert Semicolon; first character not ‘;’ in " + s
    separator = '<span class="sep">•&nbsp;</span>'
    if s[1] == ':': return separator + convertColon(s[1:])
    else: return separator + s[1:].strip()
    
def convertTerm (s):
    return '<a class="lingo term" href="#' + linkify(s.strip()) + '">' + s.strip() + '</a>' 

def convertDefault (s):
    return '<span class="meaning">' + s.strip() + '</span>'

def readDictionary ():

    # interpret tsv file into 2d array
    with open ("The Chonker - Entries.tsv") as ch:
       c = csv.reader(ch, delimiter="\t")
       for l in c:
           d.append([e for e in l if e != '']) # remove empty entries
    
    # initialise term set
    for l in d:
        terms.add(l[0])

def generate (d):
    readDictionary() # reads chonker.tsv into
    
    hf = open("chonker-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M") + ".html", 'a') # html file 

    hf.write("""
<!DOCTYPE html>
<html>
<head>
<title>The Chonker • Panga & Rays lingo dictionary</title>
<link rel="stylesheet" type="text/css" href="style.css">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<main>
<header>
<h1 class="lingo">The Chonker</h1>
<p>A comprehensive dictionary of <a class="ex" href="https://www.youtube.com/user/PangaTAS">↗&nbsp;PangaeaPanga</a> and <a class="ex" href="https://www.youtube.com/c/raysfireplus">↗&nbsp;Raysfire</a>’s lingo</p>
</header>
<h2>Legend</h2>
<table>
<tr><td><span class="lingo example tilde">~</span></td><td>replaces the keyword</td></tr>
<tr><td><strong>•</strong></td><td>separates different senses or contexts</td></tr>
<tr><td><i><a class="ex" href="#">↗p</a> <a class="ex" href="#">↗r</a></i><td>external reference to a quote by PangaeaPanga or Raysfire</td></tr>
<tr><td><i class="context">(mp)</i></td><td>pertaining to multiplayer</td></tr>
<tr><td><i class="context">(rays)</i></td><td>exclusive to Raysfire</td></tr>
</table>
<hr>
""")
    for row in d:
        hf.write('<p class="entry" id="' + linkify(row[0]) + '">')
        hf.write(convertTerm(row[0])) # first cell in row = term
        
        for cell in range(1, len(row)): # for all other cells in row
            hf.write(' ')
            
            # replace parentheses if directly at beginning
            # or after any semicolon
            row[cell] = re.sub(r'(^|;\s*)(\(.*?\))', replaceContext, row[cell])
            
            # recognise first character and convert
            if   row[cell][0] == ':':
                row[cell] = convertColon(row[cell])
            elif row[cell][0] == ';':
                row[cell] = convertSemicolon(row[cell])
            elif row[cell][0] == '>':
                row[cell] = convertInRef(row[cell])
            # else: row[cell] = convertDefault(row[cell])
            # substitute references by links
            row[cell] = re.sub(r'\(([pr]) ([0-9A-Za-z_-]{11}) (?:(\d*):)?(\d\d?):(\d\d)\)', replaceExRef, row[cell])
            
            row[cell] = re.sub(r'\~', '<span class="tilde">~</span>', row[cell])
            hf.write(row[cell].strip())
        hf.write('</p>')

    hf.write("""<hr>
    <p><em class="lingo">The Chonker</em><br>First Edition (March 2022)<br> by <a class="ex" href="https://reddit.com/user/casperdewith">↗ Casper de With</a></p><p>This work is licensed under a <a rel="license" class="ex" href="http://creativecommons.org/licenses/by-sa/4.0/">↗&nbsp;Creative Commons Attribution-ShareAlike 4.0 International License</a></p></main></body>
</html>""")
    hf.close()
    return





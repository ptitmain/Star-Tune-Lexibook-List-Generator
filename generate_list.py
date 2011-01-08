#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import unicodedata
import getopt


def clean_string(s):
    s = unicode(s, "utf8", "replace")
    s = unicodedata.normalize('NFD', s)
    return s.encode('ascii', 'ignore')

def main(argv=sys.argv):
  opts, args = getopt.getopt(sys.argv[1:], "r" ,"rename")
  rename = False
  for o, a in opts:
     if o == "-r":
        rename = True
     if o == "--rename":
        rename = True

  stack = []
  f = open('list.list', 'w+')

  # Searching all mp3 files
  for filename in os.listdir("."):
    basename, extension = os.path.splitext(filename)
    if extension == ".mp3":
       if (filename != clean_string(filename)):
           print "Attention, le nom de fichier contient des accents !"
	   print filename + " -> " + clean_string(filename)
	   if (rename):
	     print "Renaming " + filename
	     os.rename(filename, clean_string(filename))
	     filename = clean_string(filename)
	   else:
	     print "Utilisez l'option -r ou --rename pour renommer automatiquement les fichiers"
       if (filename == clean_string(filename)):
           stack.append(filename)

  stack.sort()
  print "La liste des morceaux suivants a été générée:"

  # Writting the number of tracks
  f.write(chr(len(stack)))
  f.write(chr(0))

  # Writting the tracks
  for filename in stack:
    print filename
    size = 0
    for lettre in filename:
	f.write(lettre)
	f.write(chr(0))
	size = size + 1
    while size < 128 / 2:
	f.write(chr(0))
	f.write(chr(0))
	size = size + 1

if __name__ == "__main__":
    main()


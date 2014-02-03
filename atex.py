#!/usr/bin/env python3
#Alec Snyder
#tex markup language
#takes in .atex files and coverts to .tex
import sys
import re
import atexlib

infile=sys.argv[1]
usepackage=[]
document=False
outfile=re.split('\.atex$', infile)[0]
outfile=outfile+".tex"
infile=open(infile)
outfile=open(outfile, 'w')
comment="//"
mathOpen="{"
mathClose="}"
author="student"
title="Math Homework"
escape="#"
control="/"
parenOpen="{"
parenClosed="}"
line=infile.readline()
outfile.write("\\documentclass[12pt]{article}\n")
while line!="":
    if line[:6]==comment:
        pass
    elif line[:6]==escape+"title":
        title=line.split()[1]
        outfile.write("\\title{"+title+"}\n")
    elif line[:7]==escape+"author":
        author=line.split()[1]
        outfile.write("\\author{"+author+"}\n")
    elif line[:8]==escape+"control":
        control=line.split()[1]
    elif line[:7]==escape+"import":
        for word in line.split()[1:]:
            usepackage.append(word)
        for pac in usepackage:
            outfile.write("\\usepackage{"+pac+"}\n")
    elif line[:8]==escape+"theorem":
        if not document:
            outfile.write("\\begin{document}\n")
            document=True
        outfile.write("\\newtheorem{theorem}{Theorem}[section]\n")
        outfile.write("\\begin{theorem} \n")
        atexlib.parseSeq(infile, outfile, mathOpen, mathClose,parenOpen, parenClosed, control)
        outfile.write("\\end{theorem}\n")
    elif line[:7]==escape+"center":
        if not document:
            outfile.write("\\begin{document}\n")
            document=True
        outfile.write("\\begin{center}\n")
        atexlib.parseSeq(infile, outfile, mathOpen, mathClose,parenOpen, parenClosed, control)
        outfile.write("\\end{center}\n")
    elif line[:6]==escape+"proof":
        if not document:
            outfile.write("\\begin{document}\n")
            document=True
        outfile.write("\\begin{proof}\n")
        atexlib.parseSeq(infile, outfile, mathOpen, mathClose,parenOpen, parenClosed, control)
        outfile.write("\\end{proof}\n")
    elif line[:4]==escape+"tex":
        atexlib.parseTex(infile, outfile)
    line=infile.readline()
outfile.write("\end{document}\n")
infile.close()
outfile.close()

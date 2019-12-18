#!/usr/bin/env python

import argparse
import random
import sys

parser = argparse.ArgumentParser(description='A simple bingo card generator.')
parser.add_argument("termsfile", help="text file with each term on its own line", type=argparse.FileType('r'))
parser.add_argument("cards", help="number of bingo cards per sheet", type=int)
parser.add_argument("sheets", help="number of sheets", type=int)
parser.add_argument("--outfile", default="out.html", help="output file, default: out.html", type=argparse.FileType('w'))
parser.add_argument("--columns", default=5, help="number of columns per card, default: 5", type=int)
parser.add_argument("--rows", default=3, help="number of rows per card, default: 3", type=int)
args = parser.parse_args()

terms = args.termsfile.readlines()

# XHTML4 Strict, y'all!
head = ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">\n"
        "<html lang=\"en\">\n<head>\n"
        "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
        "<title>Bingo Cards</title>\n"
        "<style type=\"text/css\">\n"
        "\tbody { font-size: 12px; }\n"
        "\ttable { margin: 40px auto; border-spacing: 2px; }\n"
        "\t.newpage { page-break-after:always; }\n"
        "\ttr { height: 80px; }\n"
        "\ttd { text-align: center; border: thin black solid; padding: 10px; width: 80px; }\n"
        "</style>\n</head>\n<body>\n")

# Generates an HTML table representation of the bingo card for terms
def generateTable(terms, cols, rows, pagebreak = True):
    ts = random.sample(terms, cols * rows)
    if pagebreak:
        res = "<table class=\"newpage\">\n"
    else:
        res = "<table>\n"
    for i, term in enumerate(ts):
        if i % cols == 0:
            res += "\t<tr>\n"
        res += "\t\t<td>" + term + "</td>\n"
        if i % cols == cols - 1:
            res += "\t</tr>\n"
    res += "</table>\n"
    return res

# write outfile
args.outfile.write(head)

cards = args.cards
cols = args.columns
rows = args.rows
sheets = args.sheets

for i in range(sheets):
    for i in range(cards):
        random.shuffle(terms)
        if i == cards - 1:
            args.outfile.write(generateTable(terms, cols, rows, pagebreak=True))
        else:
            args.outfile.write(generateTable(terms, cols, rows, pagebreak=False))

args.outfile.write("</body></html>")

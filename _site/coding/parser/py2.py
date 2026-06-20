
import bibtexparser

with open('papers.txt') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

print(bib_database.entries)

for i in range(0,106):
    print(bib_database.entries[i]['ID'])


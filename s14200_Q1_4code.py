"""
input: DNA sequence for BRCA 1 gene in FASTA format
 Output: length of the DNA sequence

"""

# •	Read the sequence from text file
file = open("sequence", "r")
contents = file.read()
file.close()

# Count sequence from one end to another
counter = 0

for base in contents:
    base = base.strip()
    if base.splitlines():
        counter = counter + 1

# Print total length of database.
print("Length of sequence is " + str(counter))

"""
input: DNA sequence for BRCA 1 gene in FASTA format
 Output: length of the DNA sequence

"""

# •	Read the sequence from text file
file = open("sequence", "rt")
contents = file.read()

# remove spaces at the end of the lines
contents1 = contents.replace('\n', '')


# Print total length of database.
print("Length of sequence is ", len(contents1))
file.close()

"""
input: DNA sequence for BRCA 1 gene in FASTA format
 Output: length of the DNA sequence

"""

# •	Read the sequence from text file
file = open("sequence", "r")
contents = file.read()
file.close()
# print(contents)


# Count No of A bases in sequence
counter1 = 0
for base in contents:
    if base == "A":
        counter1 = counter1 + 1

# Count No of G bases in sequence
counter2 = 0
for base in contents:
    if base == "G":
        counter2 = counter2 + 1

# Count No of T bases in sequence
counter3 = 0
for base in contents:
    if base == "T":
        counter3 = counter3 + 1

# Count No of C bases in sequence
counter4 = 0
for base in contents:
    if base == "C":
        counter4 = counter4 + 1

# Get the total count as one count
counter = counter1 + counter2 + counter3 + counter4

# Print total length of database.
print("Length of sequence is " + str(counter))
print("No of adenine bases are " + str(counter1))
print("No of guanine bases are " + str(counter2))
print("No of thymine bases are " + str(counter3))
print("No of cytosine bases are " + str(counter4))

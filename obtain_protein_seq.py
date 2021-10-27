# Reads in the preproinsulin_seq.txt file
file = open("Data_Files/preproinsulin_seq.txt", "r")
lines = []
for line in file:
    lines.append(line.strip())
file.close()
# Cleans the contents of the preproinsulin_seq.txt file
lines.remove("ORIGIN")
lines.remove("//")
newData = ''
for i in range(0, len(lines)):
    newData += ''.join([i for i in lines[i] if not i.isdigit()]).strip()
newData = newData.replace(" ", "")
# Creates a file called preproinsulin_seq_clean.txt and writes the clean contents from the preproinsulin_seq.txt file
file = open("Data_Files/preproinsulin_seq_clean.txt", "w")
file.write(newData)
file.close()
# Creates a file called lsinsulin_seq_clean.txt
file = open("Data_Files/lsinsulin_seq_clean.txt", "w")
file.write(newData[0:24])
file.close()
# Creates a file called binsulin_seq_clean.txt
file = open("Data_Files/binsulin_seq_clean.txt", "w")
file.write(newData[24:54])
file.close()
# Creates a file called cinsulin_seq_clean.txt
file = open("Data_Files/cinsulin_seq_clean.txt", "w")
file.write(newData[54:89])
file.close()
# Creates a file called ainsulin_seq_clean.txt
file = open("Data_Files/ainsulin_seq_clean.txt", "w")
file.write(newData[89:110])
file.close()
"""
    Author: Lori White
    Purpose: Finds the molecular weight of the insulin stored in the preproinsulin_seq_clean.txt
    text file and finds the percent error of the insulin's molecular weight.
"""
# store the human preproinsulin sequence in a variable called preproinsulin:**
preproInsulin = open("Data_Files/preproinsulin_seq_clean.txt", "r").read()
# store the remaining sequence elements of human insulin in variables:
lsInsulin, bInsulin, cInsulin, aInsulin = preproInsulin[0:24], preproInsulin[24:54], preproInsulin[54:89], preproInsulin[89:110]
insulin = bInsulin + aInsulin
# Printing "the sequence of human insulin" to console using successive print() commands
print(f"The sequence of human preproinsulin:")
print(preproInsulin)
# printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)
# Printing to console using concatenated strings
bInsulinPrint = "The sequence of chain b of human insulin: " + bInsulin
print(bInsulinPrint)
# Concatenating chain b to chain a to make the human insulin peptide
insulin = bInsulin + aInsulin
print("The sequence of human insulin: " + insulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19, 'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19}
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
# Calculating the percent error
molecularWeightInsulinActual = 5807.63
print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
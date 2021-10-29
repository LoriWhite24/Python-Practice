"""
    Author: Lori White
    Purpose: Calculate the net charge of an insulin based off of the pH.
    python 3.9.6  
    coding: utf-8
""" 
# store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = open("Data_Files/preproinsulin_seq_clean.txt", "r").read()
# store the remaining sequence elements of human insulin in variables:  
lsInsulin, bInsulin, cInsulin, aInsulin = preproInsulin[0:24], preproInsulin[24:54], preproInsulin[54:89], preproInsulin[89:110] 
insulin = bInsulin + aInsulin
# Store AA pKR values and N/C-terms in dictionaries:
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}
# Count the occurrence of each pKR AA in the sequence, and append N/C-terms:
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
# Compute the net charge according to the Henderson-Hesselbach equation:
for pH in range(0, 15):
    netCharge = (
        (sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) for x in ['y','c','d','e']}.values()))
    )
    print('pH = {0:.2f}'.format(pH), f': Net Charge = {netCharge}')
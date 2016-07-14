dictionary = open('dictionary.txt','r').read().split()
inputfile = open('output_prob_arith.txt','r').read().split()
outputfile = open('output_deprob_arith.txt','w+')
output = ""
for i in inputfile:
	if i.isdigit():
		output += dictionary[int(i)]            #if integer, replace with apt word, then add it to output
	else:
		output += i								#if word, add it to output 
	output += ' '
outputfile.write(output)

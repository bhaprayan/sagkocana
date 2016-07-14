#more than 3 minutes to compress. Very slow. Compression ratio around 1.4




input = open('input_file.txt','r').read()
from collections import defaultdict
from collections import OrderedDict
#import time
#start = time.time()
input_words = input.split()
d = defaultdict(int)                  
for word in input_words:
	d[word] += 1					#list converted to dictionary with frequency count
index = 0
d = sorted(d.items(), key=lambda item: item[1], reverse = True)      #dictionary sorted in descending order as per frequency count
e = OrderedDict(d)                        #index is introduced in the dictionary
#print len(input_words)
dictionaryfile = open('dictionary.txt','w+')
dictstring = ""											#dictstring will contain the dictionary words in a string separated by a space for further use
for i in e.keys():
	dictstring += i
	dictstring += ' '
dictionaryfile.write(dictstring)	
#count = 0
output = ""
for i in input_words:
	if len(i) < len(str(e.keys().index(i))):           #if len of word is less than len of index then use the word
		output = output + i
	else:
		output += str(e.keys().index(i))
	output = output +  ' '
	#count += 1
	#print count
outputfile = open('output_prob_arith.txt','w+')
outputfile.write(output)
compressedlength = len(output)
#print time.time() - start
print "Original size ", len(input)
print "Compressed size ",len(output)
print "Compression ratio ", float(len(input))/len(output)


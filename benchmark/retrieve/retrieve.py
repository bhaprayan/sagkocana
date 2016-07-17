import os
import urllib.request
'''
Checks to see whether the data is present.
To be used to check whether to download OR not.
Insert the name in the following format
'os.path.isfile('NAME_OF_FILE')
'''
#TEXT URLS
text_urls = open('./text_urls.txt').read().strip().split('\n')

for i in range(0,len(text_urls), 2):
	if not os.path.isfile('../' + text_urls[i]):
		print("Downloading: ", text_urls[i+1])
		urllib.request.urlretrieve(text_urls[i+1]
				, '../'+text_urls[i])
	else:
		print("The file ", text_urls[i], " is present!")

print("Downloading of data is complete!")

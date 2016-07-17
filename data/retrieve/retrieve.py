import os
import urllib.request
'''
Checks to see whether the data is present.
To be used to check whether to download OR not.
Insert the name in the following format
'os.path.isfile('NAME_OF_FILE')
'''
if not os.path.isfile('../DNA_TEST_1.txt'):
	urllib.request.urlretrieve(url, 'DNA_TEST_1.txt')


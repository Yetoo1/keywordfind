#python 2.7.12
#THIS IS WRITING TO FILES BECAUSE THIS IS DESIGNED FOR DOWNLOAD LISTS THAT WILL EVENTUALLY TAKE UP A LOT OF RAM. DOWNLOAD TO FILE, JUST READ ONE AT A TIME. PROBABLY HAVE THE WAY PYTHON INTERACTS WITH RAM WRONG, BUT JUST IN THE POSSIBILITY THAT I'M RIGHT. WHATEVER THE ANSWER IS, YOU'RE DOING THE RIGHT THING! THIS WILL EVENTUALL WANT OPTION FOR A SLECTION! THAT WOULD BE A LOT OF SHIT IN RAM!#####
#	 TODO LIST	#
#	      1. Have the folder that is going to be created to check the file permissions so that the program doesn't fuckup the user's shit.
#	      2. Make this less of a clusterfuck and make it go fast if possible, but at the least, make this less of a clusterfuck
#	      3. Clean of the folder and its contents that are left behind if the code doesn't complete correctly
#INSTALL DEBIAN CORE ON THE LAPTOP!!!!!!!!!!!!!!!!
import urllib2
import sys
import os
import shutil
import datetime
import argparse
aparse = argparse.ArgumentParser()
aparse.parse_args()
time = datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)
time = str(time.total_seconds())
thefolder_path=os.path.dirname(os.path.realpath(__file__)) + "/" + "urface" + time + "/"
if not os.path.exists(thefolder_path): #the same as doing a+b, but this code is special
	os.makedirs(thefolder_path)
	#print "Created Folder"
#check to see if each item in the list is true the the directory that you want
downloads = open('downloadlist.txt', 'r')
urlstring = downloads.read()
urlstring = urlstring.split("\n")
line = 0
a = 0
length = []
for i in urlstring:
	line += 1
	length.append(len(i))
#yeah, I guess I could search in the same loop, not even needing to write, but again, I don't want to spend the time now
actlength = max(length) 
for i in urlstring:
	if a == line-1:
		break	
	lookforstr = "+1234567890+@" + i + "+1234567890+@" #when the program actually looks for this, it needs to look on either side	
	#for x in range(0, actlength):
		#print "-",
	#	sys.stdout.write('-')
	#sys.stdout.flush()	
	print "\n"	
	print "Downloading: " + i 	
	response = urllib2.urlopen("%s" % i)
	html = response.read()
	#if shit doesn't work later, remember to html.split("\n")	
	files = open(thefolder_path + "html%d.txt" % a, "w")
	files.write(html + "\n" + lookforstr) #unrelated but if want to append something to the top of a written file later on, need to put whatever is in the file into a variable and then delete the original variable and then create a new file with the append shits at the fuck cat (top)
	files.close()
	print "Downloaded: " + i
	#this is a shitty verification method and it should get improved
	print "Verifying: " + i
	verify = open(thefolder_path + "html%d.txt" % a, 'r')	
	verify2 = verify.read()	
	if lookforstr in verify2:
		print "Verified: " + i
	else:
		print "Fuck something went wrong, exiting ..."
		verify.close()		
		exit() 
	verify.close()	
	a += 1
#this shit goes here because we want to download all the shit first, again, we could put this in memory but then the user's environment is also too variable
print "+==========downloadlist.txt==========+"
for i in urlstring:
	print i
thequestion = raw_input("Enter the string that you would like to find: ")
#then <insert search through files>, no this isn't going to end up like google shit because this is going to datamine what i want. This isn't data mining yet, but eventually i want the thing to ask if the data on a set of selected urls is sufficient for the purpose at hand, then the user will either put yes or no, but yes is assumed (not default) and then data mining occurs, but then the user can set how far the tool can go. Hey isn't this like wget, you bet it is, except my tool has less features and is meant for me, it is meant to systematically stalk on people mmmmm  
dlist = sorted(os.listdir(thefolder_path))
line = 0
a = 0
amntfound = 0
length = []
for i in urlstring:
	line += 1
for i in urlstring:
	if a == line-1:
		break	
	print "Searching through: " + i
	search = open(thefolder_path + "html%d.txt" % a, 'r')
	search2 = search.read()
	if thequestion in search2:
		print "Found " + thequestion
		amntfound += 1
	else:
		print thequestion + " was not found." 	
	a += 1
line = str(line - 1)
amntfound = str(amntfound)
print amntfound + " of the the " + line + " urls were found." 
#this is supposed to go at the very end of the instance, like it is now, 
#but keep it there
#this may not be needed later
shutil.rmtree(thefolder_path)
#print "Deleted Folder"	

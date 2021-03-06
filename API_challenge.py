import urllib2
import json
import datetime
import dateutil
import dateutil.parser

#all neccesary urls
email = 'aeisape1@jhu.edu'
github_url = 'https://github.com/aeisape/CODE2040'
reg_url = 'http://challenge.code2040.org/api/register'
get_rev_str_url = 'http://challenge.code2040.org/api/getstring'
send_rev_str_url = 'http://challenge.code2040.org/api/validatestring'
get_haystack_url = 'http://challenge.code2040.org/api/haystack'
send_haystack_url = 'http://challenge.code2040.org/api/validateneedle'
get_prefix_url = 'http://challenge.code2040.org/api/prefix'
send_prefix_url = 'http://challenge.code2040.org/api/validateprefix'
get_date_url = 'http://challenge.code2040.org/api/time'
send_date_url = 'http://challenge.code2040.org/api/validatetime'
	
def get_token(email, github_url):	#have to register first.., no recursion
	#my registration dictionary, might as well generalize, because reusable code is amazing
	reg_dict = {'email':email,'github':github_url}

	#makes it into a json object
	jdat = json.dumps(reg_dict)
		
	#the thing sent back after sending the registration info
	req = urllib2.Request(reg_url, jdat)
	
	#which is a file-like object, so it needs to be opened
	res = urllib2.urlopen(req)
	
	#and then read
	prt = res.read()
	
	#get token from what was sent back
	jsondata = json.loads(prt)
	
	token = jsondata['result']
	return token

#condense above into a function
def get_json(url):
	token = get_token(email, github_url)				#get my token
	jdict = {"token":token}			#put it in a dictionary
	jdat = json.dumps(jdict)		#convert to json
	req = urllib2.Request(url, jdat)#send
	res = urllib2.urlopen(req)		#response, file-like, so it needs to b opened
	data = res.read()				#and read
	jsondata = json.loads(data)		#convert to dictionary
	return jsondata					#return the dictionary
	
def send_json(url, _dict):
	jdat = json.dumps(_dict)		#convert given dictionary
	req = urllib2.Request(url, jdat)#send it
	res = urllib2.urlopen(req)		#get response
	data = res.read()				#read response
	jsondata = json.loads(data)		#convert response to dictionary
	return jsondata					#retunr thr dictionary
	
def reverse_string():
	
	data = get_json(get_rev_str_url)
	string = data['result']
	
	#print before and after reversal for diagnostic purpuses
	print string
	rev_str = string[::-1]	#<-SO truly is your friend
	print rev_str
	
	#now we need to send the reversed string back
	result = {'token':get_token(email, github_url), 'string':rev_str}
	data = send_json(send_rev_str_url , result)
	
	print data['result']	#print response for self-gratification
	print '============================================'
	
	#return for full test
	return data['result'][0:4]

def needle_in_haystack():
	datum = get_json(get_haystack_url)
	
	#get the needle
	needle = datum['result']['needle']
	
	#get the haystack
	haystack = datum['result']['haystack']
	
	#print for disgnostic purposes
	print needle
	print haystack
	print "finding needle " + needle + " in given haystack"
	
	#getting the index is simple
	index = haystack.index(needle)
	
	#print for self-gratification
	print "needle is at index " + str(index)
	result = {'token':get_token(email, github_url), 'needle':index}

	#send it on its way
	data = send_json(send_haystack_url, result)
	print data['result']
	print '============================================'
		
	#return for full test
	return data['result'][0:4]

def rm_prefix():
	#get some tasty json
	data = get_json(get_prefix_url)
	
	#get prefix and array to search
	prefix = data['result']['prefix']
	array = data['result']['array']
	
	#print for diagnostic purposes
	print "Prefix is " + prefix 
	print array
	
	j = 0
	for i in array:	#increments through values, need numbers
		if array[j].startswith(prefix): 
			del array[j]	#if a word starts with the prefix, delete it
		j = j+1
	print array
	
	#package and send
	result = {'token':get_token(email, github_url), 'array':array}
	data = send_json(send_prefix_url, result) #send result, get response
	
	print data['result']    #passed!!
	print '============================================'
		
	#return for full test
	return data['result'][0:4]
			
def dating_game():
	
	data = get_json(get_date_url)
	
	#get the date and interval
	le_date = data['result']['datestamp']
	interval = data['result']['interval']
	
	#print for diagnostic purposes
	print 'Given time ' + le_date
	print 'Given interval (secs) ' + str(interval)
	
	#convert date so that it can be manipulated
	le_int = int(interval)
	curr_date = dateutil.parser.parse(le_date)
	
	#increment date by given interval
	new_date = curr_date + datetime.timedelta(seconds = le_int)
	print 'Given interval applied to given time: ' + str(new_date)
	
	#tie it all up with a neat little bow
	result = {'token':get_token(email, github_url), 'datestamp':str(new_date)}
	data = send_json(send_date_url, result)
	
	#print the songs of our glory
	print data['result']
		
	print '============================================'
		
	#return for full test
	return data['result'][0:4]

def main():
	print "My token is " + get_token(email, github_url)
	
	rev = ''					#default, for full runthrough
	rev = reverse_string()		#works
	
	hay = ''					#default, for full runthrough
	hay = needle_in_haystack()	#works
	
	pre = ''					#default, for full runthrough
	pre = rm_prefix()           #works
	
	un_date = ''				#default, for full runthrough
	un_date = dating_game()		#works
	
	#currently passed all tests
	failed = 0
	
	#if any test fails, increment 
	if rev != 'PASS' or hay != 'PASS'  or pre != 'PASS'or un_date != 'PASS':
		failed = 1
		
	#prints an error assuming test simply does not pass or is not run
	if failed != 0:
		print '...'
		print 'Something went wrong, not all stages passed'
	
	#print stories of our sccuess
	else:
		print 'All stages passed! Great job, man!'

if __name__ == "__main__":
	main()

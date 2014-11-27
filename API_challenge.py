import urllib2
import json
import datetime
import dateutil
import dateutil.parser
#all neccesary urls
reg_url = 'http://challenge.code2040.org/api/register'
get_rev_str_url = 'http://challenge.code2040.org/api/getstring'
send_rev_str_url = 'http://challenge.code2040.org/api/validatestring'
get_haystack_url = 'http://challenge.code2040.org/api/haystack'
send_haystack_url = 'http://challenge.code2040.org/api/validateneedle'
get_prefix_url = 'http://challenge.code2040.org/api/prefix'
send_prefix_url = 'http://challenge.code2040.org/api/validateprefix'
get_date_url = 'http://challenge.code2040.org/api/time'
send_date_url = 'http://challenge.code2040.org/api/validatetime'
	
def get_token():	#have to register first.., no recursion
	#my registration dictionary
	reg_dict = {'email':'aeisape1@jhu.edu','github':'https://github.com/aeisape/CODE2040'}

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
	token = get_token()				#get my token
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
	result = {'token':get_token(), 'string':rev_str}
	data = send_json(send_rev_str_url , result)
	print data['result']	#print response for self-gratification
	print '============================================'

def needle_in_haystack():
	data = get_json(get_haystack_url)
	
	#get the needle
	needle = data['result']['needle']
	
	#get the haystack
	haystack = data['result']['haystack']
	
	#print for disgnostic purposes
	print needle
	print haystack
	print "finding needle " + needle + " in given haystack"
	
	#getting the index is simple
	index = haystack.index(needle)
	
	#print for self-gratification
	print "needle is at index " + str(index)
	result = {'token':get_token(), 'needle':index}

	#send it on its way
	data = send_json(send_haystack_url, result)
	print data['result']
	print '============================================'


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
	result = {'token':get_token(),'array':array}
	data = send_json(send_prefix_url, result) #send result, get response
	print data['result']    #passed!!
	print '============================================'
			
def dating_game():
	data = get_json(get_date_url)
	
	le_date = data['result']['datestamp']
	interval = data['result']['interval']
	
	print 'Given time ' + le_date
	print 'Given interval (secs) ' + str(interval)
	
	le_int = int(interval)
	curr_date = dateutil.parser.parse(le_date)
	
	new_date = curr_date + datetime.timedelta(seconds = le_int)
	print 'Given interval applied to given time: ' + str(new_date)
	
	result = {'token':get_token(), 'datestamp':str(new_date)}
	data = send_json(send_date_url, result)
	print data['result']	
	print '============================================'

	
	
def main():
	#print "My token is " + get_token()
	#reverse_string()		#works
	#needle_in_haystack()	#works
	#rm_prefix()             #works
	dating_game()

if __name__ == "__main__":
	main()

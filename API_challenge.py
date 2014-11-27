import urllib
import urllib2
import json
import requests
reg_url = 'http://challenge.code2040.org/api/register'
get_rev_str_url = 'http://challenge.code2040.org/api/getstring'
send_rev_str_url = 'http://challenge.code2040.org/api/validatestring'
get_haystack_url = 'http://challenge.code2040.org/api/haystack'
send_haystack_url = 'http://challenge.code2040.org/api/validateneedle'


def get_token():	#have to register first..
	#my registration dictionary
	reg_dict = {'email':'aeisape1@jhu.edu','github':'https://github.com/aeisape/CODE2040'}

	#makes it into a json object
	jdat = json.dumps(reg_dict)
	
	#the url to get the 
	#url = 'http://challenge.code2040.org/api/register'
	
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
	
def reverse_string():
	token = get_token()
	jdict = {"token":token}
	jdat = json.dumps(jdict)
	req = urllib2.Request(get_rev_str_url, jdat)
	res = urllib2.urlopen(req)
	prt = res.read()
	jsondata = json.loads(prt)
	string = jsondata['result']
	
	#print before and after reversal for diagnostic purpuses
	print string
	rev_str = string[::-1]	#<-SO truly is your friend
	print rev_str
	
	#now we need to send the reversed string back
	result = {'token':token, 'string':rev_str}
	jdat = json.dumps(result)
	req = urllib2.Request(send_rev_str_url, jdat)
	res = urllib2.urlopen(req)
	prt = res.read()
	jsondata = json.loads(prt)
	string = jsondata['result']
	print string	#print response for self-gratification

def needle_in_haystack():
	#same as before, should be a function
	token = get_token()
	jdict = {"token":token}
	jdat = json.dumps(jdict)
	req = urllib2.Request(get_haystack_url, jdat)
	res = urllib2.urlopen(req)
	prt = res.read()	
	jsondata = json.loads(prt)
	
	needle = jsondata['result']['needle']
	haystack = jsondata['result']['haystack']
	print needle
	print haystack
	print "finding needle " + needle + " in given haystack"
	index = haystack.index(needle)
	print index

def main():
	#print "My token is " + get_token()
	#reverse_string()	#works
	needle_in_haystack()

if __name__ == "__main__":
	main()

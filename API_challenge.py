import urllib
import urllib2
import json
import requests
reg_url = 'http://challenge.code2040.org/api/register'
get_rev_str_url = 'http://challenge.code2040.org/api/getstring'
send_rev_str_url = 'http://challenge.code2040.org/api/validatestring'

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
	sdat = json.dumps(result)
	req0 = urllib2.Request(send_rev_str_url, sdat)
	res0 = urllib2.urlopen(req0)
	prt0 = res0.read()
	jsondat = json.loads(prt0)
	rslt = jsondat['result']
	print rslt	#print response for self-gratification


def main():
	print "My token is " + get_token()
	reverse_string()	#works

if __name__ == "__main__":
	main()

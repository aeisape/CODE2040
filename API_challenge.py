import urllib2
import json

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
	string = data['result']
	print string	#print response for self-gratification

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
	success = data['result']
	print success

def rm_prefix():
	pass
	
	
def main():
	#print "My token is " + get_token()
	#reverse_string()		#works
	needle_in_haystack()	#works
	rm_prefix()

if __name__ == "__main__":
	main()

from API_challenge import get_json
from API_challenge import send_json 
from API_challenge import get_token
import API_challenge

github_url = 'https://github.com/aeisape/CODE2040'
check_grades_url = 'http://challenge.code2040.org/api/status'

def check_grade():
	token = get_token('aeisape1@jhu.edu', github_url)
	jdict = {'token':token}
	data = send_json(check_grades_url, jdict)
	print data['result']
	
def main():
	check_grade()
	
if __name__ == "__main__":
	main()

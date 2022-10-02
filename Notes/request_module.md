## Request Module
* The requests module allows you to send HTTP requests using Python.
* The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

### Download and Install the Requests Module
* Navigate your command line to the location of PIP, and type the following:
```bash
pip install requests 
```

### get() Method
* The get() method sends a GET request to the specified url.
```bash
import requests

x = requests.get('https://w3schools.com')
print(x.status_code)
```

### head() Method
* The head() method sends a HEAD request to the specified url.
* HEAD requests are done when you do not need the content of the file, but only the status_code or HTTP headers.
```bash
import requests

x = requests.head('https://www.w3schools.com/python/demopage.php')
print(x.headers) 
```

### post() Method
* The post() method sends a POST request to the specified url.
* The post() method is used when you want to send some data to the server.
```bash
import requests

url = 'https://www.w3schools.com/python/demopage.php'

# 01 . data : Optional. A dictionary, list of tuples, bytes or a file object to send to the specified url
myobj = {'somekey': 'somevalue'}
x = requests.post(url, json = myobj)
#print the response text (the content of the requested file):
print(x.text)

# 02 . json : Optional. A JSON object to send to the specified url
myjson = {'somekey': 'somevalue'}
x = requests.post(url, json = myjson)
#print the response text (the content of the requested file):
print(x.text)

# 03 . files :  Optional. A dictionary of files to send to the specified url
myfiles = {'file': open('myfirstreact.png' ,'rb')}
x = requests.post(url, files = myfiles)
#print the response text (the content of the requested file):
print(x.text)
```

### delete() Method
* The delete() method sends a DELETE request to the specified url.
* DELETE requests are made for deleting the specified resource (file, record etc).
* Make a DELETE request to a web page, and return the response text:
```bash
import requests

x = requests.delete('https://w3schools.com/python/demopage.php')

print(x.text) 
```

### patch(url, data, args)
* Sends a PATCH request to the specified url

### put(url, data, args)
* Sends a PUT request to the specified url

### request(method, url, args)
* Sends a request of the specified method to the specified url

### Parameters:
* parameters are used with **any request methods**(GET,POST,PUT,PATCH,DELETE).Below we have use DELETE only to give example.
```bash
import requests
url = 'https://w3schools.com/python/demopage.php'

# 01 : allow_redirects : Optional. A Boolean to enable/disable redirection. Default True.
#Sometimes the server redirects a request, could be if the file does not exist etc., set the 'allow_redirects' parameter to False to deny redirects:
x = requests.delete(url, allow_redirects=False)
#print the response text (the content of the requested file):
print(x.text)

# 02 : auth : Optional. A tuple to enable a certain HTTP authentication.Default None
#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.delete(url, auth = ('user', 'pass'))
print(x.status_code)
 
# 03 : cert : Optional. A String or Tuple specifying a cert file or key.Default None
#specify a cert to use as a client side certificate by setting the 'cert' parameter:
x = requests.delete(url, cert='folder/myclient.cert')
print(x.status_code)

# 04 : cookies : Optional. A dictionary of cookies to send to the specified url.Default None
#use the 'cookies' parameter to send cookies to the server:
x = requests.delete(url, cookies = {"favcolor": "Red"})
print(x.status_code)

# 05 : header : Optional. A dictionary of HTTP headers to send to the specified url.Default None
#use the 'headers' parameter to set the HTTP headers:
x = requests.delete(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
print(x.status_code)

# 06 : proxy : Optional. A dictionary of the protocol to the proxy url.Default None
#find a free proxy address and send your request via that proxy:
x = requests.delete(url, proxies = { "https" : "https://1.1.0.1:80"})
print(x.status_code)

# 07 : steam : Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).Default False
#allow the response to be streamed by setting the 'stream' parameter to True:
x = requests.delete(url, stream=True)
print(x.status_code)

# 08 : verify : Optional. A Boolean or a String indication to verify the servers TLS certificate or not.Default True
#make the request with the path to a TLS certificate:
x = requests.delete(url, verify='folder/tlscertificate')
print(x.status_code)
#make the request and specify that there will be no verifying:
x = requests.delete(url, verify=False)
print(x.status_code)

# 09 : timeout : Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.Default None which means the request will continue until the connection is closed
#to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
x = requests.head(url, timeout=0.001)

print(x.status_code)
```


## Python requests.Response Object
* **Definition and usage** : The requests.Response() Object contains the server's response to the HTTP request.
```bash
import requests
url = 'https://w3schools.com/python/demopage.htm'
x = requests.get(url)

# 01 : apparent_encoding : Returns the apparent encoding
print(x.apparent_encoding) 

# 02 : close()
#close the connection to the server:
x.close()

# 03 : content : Returns the content of the response, in bytes
print(x.content)

# 04 : cookies :  Returns a CookieJar object with the cookies sent back from the server
print(x.cookies)

# 05 : elapsed : Returns a timedelta object with the time elapsed from sending the request to the arrival of the response
print(x.elapsed)

# 06 : encoding :  Returns the encoding used to decode r.text
print(x.encoding)

# 07 : headers : Returns a dictionary of response headers
print(x.headers)

# 08 : history : Returns a list of response objects holding the history of request (url)
print(x.history)

# 09 : is_permanent_redirect : Returns True if the response is the permanent redirected url, otherwise False
print(x.is_permanent_redirect)

# 10 : is_redirect : Returns True if the response was redirected, otherwise False
print(x.is_redirect)

# 11 : iter_content() : Iterates over the response
#return an iterator, one item for each character:
print(x.iter_content())

#looping through the iterator:
for c in x.iter_content():
  print(c)
  

# 12 : iter_lines() : Iterates over the lines of the response
#return an iterator, one item for each line:
print(x.iter_lines())

#looping through the iterator:
for c in x.iter_content():
  print(c)

# 13 : json()  :Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)
print(x.json())

# 14 : links : Returns the header links
print(x.links)

# 15 : next : Returns a PreparedRequest object for the next request in a redirection
print(x.next)

# 16 : ok : Returns True if status_code is less than 400, otherwise False
print(x.ok)

# 17 : raise_for_status() : If an error occur, this method returns a HTTPError object
print(x.raise_for_status())

# 18 : reason : Returns a text corresponding to the status code
print(x.reason)

# 19 : request : Returns the request object that requested this response
print(x.request)

# 20 : status_code : Returns a number that indicates the status (200 is OK, 404 is Not Found)
print(x.status_code)

# 21 : text : Returns the content of the response, in unicode
print(x.text)

# 22 : url : Returns the URL of the response
print(x.url)
```

### Important resources
* [Python request response object - for all response type in python](https://www.w3schools.com/python/ref_requests_response.asp)
* [Python request module](https://www.w3schools.com/python/module_requests.asp)
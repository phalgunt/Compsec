#Worked with Ange Ishimwe
from pymd5 import md5, padding
import http.client, urllib.parse, sys, urllib.request, urllib.parse, urllib.error, math, requests
url = sys.argv[1]
parsedUrl = urllib.parse.urlparse(url)
m = parsedUrl.query.split('&', 1)[1]
#print('Query is: ', query)
token = parsedUrl.query.split('=')[1].split('&')[0]
#print('Token is: ', token)
unlockAllSafes = '&command=UnlockAllSafes'
length_of_m = 8 + len(m)
bits = (length_of_m + len(padding(length_of_m * 8))) * 8
h = md5(state=bytes.fromhex(token), count=bits)
h.update(unlockAllSafes)
newToken = urllib.parse.quote(h.hexdigest())
newUrl='https://project1.ecen4133.org/phta6996/lengthextension/api?token='+newToken+'&'+m+\
         urllib.parse.quote(padding(length_of_m * 8)) + unlockAllSafes
print(newUrl)

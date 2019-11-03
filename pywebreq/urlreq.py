import urllib.request
# Hi this is just a commen
x = urllib.request.urlopen(
    'https://www.google.co.in/')
print(x.read())

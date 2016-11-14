import urllib.request
file = urllib.request.urlopen('https://helloworldbook.com/data/message.txt');
message = file.read();
print(message);
import urllib.request

try:
    a=urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print('O site não está acessivel.')
else:
    print('O site está acessível.')
    print(a.read())
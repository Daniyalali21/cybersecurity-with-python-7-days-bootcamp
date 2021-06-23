import requests;

r = requests.get('https://xkcd.com/333/');

with open('comic.png','wb') as f:

    f.write(r.content); 
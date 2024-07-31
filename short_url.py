import pyshorteners

long_url = 'https://jurados.github.io/'

def shorten_url(url: str) -> str:
	s = pyshorteners.Shortener()
	return print(s.tinyurl.short(url))

if __name__ == '__main__':
	shorten_url(long_url)




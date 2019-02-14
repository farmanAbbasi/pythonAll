import requests
from bs4 import BeautifulSoup

def getAvailableMovies():
	parsed_movies={}
	res = requests.get('https://in.bookmyshow.com/hyderabad/movies')
	print(res.status_code)
	soup = BeautifulSoup(res.text,features="html.parser")
	movies = soup.findAll("div",{"class":"card-container wow fadeIn movie-card-container"})
	for movie in movies:
	    pass
	#	print(movie["data-title"])#accessing the class
	#	print(str(movie.h4.text)) #acccessing the other stuffs
	res2=requests.get('https://in.bookmyshow.com/buytickets/badhaai-ho-hyderabad/movie-hyd-ET00068588-MT/20181102#!seatlayout')
	soup2=BeautifulSoup(res2.text,features="html.parser")

	seatData=soup2.findAll("div",{"class":"seatP"}).find("td",{"class":"seatR Setrow1"}).findAll("td")
	
	


	
getAvailableMovies()	
import requests
from bs4 import BeautifulSoup

def getAvailableMovies():
	parsed_movies={}
	parsed_movies = {'sample':[12,20]}
	
	print (parsed_movies)

	res = requests.get('https://in.bookmyshow.com/hyderabad/movies')
	print(res.status_code)

	acceptableVenues = ['PVR: Inorbit, Cyberabad','PVR ICON: Hitech, Madhapur, Hyderabad','PVR Forum Sujana Mall: Kukatpally, Hyderabad']

	if res.status_code == 200:
		message = "movie update "
		soup = BeautifulSoup(res.text,features="html.parser")
		movies = soup.findAll("div",{"class":"card-container wow fadeIn movie-card-container"})
		for movie in movies:
			if movie["data-language-filter"] == '|Hindi' or movie["data-language-filter"] == '|English':
				eachMovieRes = requests.get('https://in.bookmyshow.com'+movie.a["href"])
				eachMovieSoup = BeautifulSoup(eachMovieRes.text,features="html.parser")
				try:
					percentage = eachMovieSoup.find("span",{"class":"__percentage"}).text
				except:
					percentage = '10%' #new movie
				if int(percentage[0:-1])>84:
					eachMovieDateRes = requests.get('https://in.bookmyshow.com'+eachMovieSoup.find("div",{"class":"more-showtimes"}).a["href"])
					eachMovieDateSoup = BeautifulSoup(eachMovieDateRes.text,features="html.parser")
					allDates = eachMovieDateSoup.find("ul",{"id":"showDates"}).findAll("li")
					for eachDate in allDates:
						# print eachDate.a["href"]
						eachMovieDateTmeRes = requests.get('https://in.bookmyshow.com'+eachDate.a["href"])
						eachMovieDateTimeSoup = BeautifulSoup(eachMovieDateTmeRes.text,features="html.parser")
						allVenues = eachMovieDateTimeSoup.find("ul",{"id":"venuelist"}).findAll("li")
						for eachVenue in allVenues:
							if eachVenue["data-name"] in acceptableVenues:
								allAvailabilityforEachVenue = eachVenue.find("div",{"class":"body"}).findAll("div",{"data-online":"Y"})
								for eachTime in allAvailabilityforEachVenue:
									# if eachAvailabilityforEachVenue["class"] != '_sold':
									# file.write(str(movie.h4.text)+",")
									for seatClass in eval(eachTime.a["data-cat-popup"]):
										if seatClass['availabilityText'] == 'Available':
											if str(movie.h4.text) in parsed_movies:
												if str(eachDate.a.div.text[0:2]) in parsed_movies[movie.h4.text]:
													#movie and date both exists so do nothing
													continue
												else:
													# movie exist but not date so add date
													message += str(movie.h4.text)+" "+str(eachDate.a.div.text[0:2])+" "+str(eachVenue["data-name"][0:10])+" "+str(eachTime.a["data-display-showtime"]+", ")
													parsed_movies[str(movie.h4.text)].append(str(eachDate.a.div.text[0:2]))
											else:
												# movie does not exist
												message += str(movie.h4.text)+" "+str(eachDate.a.div.text[0:2])+" "+str(eachVenue["data-name"][0:10])+" "+str(eachTime.a["data-display-showtime"]+", ")
												parsed_movies[str(movie.h4.text)] = [str(eachDate.a.div.text[0:2])]
									# file.write(movie.h4.text+eachDate.a.div.text[0:2]+eachVenue["data-name"]+eachTime.a["data-display-showtime"]+",")
	return message
print(getAvailableMovies())
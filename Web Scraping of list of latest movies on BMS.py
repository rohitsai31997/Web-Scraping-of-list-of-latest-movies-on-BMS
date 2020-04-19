#In this program, we will scrap data from BMS website to track the latest upcoming movies
#Step - 1 Crawling
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://in.bookmyshow.com/hyderabad/movies/comingsoon"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

response = requests.request("GET", url, headers= headers)
Web_Data = BeautifulSoup(response.text, 'html.parser')

#Step - 2 Parsing and Transforming
movie_data = Web_Data.find_all('div', attrs = {'class', 'cards cs-card-regular'})
#print(movie_data)
#print(len(movie_data))

for movie in movie_data:
    Movie_Name = movie.find('h4')
    Movie_Date = movie.find('span', attrs ={'class', 'day'})
    Movie_Language = movie.find('li', attrs ={'class',  '__language'})
    #print(Movie_Name.text, Movie_Date.text, Movie_Language.text)

# Step - 3 Storing of the extracted data in the CSV file

file = []
for movie in movie_data:
    movie_details = {}
    Movie_Name = movie.find('h4')
    Movie_Date = movie.find('span', attrs={'class', 'day'})
    Movie_Language = movie.find('li', attrs={'class', '__language'})
    movie_details['Movie_Name'] = Movie_Name.text
    movie_details['Movie_Date'] = Movie_Date.text
    movie_details['Movie_Language'] = Movie_Language.text
    file.append(movie_details)

dataframe = pd.DataFrame.from_dict(file)
dataframe.to_csv('movie_data.csv', index = False)
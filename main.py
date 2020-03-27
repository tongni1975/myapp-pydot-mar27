# import flask
import os
from flask import Flask, request, render_template
import requests

news_template = 'http://newsapi.org/v2/top-headlines?country=%s&category=general'
weather_template = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s'

#heys from environment

WEATHER_KEY = os.environ['WEATHER_KEY']
NEWS_KEY = os.environ['NEWS_KEY']

news_headers = { 'X-Api-Key': NEWS_KEY }

# create a flask app
app = Flask(__name__, static_folder='./static', template_folder='./templates')

@app.route('/weather-news', methods=['GET'])
def weather_news():
   city = request.args['city']

   # get the weather
   weather_url = weather_template %(city, WEATHER_KEY)
   resp = requests.get(weather_url)
   weather_json = resp.json()
   weather = [ '%s - %s' %(i['main'], i['description']) for i in weather_json['weather'] ]
   country_code = weather_json['sys']['country'].lower()

   # get the news
   news_url = news_template %country_code
   resp = requests.get(news_url, headers=news_headers)
   news_json = resp.json()
   news = []
   for art in news_json['articles']:
      news.append({ 'title': art['title'], 'url': art['url'], 'image': art['urlToImage'] })

   return render_template('weather-news.html', city=city.upper(), news=news, weather=weather)

# loading from static folder
@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/<path:mypath>', methods=['GET'])
def resources(mypath):
    print('mypath: ', mypath)
    return app.send_static_file(mypath)

# run flask
if '__main__' == __name__:
    # get the PORT from the environment variable
    #provided by heroku
    app.run(port=os.environ['PORT'], debug=False, host='0.0.0.0')


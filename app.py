from flask import Flask, render_template, request, redirect, url_for

# importing requests module to call the API
import requests

# to display the day on the web page. Possibly.
import datetime

# to work with JSON data & convert it to python code
import json

# might be needed for pattern matching. 
import re


app = Flask(__name__)

api_key = "api_key_goes_here"




@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        entered_city = request.form.get('search_box').strip()
        print(entered_city)
        print(type(entered_city))

        api_location = entered_city
        api_string = f"api_url_goes_here?q={api_location}&units=metric&appid={api_key}"

        response = requests.get(api_string)

        if response.status_code == 200:
            print('The city was found in the API!')
            response_in_json = response.text
            print(response_in_json)

            # converting to python dictionaries... which look almost identical to json
            converted_response = json.loads(response_in_json)

            city_name = converted_response['name']
            country_name = converted_response['sys']['country']

            current_temperature = converted_response['main']['temp']
            print("Current temp is: " + str(current_temperature))

            feels_like = converted_response['main']['feels_like']
            print("Feels like: " + str(feels_like))

            pressure = converted_response['main']['pressure']
            print('Pressure is at: ' + str(pressure))

            humidity = converted_response['main']['humidity']
            print('Humidity is at: ' + str(humidity))

            visibility = converted_response['visibility']
            print('visibility is at: ' + str(visibility))

            wind = converted_response['wind']['speed']
            print('wind speed is at: ' + str(wind))


            weather_data = {
                "name": city_name,
                "country": country_name,
                "current_temp": current_temperature,
                "feels_like": feels_like,
                "pressure": pressure,
                "humidity": humidity,
                "visibility": visibility,
                "wind": wind
            }

            return render_template("index.html", weather_display=weather_data)
        else:
            return redirect(url_for('main'))
    return render_template('index.html')





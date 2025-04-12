import requests
import json
import pprint

def main():
    appid="6620adbdca1f561b30ab5e6c8c754a78"
    URL = "http://api.openweathermap.org/data/2.5/weather"
    PARAMS = {"q": "Botosani", "appid": appid, "units": "metric", "lang": "RO"}
    try:
        response = requests.get(url=URL, params=PARAMS)   
        #On successful response, we'll get a status code of 200, so comparing
        # if the request was successful. 
        if response.status_code == 200:
            print("Request was Successful")
            
            data = response.json()
            pprint.pprint(data)
        else:
            print("Request was not Successful")
 #Handling any exceptions that may occur
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("Request was not Successful")













if __name__ == "__main__":
    main()
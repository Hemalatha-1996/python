import requests

API_KEY="53a6bd661ddc05342e3d4f4265bc4630"

def get_data(place,forecastdays=None):

    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    n_values=int(8*forecastdays)
    filtered_data=filtered_data[:n_values]
    return filtered_data


  
    







import requests
import openapi

# Make a get request to get the pc part picker api api.
response = requests.get("http://github.com/ncwick96/Computer-Parts-Aggr/blob/master/pcpartpicker.py/")

# Print the status code of the response.
print(response.status_code)

# Set up the parameters we want to pass to the API.
parameters = {"RAM: 16gb","Heat_Sink"}

# Make a get request with the parameters.
#response = requests.get("http://github.com/ncwick96/Computer-Parts-Aggr/blob/master/pcpartpicker.py/", params=parameters)

# Print the content of the response (the data the server returned)
print(response.content)


# Assumes that the key is plaintext
# Returns the API key stored in the file found at relative path C:\Users\Parker.DRAGON.001\Documents\CNA\CNA 330\Computer-Parts-Aggr\test_APIkey.txt
def get_api_key_from_file():
    with open(r'''C:\Users\Parker.DRAGON.001\Documents\CNA\CNA 330\Computer-Parts-Aggr\test_APIkey.txt''') as f:
        return f.read()


#reads the pcpartpicker.py file in our github repository
    uri += region + "github.com/ncwick96/Computer-Parts-Aggr/blob/master/pcpartpicker.py/"
    uri += achievement_id + "?locale=" + locale + "&apikey=" + apikey
    verboseprint(url)
    return uri



  #  uri = build_achievement_request(request_args)
    response = requests.get(uri)
    print(response.json())
    print(url)

#if __name__ == '__main__':

import requests
import openapi

# Make a get request to get the pc part picker api api.
req = requests.get("https://www.mouser.com/")

# Print the status code of the response.
result = "print(response.status_code)"

# Set up the parameters we want to pass to the API.
params = {"16gb","Corsair"}

# Make a get request with the parameters.
# response = requests.get("http://github.com/ncwick96/Computer-Parts-Aggr/blob/master/pcpartpicker.py/"


# Print the content of the response (the data the server returned)
rescon = "print(response.content)"


# Assumes that the key is plaintext
# Returns the API key stored in the file found at relative path ".\APIS\Mouser Electronics.txt"
def get_api_key_from_file():
    with open(r'''.\APIS\Mouser Electronics.txt''') as f:
        return f.read()


# reads the pcpartpicker.py file in our github repository
#   url += region + "github.com/ncwick96/Computer-Parts-Aggr/blob/master/pcpartpicker.py/"
#   url += achievement_id + "?locale=" + locale + "&apikey=" + apikey
#   verboseprint(url)
#   return url


    url += region + "https://mouser.com"
    return url
    result
    rescon

    url = build_achievement_request(request_args)
    response = requests.get(url)
    print(response.json())
    print(url)

#if __name__ == '__main__':

import tweepy # Tweepy is the library we use to connect to the Twitter API and makes things a whole lot easier
from configparser import ConfigParser # I am using the configparser library as a way of hiding my keys and secrets so other people can't use them

config_object = ConfigParser()
config_object.read('../twitter.ini')
keys = config_object["KEYS"]


# Authenticate to Twitter
auth = tweepy.OAuthHandler(keys["apikey"], keys["apisecret"])
auth.set_access_token(keys["accesstoken"], keys["accesssecret"])

# Create API object
api = tweepy.API(auth)

# Attempt to get a connection to twitter
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication") # If the connection fails it will output this massage to the user

# The input function allows you to enter a text prompt for the user, and save their input as place_id
place_id = input("Enter a WOEID here to see the latest Twitter trends for that area: \n");

trends_result = api.trends_place(int(place_id)); # api.trends_place() will return a dictionary of lots of values inside of a list
print(f'Here are the twitter trends for {place_id}:')
for trend in trends_result[0]["trends"]: # We are only interested in the trends value of the dictionary
    print(trend['name'])




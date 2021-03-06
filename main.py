import tweepy
import keys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Selecting a User
tweetOfGod = api.get_user('TheTweetOfGod')

# Check what is returned with
# returns: tweepy.models.User
type(tweetOfGod)

# Check ID
# returns: 204832963
tweetOfGod.id

# Check Name
# returns: God
tweetOfGod.name

# Check Screen name
# returns: TheTweetOfGod
tweetOfGod.screen_name

# Getting the most recent tweet
tweetOfGod.status.text


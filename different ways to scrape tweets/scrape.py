#Before scraping tweets using Python, you need access via Twitter's API. This access is easily attainable through Twitter's developer platform https://developer.twitter.com/en.

#If you have a Twitter account, you can use that to sign in to the developer platform. If not, you can create one easily. After signing in, you want to select the option to explore API, which will require you to add more information. Next, you should click the option to "create an app" and specify its name and description. After that, Twitter will provide you with your app's keys and tokens which you can use in Python for tweets extraction.

!pip install tweepy
import tweepy

#The below code shows the necessary keys that should be available in your developer portal after Twitter has approved your application. Here there are two things essential to note about your keys and access:
#1. Your keys will only be revealed once and should be stored secretly. Otherwise, you'll always be generating new keys
#2. You can only access tweets as far back as a week unless you're granted access to a research API, which is not to be used for commercial purposes. Read the documentation here https://developer.twitter.com/en/docs/twitter-api

#Input API credentials from Twitter app developer account
consumer_key= 'insert'
consumer_secret= 'insert'
access_token= 'insert'
access_token_secret= 'insert'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#After adding your keys you can choose to scrape tweets by keyword, from a particular user or replies to a particular tweet

#This code is if you want to search tweets by keyword.  
query = 'LoveIsland' #query means that tweets containing what you specify will be scraped
max_tweets = 3000 #you can specify how many tweets you want or python will collect only 100
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items()]

#After searching tweets by keyword use this to create datafram including things like no. of likes, retweets and date created
my_list_of_dicts = []
for each_json_tweet in searched_tweets:
    my_list_of_dicts.append(each_json_tweet._json)

    
with open('tweet_json_Data.txt', 'w') as file:
        file.write(json.dumps(my_list_of_dicts, indent=4))

        
my_demo_list = []
with open('tweet_json_Data.txt', encoding='utf-8') as json_file:  
    all_data = json.load(json_file)
    for each_dictionary in all_data:
        tweet_id = each_dictionary['id']
        text = each_dictionary['text']
        favorite_count = each_dictionary['favorite_count']
        retweet_count = each_dictionary['retweet_count']
        created_at = each_dictionary['created_at']
        my_demo_list.append({'tweet_id': str(tweet_id),
                             'text': str(text),
                             'favorite_count': int(favorite_count),
                             'retweet_count': int(retweet_count),
                             'created_at': created_at,
                            })
        
        tweet_dataset = pd.DataFrame(my_demo_list, columns = 
                                  ['tweet_id', 'text', 
                                   'favorite_count', 'retweet_count', 
                                   'created_at'])
        

#This code is if you want to search tweets by username
user = "@username"

tweets = tw.Cursor(api.user_timeline,
                   screen_name = user,
                   count = None,
                   since_id = None,
                   max_id = None, trim_user = True, exclude_retweets = True, contributor_details = False,
                   include_entities = False).items(2000);
df = pd.DataFrame(data =[tweet.text for tweet in tweets], columns = ["Tweet"]) #save user tweets to dataframe


#This code is if you want to search replies to a particular tweet
name = '@username'
target_tweet_id = "1562042561031815168" #this is the id of the particular tweet and can be found in the url link
 
replies=[]
for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(1000):
   if hasattr(tweet, 'in_reply_to_status_id_str'):
       if (tweet.in_reply_to_status_id_str==target_tweet_id):
           replies.append(tweet)
 
tweet_pd = pd.DataFrame(replies)







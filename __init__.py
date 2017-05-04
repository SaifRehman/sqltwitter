from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import MySQLdb
from dateutil import parser
HOST = ""
USER = ""
PASSWD = ""
DATABASE = ""
def set(HOSTval,USERval,PASSWDval,DATABASEval):
    HOST = HOSTval
    USER = USERval
    PASSWD = PASSWDval
    DATABASE = DATABASEval
def store_data(created_at, text, screen_name, tweet_id):
    db=MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DATABASE, charset="utf8")
    cursor = db.cursor()
    insert_query = "INSERT INTO tweet (tweet_id, screen_name, created_at, tweet) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (tweet_id, screen_name, created_at, text))
    db.commit()
    cursor.close()
    db.close()
    return
class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            #grab the wanted data from the Tweet
            text = datajson['text']
            screen_name = datajson['user']['screen_name']
            tweet_id = datajson['id']
            created_at = parser.parse(datajson['created_at'])
            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))
            #insert the data into the MySQL database
            store_data(created_at, text, screen_name, tweet_id)
        except Exception as e:
            print(e)
        return True
    def on_error(self, status):
        print status
def joke(consumer_key,consumer_secret,access_token,access_token_secret,values):
    if __name__ == '__main__':
        #This handles Twitter authetification and the connection to Twitter Streaming API
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
        stream.filter(track=values)

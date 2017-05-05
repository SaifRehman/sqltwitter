from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import MySQLdb
from dateutil import parser
global HOST
global USER
global PASSWD
global DATABASE
def setdb(HOSTval,USERval,PASSWDval,DATABASEval):
    global HOST
    global USER
    global PASSWD
    global DATABASE
    HOST = HOSTval
    USER = USERval
    PASSWD = PASSWDval
    DATABASE = DATABASEval
def store_data(created_at, text, screen_name, tweet_id):
    db=MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DATABASE, charset="utf8")
    cursor = db.cursor()
    cursor.execute("select * from information_schema.tables where table_name=%s", ('tweet',))
    if(bool(cursor.rowcount)):
        insert_query = "INSERT INTO tweet (tweet_id, screen_name, created_at, tweet) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (tweet_id, screen_name, created_at, text))
        db.commit()
        cursor.close()
        db.close()
        return
    else:
        cursor.execute("CREATE TABLE tweet (postid serial PRIMARY KEY NOT NULL , tweet_id varchar(200) NOT NULL , screen_name text NOT NULL, created_at text NOT NULL, tweet text NOT NULL);")
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
            print self
        return True
    def on_error(self, status):
        print status
def server(consumer_key,consumer_secret,access_token,access_token_secret,values):
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=values)

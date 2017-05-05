import tweetminer
tweetminer.setdb("HOST","USER","PASSWD","DATSBASE")
if __name__ == '__main__':
    tweetminer.server("consumer_key","consumer_secret","access_token","access_token_secret",['#tags'])

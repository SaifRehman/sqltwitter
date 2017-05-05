from setuptools import setup

setup(name='tweetminer',
      version='0.1',
      description='Mine for tweets with certain hashtag',
      author='saif rehman',
      author_email='saif.urrehman@alasbab.com',
      license='MIT',
      packages=['tweetminer'],
      install_requires=['tweepy','MySQL-python','textblob'],
      keywords = ['testing', 'logging', 'example','twitter','mining'],
      zip_safe=False)

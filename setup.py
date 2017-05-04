from setuptools import setup

setup(name='sqltwitter',
      version='0.1',
      description='Mine for tweets with certain hashtag',
      author='saif rehman',
      author_email='saif.urrehman@alasbab.com',
      license='MIT',
      packages=['sqltwitter'],
      install_requires=['tweepy','MySQL-python'],
      keywords = ['testing', 'logging', 'example','twitter','mining'], # arbitrary keywords
      zip_safe=False)

# Twitter Bot

This solution/tutorial is meant to produce a very simple twitter bot that generates random sentences based on a list of sentences and tweets them out on a schedule.

I <3 constructive criticism, so if you think there's something that could have been done better don't hesitate to contact me or submit a pull request- I'd love to discuss it.

<i>*This is a work in progress.</i>

### Prerequisites

* A twitter account with a verified email. This will be the account that tweets.
* A Heroku account. Heroku is a cloud platform. The free account is strong enough to host this bot. See the 'Setting Up Heroku' section for more details.
* It's helpful to have a computer that can execute .py (Python) scripts.

### Setting Up Your Twitter Account

### Generating Random Sentences

The bot.py script that was provided is what will run on the cloud. It generates a random sentence, tweets it, and then sleeps for a given amount of time.

The code generates the random sentence by randomly choosing words that appear next to one another from the sentences provided in sentences.txt. If you haven't made any changes to the solution, sentences.txt will contain the poem <i>There is Another Sky</i> by Emily Dickinson. Change this as desired. Sentences need to be in the format that this poem is in. Each one needs a new line, and to end with either a period (.), question mark (?), or exclamation point (!).

##### Optional Testing/Understanding

Let's modify bot.py so that we can generate a random sentence and print it out rather than tweet it. Try replacing your main function in bot.py with this new one:

```python
def main():
    # TODO
    CONSUMER_KEY = 'Your Consumer Key'
    CONSUMER_SECRET = 'Your Consumer Secret'
    ACCESS_KEY = 'Your Access Key'
    ACCESS_SECRET = 'Your Access Secret'
    # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    # api = tweepy.API(auth)

    n = [1, 2, 2]
    s = random.choices(n)
    oldSentence = ""
    sentence = ""
    # while (True):
    try:
        for i in range(0, s[0]):
            if i == 0:
                sentence = getRandomSentence()
            sentence += " " + getRandomSentence()
        if sentence[-1:] != '?' or sentence[-1:] != '!':
            sentence = sentence[:-1]
        allCaps = IsAllCaps()
        if allCaps:
            sentence = sentence.upper()
        print(sentence)
        # api.update_status(sentence)
    except Exception as Error:
        print(Error)
        # api.update_status("Although there's a chance this may error as well, 
        # + "this is where you can have your bot tweet when something goes wrong. 
        # + "I recommend including your '@' so that you receive a notification.")
    # time.sleep(7200)
```

I've commented out everything related to twitter, and it no longer runs on a loop.

Now you can run the script:

![](/readme_pictures/testrun.PNG)

And you'll see that it used the poem to generate a random sentence. 

If you get an error related to tweepy, use pip to install it.

### Setting Up Heroku
from os import environ
from random import shuffle
from random import randrange
import tweepy
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer  # Load the popular external library

mixer.init()
# Add the full path of the mp3 file
playlist = ['/Users/davidha/PycharmProjects/Twitter-Guessing-Game/Lovebug.mp3',
            '/Users/davidha/PycharmProjects/Twitter-Guessing-Game/34+35.mp3',
            '/Users/davidha/PycharmProjects/Twitter-Guessing-Game/music/Shape_of_you.mp3',
            '/Users/davidha/PycharmProjects/Twitter-Guessing-Game/music/sugar.mp3',
            '/Users/davidha/PycharmProjects/Twitter-Guessing-Game/music/rude.mp3',
            '/Users/davidha/PycharmProjects/Twitter-Guessing-Game/music/count_on_me.mp3',
            '/Users/davidha/PycharmProjects/Twitter-Guessing-Game/music/sunflower.mp3'
            ]
shuffle(playlist)
shuffle(playlist)
mixer.music.load(playlist.pop())
mixer.music.set_volume(.8)
mixer.music.play()
mixer.music.queue(playlist.pop())

print("Welcome to the Twitter Guessing Game! Please wait while we load tweets for Kanye West and Elon Musk")

people = ['George Takei @GeorgeTakei', 'Jeff Weiner @jeffweiner', 'Alexia Tsotsis @alexia',
          'Dan Primack @danprimack', 'Marissa Mayer @marissamayer', 'Kim Dotcom @KimDotcom',
          'Arianna Huffington @ariannahuff', 'PewDiePie @pewdiepie', 'Vani Hari @thefoodbabe',
          'Beyoncé @Beyonce', 'Lorde @lorde', 'The White House @WhiteHouse',
          'Barack Obama @BarackObama', 'Pope Francis @Pontifex', 'J.K. Rowling @jk_rowling',
          'Michelle Obama @MichelleObama', 'Melissa Stewart @MelissaOnline', 'Steve Forbes @SteveForbesCEO',
          'Sir Richard Branson @RichardBranson', 'Steve Case @SteveCase', 'Bill Gates @BillGates',
          'Anne-Marie Slaughter @SlaughterAM', 'Jeff Weiner @jeffweiner', 'Elizabeth Warren @SenWarren',
          'Debora Spar @deboraspar', 'Padmasree Warrior @padmasree', 'Anna Maria Chávez @AnnaMariaChavez',
          'Gloria Steinem @gloriasteinem', 'Aileen Lee @aileenlee', 'Dwayne Johnson @TheRock',
          'Kanye West @kanyewest', 'Serena William @serenawilliams', 'Katy Perry @katyperry',
          'Justin Bieber @justinbieber', 'Taylor Swift @taylorswift13', 'Youtube @YouTube',
          'Rihanna @rihanna', 'Ellen DeGeneres @TheEllenShow', 'Lady Gaga @ladygaga',
          'Justin Timberlake @jtimberlake', 'Britney Spears @britneyspears',
          'Selena Gomez @selenagomez', 'Cristiano Ronaldo @Cristiano', 'Instagram @instagram',
          'Twitter @twitter', 'Jimmy Fallon @jimmyfallon', 'CNN Breaking News @cnnbrk',
          'Ariana Grande @ArianaGrande', 'Shakira @Shakira', 'Demi Lovato @ddlovato',
          'Jennifer Lopez @JLo', 'Drizzy @Drake', 'Oprah Winfrey @Oprah',
          'LeBron James @KingJames', 'Miley Ray Cyrus @MileyCyrus', 'Kevin Hart @KevinHart4real',
          'Bill Gates @BillGates', 'One Direction @onedirection', 'ESPN @espn',
          'SportsCenter @SportsCenter', 'Kim Kardashian West @KimKardashian',
          'Elon Musk @elonmusk'
          ]
USER1 = "Kanye West"
USER2 = "Elon Musk"
USERNAME1 = "kanyewest"
USERNAME2 = "elonmusk"
VERBOSE = False

# Encapsulate the twitter developer keys
# open file TwitterDeveloperKeys.txt
# Format of TwitterDeveloperKeys.txt
'''
CONSUMER_KEY XXXXXXXXXXXXXXXXXXXXXXXXX
CONSUMER_SECRET XXXXXXXXXXXXXXXXXXXXXX
BEARER_TOKEN XXXXXXXXXXXXXXXXXXXXXXXXX
ACCESS_TOKEN_KEY XXXXXXXXXXXXXXXXXXXXX
ACCESS_TOKEN_SECRET XXXXXXXXXXXXXXXXXX
'''

with open("TwitterDeveloperKeys.txt") as f:
    lines = f.readlines()
    words = []
    for line in lines:
        words += line.split()

consumer_key = words[1]
consumer_secret = words[3]
bearer_token = words[5]
access_token = words[7]
access_token_secret = words[9]


def game_input() -> str:
    b = 1
    while b:
        # ask user
        print('1) ', USER1, '\n2) ', USER2, '\n3) Start another game\n4) Quit', sep="")
        row = input()

        # user just enters enter. Makes sure the program does not crash when no input is given
        if row == '':
            print("No input was given. Please try again.")
        # quit command
        elif row.lower() == 'quit' or row.lower() == "q" or int(row) == 4:
            exit(0)
        # input for the choosing who the tweet is from
        elif row == '1' or row == '2' or row == '3':
            return row
        else:
            print("\nInvalid Input. Please try again.")


def verbose_get_tweets() -> tuple:
    print("First Person")
    b = 1
    user1, username1 = "", ""
    user2, username2 = "", ""
    while b:

        temp = input("1) ")
        temp = temp.lower()
        boolean = False
        for name in people:
            if temp in name.lower():
                user1, username1 = name.split('@')
                boolean = check_username(user1)
                if boolean:
                    break
        if not boolean:
            print("Invalid input. Please try again.")
        else:
            b -= 1
    global USER1
    USER1 = user1
    global USERNAME1
    USERNAME1 = username1
    print("Second Person")
    b = 1
    while b:
        temp = input("2) ")
        temp = temp.lower()
        # first, last = temp.split(" ", 1)
        boolean = False
        for name in people:
            if temp in name.lower():
                user2, username2 = name.split('@', 1)
                boolean = check_username(user2)
                if boolean:
                    break
        if not boolean:
            print("Invalid input. Please try again.")
        else:
            b -= 1
    global USER2
    USER2 = user2
    global USERNAME2
    USERNAME2 = username2
    temp1 = get_tweets(USERNAME1)
    temp2 = get_tweets(USERNAME2)

    return temp1, temp2


def check_username(user: str) -> bool:
    print("Did you mean ", user[:len(user) - 1], "?", sep="")
    b = 1
    while b:
        print("1) yes\n2) no")
        pin = input()
        if pin == '':
            print("Nothing was inputted. Enter something this time!")
        elif pin == '1':
            b -= 1
            return True
        elif pin == '2':
            return False
        else:
            print("Invalid input. 1 or 2")


def get_tweets(username: str) -> list:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Access to user's access key and access secret
    auth.set_access_token(access_token, access_token_secret)

    # Calling api
    api = tweepy.API(auth)
    # Authorization to consumer key and consumer secret

    all_tweets = []

    new_tweets = api.user_timeline(screen_name=username, count=200)
    all_tweets.extend(new_tweets)
    oldest = all_tweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    if VERBOSE:
        print("Downloading Tweets for @", username, sep='')
    while len(new_tweets) > 0:
        if VERBOSE:
            print(f"getting tweets before {oldest}")

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=username, count=200, max_id=oldest)
        all_tweets.extend(new_tweets)

        # update the id of the oldest tweet
        oldest = all_tweets[-1].id - 1

        if VERBOSE:
            print(f"...{len(all_tweets)} tweets downloaded so far")

    # transform the tweepy tweets into a 2D array that will populate the csv

    tmp = []
    if VERBOSE:
        print("Total of", len(all_tweets), "Tweets Downloaded!")
    for tweet in all_tweets:
        temp = tweet.text
        if '@' not in temp:
            if '://' not in temp:
                tmp.append(temp)
    return tmp


def play_twitter_game(tweet1: list, tweet2: list) -> None:
    lives = 5
    score = 0
    total = 0
    print("Guess who wrote the quote below!")
    while lives:

        num = randrange(1, 3)
        if num == 1:
            string = tweet1.pop()
        else:
            string = tweet2.pop()
        print("\"", string, "\"", sep="")
        row = game_input()
        if num == int(row):
            total += 1
            score += 1
            print("Correct! You have", lives, "lives remaining. Keep it up!\n")
        elif row == '3':
            mode = choose_mode()
            if mode == 'verbose':
                tweet1, tweet2 = verbose_get_tweets()
            shuffle(tweet1)
            shuffle(tweet2)
            play_twitter_game(tweet1, tweet2)
        else:
            lives -= 1
            total += 1
            print("Incorrect! You have", lives, "lives remaining. Yikes!\n")
    print("\nGame Over! You have scored: ", score, "/", total, " with an accuracy of ", end="", sep="")
    percent = score / total * 100
    print("%.2f" % percent, "%", sep="")


def choose_mode() -> str:
    print("Which mode would you like to play?")
    b = 1
    while b:
        print("1) Play with Kanye West and Elon Musk\n2) Type in two valid Twitter names from the READme\n3) Quit")
        p = input()
        if p == '':
            print("No input was given. Enter something this time!")
        elif p.lower() == "1":
            return "succinct"
        elif p.lower() == '2':
            global VERBOSE
            VERBOSE = True
            return "verbose"
        elif p.lower() == '3' or p.lower() == 'q' or p.lower() == 'quit':
            exit(0)
        else:
            print("Invalid input. Please try again.")


def play_again() -> bool:
    b = 1
    while b:
        print("Would you like to play again?\n1) Yes\n2) No")
        x = input()

        if x == "1":
            return True
        elif x == "2":
            return False
        else:
            print("Invalid input. Please enter 1 or 2")


if __name__ == '__main__':
    playing = True
    # first load the game for kanye west and elon musk
    list_1 = get_tweets("kanyewest")
    list_2 = get_tweets("elonmusk")
    while playing:
        # asks user which game mode they want to play
        if len(playlist) > 0:
            mixer.music.queue(playlist.pop())
        game_mode = choose_mode()
        # this will retrieve the tweets from the people the user inputted from the api
        if game_mode == 'verbose':
            list_11, list_12 = verbose_get_tweets()
            print(len(list_1), "Filtered tweets will be used for", USER1)
            print(len(list_2), "Filtered tweets will be used for", USER2)
        # shuffle the tweets around for randomness
        shuffle(list_1)
        shuffle(list_2)
        play_twitter_game(list_1, list_2)
        # keeps playing if the user wants to keep playing
        playing = play_again()

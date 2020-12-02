import tweepy
from random import shuffle
from random import randrange

people = ['George Takei @GeorgeTakei', 'Jeff Weiner @jeffweiner', 'Alexia Tsotsis @alexia',
          'Dan Primack @danprimack', 'Marissa Mayer@@marissamayer', 'Kim Dotcom @@KimDotcom',
          'Arianna Huffington @ariannahuff', 'PewDiePie @pewdiepie', 'Vani Hari @thefoodbabe',
          'Beyoncé @Beyonce', 'Lorde @lorde', 'The White House @WhiteHouse',
          'Barack Obama @BarackObama', 'Pope Francis @Pontifex', 'J.K. Rowling @jk_rowling',
          'Michelle Obama @MichelleObama', 'Melissa Stewart @MelissaOnline', 'Steve Forbes @SteveForbesCEO',
          'Sir Richard Branson @RichardBranson', 'Steve Case @SteveCase', 'Bill Gates @BillGates',
          'Anne-Marie Slaughter @SlaughterAM', 'Jeff Weiner @jeffweiner', 'Elizabeth Warren @SenWarren',
          'Debora Spar @deboraspar', 'Padmasree Warrior @padmasree', 'Anna Maria Chávez @AnnaMariaChavez',
          'Gloria Steinem @gloriasteinem', 'Aileen Lee @aileenlee', 'Dwayne Johnson @TheRock',
          'Brianna Wu @Spacekatgal', 'Serena William @serenawilliams', 'Katy Perry @katyperry',
          'Justin Bieber @justinbieber', 'Taylor Swift @taylorswift13', 'Youtube @YouTube',
          'Rihanna @rihanna', 'Ellen DeGeneres @TheEllenShow', 'Lady Gaga @ladygaga',
          'Justin Timberlake @jtimberlake', 'Britney Spears @britneyspears',
          'Selena Gomez @selenagomez', 'Cristiano Ronaldo @Cristiano', 'Instagram @instagram',
          'Twitter @twitter', 'Jimmy Fallon @jimmyfallon', 'CNN Breaking News @cnnbrk',
          'Ariana Grande @ArianaGrande', 'Shakira @Shakira', 'Demi Lovato @ddlovato',
          'Jennifer Lopez @JLo', 'Drizzy @Drake', 'Oprah Winfrey @Oprah',
          'LeBron James @KingJames', 'Miley Ray Cyrus @MileyCyrus', 'Kevin Hart @KevinHart4real',
          'Bill Gates @BillGates', 'One Direction @onedirection', 'ESPN @espn',
          'SportsCenter @SportsCenter', 'Kim Kardashian West @KimKardashian', 'Kanye West @kanyewest'
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


def game_input():
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
        elif row.isnumeric() and 1 <= int(row) <= 3:
            b -= 1
        else:
            print("\nInvalid Input. Please try again.")
    return row


def verbose_get_tweets():
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
                user1, username1 = name.split('@', 1)
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


def check_username(user):
    print("Did you mean ", user, "?", sep="")
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


def get_tweets(username):
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


def play_twitter_game(tweet1, tweet2):
    lives = 5
    score = 0
    total = 0
    print("Guess who wrote the quote above!")
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
    print("\nGame Over! You have scored: ", score, "/", total, sep="")


def choose_mode():
    print("Which mode would you like to play?")
    b = 1
    while b:
        print("1) Play with Kanye West and Elon Musk\n2) Type in two valid Twitter names from the READme")
        p = input()
        if p == '':
            print("No input was given. Enter something this time!")
        elif p.lower() == "1":
            return "succinct"
        elif p.lower() == '2':
            global VERBOSE
            VERBOSE = True
            return "verbose"
        else:
            print("Invalid input. Please try again.")


def play_again():
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
    list1 = get_tweets("kanyewest")
    list2 = get_tweets("elonmusk")
    print("Welcome to the Twitter Guessing Game!")
    while playing:
        game_mode = choose_mode()
        if game_mode == 'verbose':
            list1, list2 = verbose_get_tweets()
            print(len(list1),"Filtered tweets will be used for", USER1)
            print(len(list2), "Filtered tweets will be used for", USER2)
        shuffle(list1)
        shuffle(list2)
        play_twitter_game(list1, list2)
        playing = play_again()

# Twitter-Guessing-Gamee
Given a tweet by Kanye West or Elon Musk, prompt the user to guess which public figure made the tweet, let the user know if they were correct. Once the user is finished let the user know how accurate they were in their guesses.


    Enter your twitter developer keys in TwitterDeveloperKeys.txt in order to run 'main.py. 
    There is also an executable file called 'main' that you can run without if you do not have access to twitter api keys.

    This is the game logic of the game:
    
    1) When user starts program, load the first 3200 tweets by Elon and Kanye, filtered to not include any links or tags to other twitter users
    2) Randomly choose a tweet by Elon or Kanye to give to the user
    3) Prompt the user to guess
    4) Let the user know if they were correct
    5) Repeat steps 1-4
    6) Show the user their game statistics

There are two game modes you can play:

    1) Kanye West vs Elon Musk
    2) Any two twitter users from the list of people below
        
List of people users can play the game with:

    1) George Takei: @GeorgeTakei
    2) Jeff Weiner: @jeffweiner
    3) Alexia Tsotsis: @alexia
    4) Dan Primack: @danprimack
    5) Marissa Mayer: @marissamayer
    6) Kim Dotcom: @KimDotcom
    7) Arianna Huffington: @ariannahuff
    8) PewDiePie: @pewdiepie
    9) Vani Hari: @thefoodbabe
    10) Beyoncé: @Beyonce
    11) The White House: @WhiteHouse
    12) Barack Obama: @BarackObama
    13) Pope Francis: @Pontifex
    14) J.K. Rowling: @jk_rowling
    15) Lorde: @lorde
    17) Michelle Obama: @MichelleObama
    18) Melissa Stewart: @MelissaOnline
    19) Steve Forbes: @SteveForbesCEO
    20) Sir Richard Branson: @RichardBranson
    21) Steve Case: @SteveCase
    22) Bill Gates: @BillGates
    23) Anne-Marie Slaughter: @SlaughterAM
    24) Elizabeth Warren: @SenWarren
    25) Debora Spar: @deboraspar
    26) Padmasree Warrior: @padmasree
    27) Anna Maria Chávez: @AnnaMariaChavez
    28) Gloria Steinem: @gloriasteinem
    29) Aileen Lee: @aileenlee
    30) Dwayne Johnson: @TheRock
    31) Kanye West @kanyewest
    32) Serena William: @serenawilliams
    33. Katy Perry: @katyperry
    34. Justin Bieber: @justinbieber
    35. Taylor Swift: @taylorswift13
    36. Youtube: @YouTube
    37. Rihanna: @rihanna
    38. Ellen DeGeneres: @TheEllenShow
    39. Lady Gaga: @ladygaga
    40. Justin Timberlake: @jtimberlake
    41. Twitter: @twitter
    42. Britney Spears: @britneyspears
    43. Kim Kardashian West: @KimKardashian
    44. Selena Gomez: @selenagomez
    45. Cristiano Ronaldo: @Cristiano
    46. Instagram: @instagram
    47. Jimmy Fallon: @jimmyfallon
    48. CNN Breaking News: @cnnbrk
    49. Ariana Grande: @ArianaGrande
    50. Shakira: @Shakira
    51. Demi Lovato: @ddlovato
    52. Jennifer Lopez: @JLo
    53. Drizzy: @Drake
    54. Oprah Winfrey: @Oprah
    55. LeBron James: @KingJames
    56. Miley Ray Cyrus: @MileyCyrus
    57. Kevin Hart: @KevinHart4real
    58. Bill Gates: @BillGates
    59. One Direction: @onedirection
    60. ESPN: @espn
    61. SportsCenter: @SportsCenter
    
Tweets were scraped using the Tweepy package

Adapted from https://github.com/ChangePlusPlusVandy/change-coding-challenge-Davi-web

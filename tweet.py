'''Assignment 1.
Author: Ossama Benaini
'''

import math

MAX_TWEET_LENGTH = 50

HASHTAG_SYMBOL = '#'

MENTION_SYMBOL = '@'

UNDERSCORE = '_'

SPACE = ' '


def is_valid_tweet(text: str) -> bool:
    '''Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).

    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False
    '''


def compare_tweet_lengths(text1: str, text2: str) -> int:
    """Return 1 if text1 longer than text2, -1 if text1 is smaller than text2
    or 0 if both texts are the same length.

    >>>compare_tweet_lengths("hello", "this is a program")
    >>>-1
    >>>compare_tweet_lengths("I hope I do well", "I'm broke")
    >>>1
    >>>compare_tweet_lengths("Ossamaaa", "Benainio")
    >>>0
    """


def add_hashtag(valid_tweet: str, tweet_word: str) -> str:
    """Return a valid_tweet with a hashtag at the end of it

    >>>add_hashtag("I like", "games")
    >>>I like #games
    >>>add_hashtag("raptors are", "champions")
    >>>raptors are #champions
    >>>add_hashtag("raports are champions however i doubt they will make the playoffs this year because kawhi left and at this point im just rambling to get to over 50 words to pass the limit because i want to have an example of what happens when you try to use a variable thats too long so i think im going to end it now", "cool")
    >>>raports are champions however i doubt they will make the playoffs this year because kawhi left and at this point im just rambling to get to over 50 words to pass the limit because i want to have an example of what happens when you try to use a variable thats too long so i think im going to end it now
    """


def contains_hashtag(valid_tweet: str, tweet_word: str) -> bool:
    """Return True if and only if valid_tweet contains a hashtag made up
       from the HASHTAG_SYMBOL and tweet_word, False otherwise.

       >>>contains_hashtag("i never #loved you", "loved")
       >>>True
       >>>contains_hashtag("i never #loved you", "you")
       >>>False
       >>>contains_hashtag("i never#loved you", "loved")
       >>>False
       """


def is_mentioned(valid_tweet: str, tweet_word: str) -> bool:
    """Return True if and only if valid_tweet contains a mention made up from
       the MENTION_SYMBOL and tweet_word, False otherwise.

       >>>is_mentioned("i never loved @you", "you")
       >>>True
       >>>is_mentioned("i never loved @you", "loved")
       >>>False
       >>>is_mentioned("i never loved@you", "you")
       >>>True
       """



def add_mention_exclusive(valid_tweet: str, tweet_word: str) -> str:
    """Return potential tweet with a mention at the end. Return valid_tweet
       if valid_tweet is already in the tweet or if the tweet is not valid.

       >>>add_mention_exclusive("I like sports too", "Ossama")
       >>>"I like sports too @Ossama
       >>>add_mention_exclusive("I like sports too, Ossama", "Ossama")
       >>>"I like sports too, Ossama"
       >>>add_mention_exclusive("I need some pizza", "Dominos")
       >>>"I need some pizza @Dominos"
    """


def num_tweets_required(message: str) -> int:
    """Return the minimum nuumber of tweets required to communicate the
       entire message

       >>>num_tweets_required("Hi my name is Ossama and im trying very hard to get rich")
       >>>2
       >>>num_tweets_required("Hi my name is Ossama and im trying very hard to get rich because i love money but i dont want to work so idk what to do")
       >>>3
       >>>num_tweets_required("ok")
       >>>1
    """


def get_nth_tweet(message: str, n: int) -> str:
    """Return the last valid tweet in a sequence of tweets. If the length
       of message is smaller than n return empty string.

       >>>get_nth_tweet("num_tweets_required("Hi my name is Ossama and im trying very hard to get rich because i love money but i dont want to work so idk what to do", 3)
       >>>"k so idk what to do"
       >>>get_nth_tweet("ive been working on this project for a while now i hope i do well", 2)
       >>>" hope i do well"
       >>>get_nth_tweet("These examples are startng to get tiring.", 7)
       >>>""
    """


def clean(text: str) -> str:
    '''Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    '''


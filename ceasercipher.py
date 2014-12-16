import string
import random
import numbers

WORDLIST_FILENAME = "words.txt"
def load_words():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist
    
wordlist=load_words()

def is_word(wordlist,word):
    word=word.lower()
    word=word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    return random.choice(wordlist)

def random_string(wordlist,n):
        return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_story_string():
    """
    Returns a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

    
def build_coder(shift):
    assert shift>=0 and shift<27, 'shift %s is not between 0 and 27'%shift
    assert isinstance(shift,numbers.Integral),'shift is not n integer'
    coder={}
    lowercase_and_space = string.ascii_lowercase + ' '
    uppercase_and_space = string.ascii_uppercase + ' '
    shifted_lowercase_and_space = lowercase_and_space[shift:] + lowercase_and_space[:shift]
    shifted_uppercase_and_space = uppercase_and_space[shift:] + uppercase_and_space[:shift]
    for i in range(uppercasse_and_space):
        coder[uppercase_and_space[i]]=shifted_uppercase_and_space
    for i in range(lowercase_and_space):
        coder[lowercase_and_space[i]]=shifted_lowercase_and_space
    return coder

def apply_coder(text,coder)
encoded_text=''
for i in text:
    if i in coder:
        encoded_text=encoded_text+coder[i]
    else:
        encoded_text+=i
    return encoded_text
    
def apply_shift(text,shift):
    assert shift<=0 and shift <27
    return apply_coder(text,build_coder(shift))


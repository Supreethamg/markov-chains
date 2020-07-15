"""Generate Markov text from text files."""

import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_data = open(file_path).read()
   
    return file_data


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    text = text_string.split()

    for i in range(0,len(text) - 2):
       key_tuple=(text[i],text[i+1])
       
       if key_tuple in chains:
            chains[key_tuple].append(text[i+2])
       else:
            
            chains[key_tuple]=[text[i+2]]
        
           

    for key,value in chains.items():
        print(key, ':' , value)
   
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    # creating a random key
    list_keys = list(chains.keys())
    key = random.choice(list_keys)
    # Creating a random value
    value = random.choice(chains[key])
    #creating first link with key and value
    link = f'{key[0]} {key[1]} {value}'
    words.append(link)

    while key in chains:
        #Creating a new key
        new_key = link.split(" ")[-2:]
        new_key_tuple = tuple(new_key)

         #if new key is chains then create new value
        if new_key_tuple in chains.keys():
            new_value = random.choice(chains[new_key_tuple])
            words.append(new_value)
            key = new_key_tuple
            link = f'{new_key[0]} {new_key[1]} {new_value}'
        else:
            break


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

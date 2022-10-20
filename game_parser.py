import string

allow_words = ["damage", "help", "go", "north", "south", "west", "east", "take", "drop", "map", "keycard", "look"]

def filter_words(words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed.
    """
    return [word for word in words if word in allow_words]
   
   
def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation.
    """
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct


def normalise_input(user_input):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned.
    """
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    # Split string into a list of words (words are separated by spaces)
    words = no_punct.split()
    # Remove "unimportant" words
    important_words = filter_words(words)
    return important_words
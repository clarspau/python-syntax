def print_upper_words(words):
    """Print out each word on a separate line, but in all uppercase.
    """

    # input: print_upper_words(["hi", "hello", "goodbye"])
    # output: HI
    # output: HELLO
    # output: GOODBYE

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """Print out each word that starts with the letter "e" (either upper or lowercase) on a separate line, but in all uppercase.
    """

    # input: print_upper_words2(["egg", "omelette", "Eggplant", "Bagel"])
    # output: EGG
    # output: EGGPLANT

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words(words, must_start_with):
    """Print out each word that starts with the given letter/s on a separate line, but in all uppercase.
    """

    # input: print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
    # output: "HELLO", "HEY", "YO", and "YES"

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

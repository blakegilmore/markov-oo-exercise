import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, call make_chains to make a dictionary from them."""
        text=""
        for filename in filenames:
            fileobject = open(filename)
            text+=fileobject.read()
        print text
        return text


    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""
        chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

        # or we could say "chains.setdefault(key, []).append(value)"

        return chains


    def make_text(self,chains):
        """Takes dictionary of markov chains; returns random text."""
        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

        return " ".join(words)


if __name__ == "__main__":
    # we should get list of filenames from sys.argv
#     
    newmarkov = SimpleMarkovGenerator()
    textystuff = newmarkov.read_files(["green-eggs.txt"])
    newdictionary = newmarkov.make_chains(textystuff)
    all_our_text = newmarkov.make_text(newdictionary)

    print all_our_text
#     # we should call the make_text method 5x

#     pass


# # import sys
# # from random import choice




# def make_chains(corpus):
#     """Takes input text as string; returns dictionary of markov chains."""

#     chains = {}

#     words = corpus.split()

#     for i in range(len(words) - 2):
#         key = (words[i], words[i + 1])
#         value = words[i + 2]

#         if key not in chains:
#             chains[key] = []

#         chains[key].append(value)

#         # or we could say "chains.setdefault(key, []).append(value)"

#     return chains


# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     key = choice(chains.keys())
#     words = [key[0], key[1]]
#     while key in chains:
#         # Keep looping until we have a key that isn't in the chains
#         # (which would mean it was the end of our original text)
#         #
#         # Note that for long texts (like a full book), this might mean
#         # it would run for a very long time.

#         word = choice(chains[key])
#         words.append(word)
#         key = (key[1], word)

#     return " ".join(words)


# input_path = sys.argv[1]
# input_text = open(input_path).read()

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text

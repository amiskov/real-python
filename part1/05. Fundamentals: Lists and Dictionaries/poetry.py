from random import choice

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

"""
{A/An} {adjective1} {noun1}

{A/An} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {preposition2} a {adjective3} {noun3}
"""

poem_string = """
{0} {1} {2}

{0} {1} {2} {3} {4} the {5} {6}
{7}, the {2} {8}
the {6} {9} {10} a {11} {12}
"""


def make_poem():
    poem_nouns = choose_words(nouns, 3)
    poem_verbs = choose_words(verbs, 3)
    poem_adjectives = choose_words(adjectives, 3)
    poem_prepositions = choose_words(prepositions, 2)
    poem_adverbs = choose_words(adverbs, 1)
    poem_article = choose_article(poem_adjectives[0])

    poem = "{} {} {}\n\n".format(
            poem_article, poem_adjectives[0], poem_nouns[0]
    )
    poem += "{} {} {} {} {} the {} {}\n".format(
            poem_article, poem_adjectives[0], poem_nouns[0], poem_verbs[0],
            poem_prepositions[0], poem_adjectives[1], poem_nouns[1]
    )
    poem += "{}, the {} {}\n".format(
            poem_adverbs[0], poem_nouns[0], poem_verbs[1]
    )
    poem += "the {} {} {} a {} {}".format(
            poem_nouns[1], poem_verbs[2], poem_prepositions[1], poem_adjectives[2], poem_nouns[2]
    )

    return poem


def choose_words(words_list, words_count):
    local_list = words_list[:]
    poem_list = []

    for i in range(0, words_count):
        random_word = choice(local_list)
        local_list.remove(random_word)
        poem_list.append(random_word)

    return poem_list


def choose_article(word):
    if word[0] in ('a', 'e', 'i', 'o', 'u'):
        article = 'An'
    else:
        article = 'A'

    return article


print(make_poem())

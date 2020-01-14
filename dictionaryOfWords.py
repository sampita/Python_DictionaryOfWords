"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["existential"] = "concerned with the nature of human existence as determined by the individual's freely made choices"

word_definitions["alien"] = "a creature from outer space; a person who has been estranged or excluded"

word_definitions["extraterrestrial"] = "outside, or originating outside, the limits of the earth"

word_definitions["supernova"] = "the explosion of a star, possibly caused by gravitational collapse, during which the star's luminosity increases by as much as 20 magnitudes and most of the star's mass is blown away at very high velocity, sometimes leaving behind an extremely dense core."

word_definitions["space shuttle"] = "any of several U.S. space vehicles consisting of a reusable manned orbiter that touches down on a landing strip after an orbital mission, two reusable solid rocket boosters that drop off after initial ascent, and an expendable external tank containing liquid propellants."


"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["alien"])
print(word_definitions["space shuttle"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for (word, definition) in word_definitions.items():
    print(f'The definition of {word} is "{definition}"')
    
# Regular Expressions
log = "July 31 7:51:48 mycomputer bad_process[12345]: ERROR Perfroming package upgrade"
index = log.index('[')

# Brittle way to extracing numbers by using index function
print(log[index+1:index+6])

# re module allows for search function to find regular expressions inside strings
import re
log = "July 31 7:51:48 mycomputer bad_process[12345]: ERROR Perfroming package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# =========================================================================================

# Basic Regular Expressions
# Simple Matching in Python
# The "r" at the beginning of the pattern indicates that this is a rawstring
# Always use rawstrings for regular expressions in Python
result = re.search(r'aza', 'plaza')
print(result)

result = re.search(r'aza', 'bazaar')
print(result)

# None is a special value that Python uses that show that there's none actual value there
result = re.search(r'aza', 'maze')
print(result)


# The match attribute always has a value of the actual sub string that match the search pattern
# The span attribute indicates the range where the sub string can be found in the string
print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "sponge"))

# Additional options to the search function can be added as a third parameter
# The re.IGNORECASE option returns a match that is case insensitive
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

# -----------------------------------------------------------------------------------------

# Wildcards and Character Classes
# Character classes are written inside square brackets
# It list the characters to match inside of the brackets
# A range of characters can be defined using a dash
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

# Use a ^, circumflex, inside the square brackets to match any characters that aren't in a group
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# Use a |, pipe symbol to match either one expression or another
# The search function returns the first matching string only when there are multiple matches
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))

# Use the findall function provided by the re module to get all possible matches
print(re.findall(r"cat|dog", "I like both cats and dogs."))

# -----------------------------------------------------------------------------------------

# Repetition Qualifiers
# Repeated matches is a common expressions that include a . followed by a *
# It matches any character repeated as many times as possible including zero - greedy behavior
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py.*n", "Pyn"))

# Use a +, plus character, to match one or more occurrences of the character that comes before it
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

# Use a ?, question mark symbol, for either zero or one occurrence of the character before it
# It is used to specified optional characters
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

# -----------------------------------------------------------------------------------------

# Escaping Characters
# A pattern that includes a \ could be escaping a special regex character or a special string character
# Use a \, escape character, to match one of the special characters
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

# Use \w to match any alphanumeric character including letters, numbers, and underscores
# Use \d to match digits
# Use \s for matching whitespace characters like space, tab or new line
# Use \b for word boundaries
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))
import random 

verbs=['leverage','sync','target','gamify','offline','crowd-sourced']

adjectives=['A/B tested','freemium','hyperlocal','siloed','oriented']

nouns=['early adopter','low hanging fruit','piperline','splash page']

verb=random.choice(verbs)
adjective=random.choice(adjectives)
noun=random.choice(nouns)

phrase=verb+''+adjective+''+noun

print(phrase)

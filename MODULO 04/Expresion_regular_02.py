import re

entrada = r"Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"

match01 = r"User_mentions:2"
match02 = r"likes: 9"
match03 = r"number of retweets: 7"

print("La cantidad de menciones del usuario son: ")
print(re.findall(match01,entrada))
print("La cantidad de likes del post son: ")
print(re.findall(match02,entrada))
print("La cantidad de retweets es: ")
print(re.findall(match03,entrada))
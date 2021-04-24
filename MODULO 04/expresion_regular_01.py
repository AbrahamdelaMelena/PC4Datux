import re
match = r"@robot4&"

cadena = "@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"

print(re.search(match,cadena))
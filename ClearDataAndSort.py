badList = ['a','f','e','q','t','o','t','e','q','a','p']

goodList = list(dict.fromkeys(badList))
print(goodList)
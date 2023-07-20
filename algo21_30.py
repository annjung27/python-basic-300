#21
letters = "python"
print(letters[0], letters[2])

#22
license_plate = "24A 2210"
print(license_plate[:])

#23
string = "ABABAB"
print(string[::2])

#24
string = "PYTHON"
print(string[::-1])

#25
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

#26
print(phone_number.replace("-", ""))

#27
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split)
print(url_split[-1])

# #28
# lang = "python"
# lang[0] = 'p'
# print(lang)

#29
string = 'abcdfe2a354a32a'
print(string.replace("a", "A"))

#30
string = 'abcd'
string2= string.replace('b', 'B')
string = string2
print(string)
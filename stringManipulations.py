message = 'It was a warm and sunny day in August, and the clocks were striking thirteen'


count= {}

for character in message.upper():
    count.setdefault(character,0)
    count[character] = count[character]+1

print(count)


#jtext = pprint.pformat(count)

#dictionaries are unordered, mutable

#pprint = pretty print
#pformat returns a string

#list of dictionaries
dansCats = []
dansCats.append({'name': 'Rufus', 'color':'black and white'})
dansCats.append({'name': 'Freddy', 'color':'orange and white'})
dansCats.append({'name': 'PT', 'color':'gray and white'})

message = 'It was a warm and sunny day in August, and the clocks were striking thirteen'


count= {}

for character in message.upper():
    count.setdefault(character,0)
    count[character] = count[character]+1

print(count)

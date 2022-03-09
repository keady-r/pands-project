sentance = input('Enter sentance: ')
offset = 5
alphabet = ('abcdefghijklmnopqrstuvwxyz')
cipher = ''

for c in sentance:
    if c in alphabet:
        cipher += alphabet[(alphabet.index(c) + offset) % (len(alphabet))]
    else:
        cipher += c

print('Your encrypted message is: ' + cipher)
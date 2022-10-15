import os

user_input = input('Dir: ')
directory = os.listdir(user_input)

searchstring = bytes(input('Bytes: '), 'utf-8').lower()

for fname in directory:
    if os.path.isfile(user_input + os.sep + fname):
        f = open(user_input + os.sep + fname, 'rb')

        if searchstring in f.read().lower():
            print('found string in file %s' % fname)
        f.close()
import functools

# longest name in the file
with open('names.txt') as f:
    print(functools.reduce(lambda x, y: x if len(x) > len(y) else y, map(str.strip, f)))

# sum of lens
with open('names.txt') as f:
    print(sum(map(lambda x: len(x.strip()), f)))

# shortest names
with open('names.txt') as f:
    names = [line.strip() for line in f]
    shortest_length = min(map(len, names))
    print('\n'.join(name for name in names if len(name) == shortest_length))

# lengths of all names
with open('names.txt') as f:
    with open('names_length.txt', 'w') as g:
        g.write('\n'.join(str(len(line.strip())) for line in f))

#saif5
name_len = int(input("Enter name length: "))
with open('names.txt') as f:
    print(''.join(filter(lambda x: len(x.strip()) == name_len, f)))



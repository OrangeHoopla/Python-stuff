from random import randint

def twistUp(s):
    new_s = ''
    for x in s:
        new_s += x
        if x.isalpha():
            new_s += chr(0x0300 + randint(0, 0x6F))
    return new_s

end = (list(twistUp('Hello, world!')))
red = ''.join(end)
print (red)
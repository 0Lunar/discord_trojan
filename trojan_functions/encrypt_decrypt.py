import random

def encrypt_file(filename):
    try:
        key = random.randint(1,20)
        x = 0
        l = 0
        astring2 = 0
        string = ""
        filename2 = open(filename, "r").read()
        while(l != 20):
            try:
                while(x != len(filename2)):
                    astring2 = ord(filename2[x])
                    if(x % 2 == 0):
                        astring2 += key
                    else:
                        astring2 -= key
                    string += chr(astring2)
                    x += 1
                filename2 = open(filename, "w").write(string)
            except:
                pass
            l += 1
        return key
    except:
        return 1

def decrypt_file(filename, key):
    try:
        x = 0
        astring2 = 0
        string = ""
        filename2 = open(filename, "r").read()
        while(x != len(filename2)):
            astring2 = ord(filename2[x])
            if(x % 2 == 0):
                astring2 -= int(key)
            else:
                astring2 += int(key)
            string += chr(astring2)
            x += 1
        filename2 = open(filename, "w").write(string)
        return 0
    except:
        return 1
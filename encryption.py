def xor_strings(s,t):
    """xor two strings together"""
    return "".join(str(ord(a)^ord(b))+' ' for a,b in zip(s,t))

key = ''

fout = open('encrypted_message.txt','w')
with open('message.txt','r') as fin:
    words = [line.strip('\n').lower() for line in fin.readlines()]
    for word in words:
        cipherWord = xor_strings(word, key)
        fout.write(cipherWord)
        fout.write('\n')
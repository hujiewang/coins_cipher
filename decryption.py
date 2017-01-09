def xor_strings(s,t):
    """xor two strings together"""
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(s,t))

key = ''

with open('encrypted_message.txt','r') as fin:
    words = [line.strip('\n').split() for line in fin.readlines()]
    for i in range(len(words)):
        word = ''.join([chr(int(num)) for num in words[i]])
        decrypted_word = xor_strings(word, key)
        print(str(i+1)+' '+decrypted_word)
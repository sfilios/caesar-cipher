##Caesar cipher program

secret_message=raw_input("user input secret message here - no spaces ")
shift=int(raw_input("how far would you like to shift each letter? "))

##create a dictionary with each letter and the number value associated with them
alphabet={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

number_code={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

##remove the spaces
for letter in secret_message:
	if letter==' ':
		secret_message=

def scrambler(secret_message):
    new_message=[]

    for letter in secret_message:
        new_letter=alphabet[letter]+shift
        print new_letter
        new_message.append(new_letter)
		
    print secret_message

    for scramble in new_message:
        print number_code[scramble],



def decoder(scrambled):
    decoded=[]
    cipher_input=scrambled
    print ''
    print cipher_input

    for letter in cipher_input:
        new_letter=alphabet[letter]-shift
        decoded.append(new_letter)
        print number_code[new_letter],
    
print scrambler(secret_message)
scrambled_input=raw_input("enter scrambled message here - no spaces ")
print decoder(scrambled_input)

from gfxhat import lcd

# This function takes hex strings and returns binary strings. I tried using bin() but found it difficult to change strings.
# Converting with int() didn't help when the Hex values were A-F.
def binConv(x):
    if x == '0':
        x = '0000'
    if x == '1':
        x = '0001'
    if x == '2':
        x = '0010'
    if x == '3':
        x = '0011'
    if x == '4':
        x = '0100'
    if x == '5':
        x = '0101'
    if x == '6':
        x = '0110'
    if x == '7':
        x = '0111'
    if x == '8':
        x = '1000'
    if x == '9':
        x = '1001'
    if x == 'A':
        x = '1010'
    if x == 'B':
        x = '1011'
    if x == 'C':
        x = '1100'
    if x == 'D':
        x = '1101'
    if x == 'E':
        x = '1110'
    if x == 'F':
        x = '1111'
    return x

# The next section essentially changes the given: 0x0808080800080000,! to a dictionary key-value pair where the key is the 
# symbol, and the value is a list of 8 items with 8 binary digits each. 

# First I create a function which will create a new empty Dictionary and a new empty List, and open the font3.txt file
# (twice, as I access it two different times).
def dictMaker():
    myDict = dict()
    fin = open('font3.txt')
    fin2 = open('font3.txt')
    listOfLists = []

    # Next I run through each line of the given file and add the hex digits to my list, cutting out the beginning '0x' 
    # and trailing ',!'.
    for line in fin:
        hexDigits = list(line[2:18]) 
        listOfLists.append(hexDigits)

    # Next I run through each number in every list, converting it to binary.
    i=0
    while i < len(listOfLists):
        j=0
        while j < len(listOfLists[i]):
            myVar = listOfLists[i][j]
            myVar = binConv(myVar)
            listOfLists[i][j] = myVar 
            j += 1
        i += 1

    # Next I join the numbers up in pairs, so index 0 is put together with index 1, index 2 is put together with index 3,
    # and so on. This creates a master list, with sublists inside them. These 8 digit x 8 digit sublists are what will 
    # be used to change the pixels on the GFXHAT.
    i = 0
    while i < len(listOfLists):

        k = 0
        j = 0
        while k <= 15:
            listOfLists[i][j] = [''.join(listOfLists[i][k:k+2])]
            k+=2
            j+=1
        del listOfLists[i][8:]
        i += 1

    # Next I begin adding to my Dictionary. The symbol on each line is the key, and the binary 8x8 digit list is the value.
    i=0
    for line in fin2:
        myDict[line[19]]=listOfLists[i]
        i+=1
    
    return myDict


# The value is then run through, and this function checks if the digits are 0 or 1. If they are 0, the pixel is not lit. If 
# it is 1, the pixel is lit. The function finishes the line, goes back to its original location (but increasing y by 1, 
# essentially moving south on the screen), and begins running through the second line. If one wishes, they could add a 
# parameter for x and y, and have the user specify which coordinates they would like to have the letter appear at.

def displayCharacter(t):
    x = 30
    y = 30
    i = 0
    while i < 8:
        g = 0
        while g < 8:
            if t[i][0][g] == '1':
                lcd.set_pixel(x,y,1)
                lcd.show()
                x+=1
                g+=1
            else:
                x+=1
                g+=1
        i+=1
        y+=1
        x=30

# This function calls all the above code.
myDict = dictMaker()

# Now, the user types the letter or symbol they wish to be displayed, and the dictionary key-value pair associated with
# it is generated. If the user types a character not in the dictionary, the while loop keeps prompting them for a new choice.
def userInput(): 
    active = True
    while active == True:
        c = input('type the letter you want to type')
        if c in list(myDict.keys()):  
            t = (myDict[c])
            return t
        else:
            print("Cannot print character. Please try a new character.")

# The function is called with the desired key-value pair selected.
t = userInput() 
displayCharacter(t)
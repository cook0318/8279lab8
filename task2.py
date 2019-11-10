def csvReader(filename):
    try:
        fin = open(filename)
        for line in fin:
            myList = (list(line))
            if ',' in myList:
                myList.remove(',')
            myString = ''.join(myList)
            print(myString.split())
    except:
        print("Error: Cannot find file")

file = input("Enter the CSV file name you'd like to read.")

csvReader(file)
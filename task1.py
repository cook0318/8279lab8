def csvConverter(file1,file2, outputfile):
    # opens the two files that user has specified
    finX = open(file1)
    finY = open(file2)
    # creates output file using user given name, and inserts first line
    fout=open(outputfile, 'w')
    fout.write('{}\n'.format("First Name, Count"))
    # loops through all lines in first file, writing into output
    for line in finX:
        name = line.split()
        fout.write("{}\n".format(name[0] + ", " + name[1]))
    # loops through all lines in second file, writing into output
    for line in finY:
        name = line.split()
        fout.write("{}\n".format(name[0] + ", " + name[1]))
    fout.close()

# user input prompts
file1 = input("Please enter first file")
file2 = input("Please enter second file")
outputfile = input("Please enter the output file name (ending with .csv)")

# main function call
csvConverter(file1,file2,outputfile)
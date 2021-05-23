try:
    #open measles file
    measles = open('measles.txt', 'r')
    inp = input('Enter year: ')
    if len(inp) <= 4:
        pass
    else:
        print('Invalid inp length!!!')
        inp = input('Enter year: ')
    file = input('Enter file name to save text: ')
    #File must have .txt extesion
    if '.txt' in file:
        pass
    else:
        print('File to file must be in txt format, such as ex.txt')
        exit()
    save = open(file,'w')
    for line in measles:
        if (inp ==" " or inp =="all" or inp =="ALL"):
            save.write(line)
        elif line[88:92].startswith(inp):#must start with any of the input
            save.write(line)
    save.close
    measles.close
except:
    print("Error!!,File cannot be opened.")
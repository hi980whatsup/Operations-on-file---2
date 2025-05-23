with open("simple_home.txt","r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)


file.close()        

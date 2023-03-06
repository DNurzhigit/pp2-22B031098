import os 
list = ["There" , "was" , "Polish" , "Cow", "lyrics"]
with open(r"C:\Users\nurzh\OneDrive\Документы\GitHub\pp2-22B031098\tsis6\dir-and-files\polish-cow.txt" , "w+") as myFile:
    for word in list:
        myFile.write(word + "\n")
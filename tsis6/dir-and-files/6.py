import os 
EngAlphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
ListOfAlphabet = list(map(str , EngAlphabet.split(" "))) 
for char in ListOfAlphabet:    
    with open( "C:\Users\nurzh\OneDrive\Документы\GitHub\pp2-22B031098\tsis6\dir-and-files\smth" + char +".txt", "w") as file:
        file.write("JZ is Power")
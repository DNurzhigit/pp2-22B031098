import os
with open(r"C:\Users\nurzh\OneDrive\Документы\GitHub\pp2-22B031098\tsis6\dir-and-files\polish-cow.txt" , 'r') as file:
    data = file.read() 
with open(r"copy.txt" , 'w') as f:
    f.write(data)
import os 
superDirectory = 'C:\Users\nurzh\OneDrive\Документы\GitHub\pp2-22B031098\tsis6\dir-and-files'
print(*[directory for directory in os.listdir(superDirectory)] , sep = "\n")

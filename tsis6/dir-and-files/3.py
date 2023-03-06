import os 
somePath = r"C:\Users\nurzh\OneDrive\Документы\GitHub\pp2-22B031098\tsis6\dir-and-files\polish-cow.txt"
if os.path.exists(somePath):
    print("Path to something exist , let's find the filename and dirname" )
    print( "Name of the file: " + os.path.basename(somePath))
    print( "Name of the directory: " + os.path.dirname(somePath))
else:
    print("Path doesn't exist") 
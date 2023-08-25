Lst = ["Banana", "Orange","Burger","speed"]
def lstToFile(lst, fileName):
    with open (str(fileName), "w") as f:
        for i in lst:
            f.write(i)
            f.write("\n")

lstToFile(Lst, "ex.txt")     
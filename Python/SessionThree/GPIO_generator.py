x1 = input("please enter bit 0 mode\n")
if x1 != "0" and x1 != "1":
    x1 = "0"
x2 = input("please enter bit 1 mode\n")
if x2 != "0" and x2 != "1":
    x2 = "0"
x3 = input("please enter bit 2 mode\n")
if x3 != "0" and x3 != "1":
    x3 = 0
x4 = input("please enter bit 3 mode\n")
if x4 != "0" and x4 != "1":
    x4 = 0
x5 = input("please enter bit 4 mode\n")
if x5 != "0" and x5 != "1":
    x5 = 0
x6 = input("please enter bit 5 mode\n")
if x6 != "0" and x6 != "1":
    x6 = 0
x7 = input("please enter bit 6 mode\n")
if x7 != "0" and x7 != "1":
    x7 = 0
x8 = input("please enter bit 7 mode\n")
if x8 != "0" and x8 != "1":
    x8 = 0

code = '''void Init_Port_Dir(void)\n{\n\tDDRA=0b'''+ str(x1)+str(x2)+str(x3)+str(x4)+ str(x5)+str(x6)+str(x7)+str(x8)+ ";\n} \n"

with open("GPIO_INIT.c", "w") as f:
    f.write(str(code))
def countFour(num):
    count =  0
    for i in num:
        if i == 4:
            count +=1
    return count


print(countFour([4,3,4,5,6,7,4]))
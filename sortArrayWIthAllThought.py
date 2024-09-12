print("length of array:", len(y))
print("array:'" + str(x) + "'")
fruits = ["blackberry", "watermelon", "Mango","Muskmelon", "wolfberry", "pear", "banana", "blueberry","apple", "strawberry", "raspberry"]
print("find berries from fruits")
for a in fruits:
    if "berry" in a:
        print(a)
print("sort fruits array")
#1 step
#c = a # c <- a
#2 step
#a = b # a <- b
#3 step
#b = c # b <- c

#1 step
#c = fruits[a] # c <- a
#2 step
#fruits[a] = fruits[b] # a <- b
#3 step
#fruits[b] = c # b <- c


#a = "blackberry"
#b = "apple"
#strlength = len(a)
#if len(b) < strlength:
#    strlength = len(b)

    

fruits = ["blackberry", "watermelon", "mango","Muskmelon", "wolfberry", "pear", "banana", "blueberry","apple", "strawberry", "raspBerry"]
#1st loop 
for a in range(len(fruits)):
    #for b in 
    print("index a:", a)
    print("index element in fruits:", fruits[a])
    #2nd loop
    for b in range(a + 1, len(fruits)):
        print("index b:", b)
        print("index element in fruits:", fruits[b])
        strlength = len(fruits[a])
        if len(fruits[b]) < strlength:
            strlength = len(fruits[b])
        f = False
        #3rd loop for compare 2 strings letter by letter
        for s in range(strlength):
            s1 = ord(fruits[a][s])
            if s1 < 97:
                s1 = s1 + 32 #in case this letter is upper case
            # s2
            #get the charactor's ascii number with ord
            if s1 > ord(fruits[b][s]):
                    #1
                    c = fruits[a]
                    #2
                    fruits[a] = fruits[b]
                    #3
                    fruits[b] = c                    
                    f = True
                    break
            elif ord(fruits[a][s]) < ord(fruits[b][s]):
                break
        if f:
            print("switched")
for a in fruits:
    print(a)

automobile=["Toyota"
,"Honda"
,"Ford"
,"Chevrolet"
,"Nissan"
,"BMW"
,"Mercedes-Benz"
,"Audi"
,"Tesla"
,"Hyundai"
,"Kia"
,"Volkswagen"
,"Porsche"
,"Ferrari"
,"Lamborghini"
,"McLaren"
,"Aston Martin"
,"Jeep"
,"Dodge"
,"Cadillac"]
targetOrderAbc=["Aston Martin","Audi"]
targetOrderLen=["BMW","Kia"]#try to finish this ...
#for a in automobile:
    #print(a)

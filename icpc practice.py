##Reverse Mode1
##a=int(input())
##b=[int(i) for i in input().split()]
##c=b[1] - b[0]
##s=b[0]
##for i in range(a):
##    s+=c
##print(s)


##vinyl records
##from math import pi
##a = int(input())
##b = [int(i) for i in input().split()]
##l = []
##tot = 0
##for i in b:
##    area = pi*(i**2)
##    l.append(area)
##l.sort(reverse = True)
##print(l)
##for i in range(len(l)-1):
##    if i % 2 == 0:
##        sub = l[i] - l[i+1]
##        tot+=sub
##tot = round(tot,6)
##print(tot)

##The Walking Adam
##a=int(input())
##su=0
##for i in range(a):
##    b=input()
##    for i in b:
##        if i == 'U':      
##            su+=1
##        else:
##            break
##    print(su)
##    su=0


##petrol station
##a=int(input())
##b=[int(i) for i in input().split()]
##c=[int(i) for i in input().split()]
##su=0
##for i in range(a):
##    su+=b[i]*c[i]
##print(sum(b),su)



##Reverse Mode2
##a = input()
##c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##for i in a:
##    if i in c:
##        print(i.lower(),end='')



##Printing Books(with time limit exceeded error)
##a=int(input())
##for i in range(a):
##    b,c = [int(i) for i in input().split()]
##    tot = [c]
##    c=str(c)
##    l = ''
##    l += c
##    while True:
##        if len(l) < b:
##            c=int(c)
##            c+=1
##            tot.append(c)
##            l += str(tot[-1])   
##        else:
##            break
##    print()
##    if len(l) != b:
##        print(-1)
##    else:
##        print(len(tot))
        

##birthdate
##l=[]
##a=int(input())
##for i in range(a):
##    b = input().split()
##    l.append((int(b[3]),int(b[2]),int(b[1]),b[0]))
##l.sort()
##print(l[-1][3])
##print(l[0][3])

##NoNR
##while True:
##    try:
##        l = []
##        a = [int(i) for i in input().split()]
##        for i in a:
##            if i not in l:
##                l.append(i)
##        for i in l:
##            print(i,end=' ')
##        print()
##        l.clear()      
##    except EOFError:
##        break
        


##elections
##a=int(input())
##for i in range(a):
##    a,b,c = map(int,input().split())
##    if a == 0 and b == 0 and c == 0:
##        print(1,1,1)
##    else:
##        if a > b and a > c:
##            b = (a-b)+1
##            c = (a-c)+1
##            a=0
##        elif b > a and b > c:
##            a = (b-a)+1
##            c = (b-c)+1
##            b=0
##        elif c > a and c > b:
##            a = (c-a)+1
##            b = (c-b)+1
##            c=0
##        print(a,b,c)



##Mind Your PQs with time limit exceeded error
##tot=[]
##l=[]
##
##while True:
##    try:
##        a=[i for i in input().split()]
##        if a[0] == 'INSERT':
##            tot.append(int(a[1]))
##        if a[0] == 'REMOVE':
##            l.append(min(tot))
##            print(l[0])
##            tot.remove(min(tot))
##            l.clear()
##        if a[0] == 'END':
##            tot.clear()
##            l.clear()
##    except EOFError:
##        break




##Prime or not?
##while True:
##        prime = True
##        c = int(input())
##        if c == -1:
##            break
##        else:
##            if c <= 1:
##                prime = False
##            else:
##                for i in range(2,c):
##                    if i*i > c:
##                        break
##                    elif c % i == 0:
##                        prime = False
##                        break
##            if prime:
##                print(c,"is PRIME!!")
##            else:
##                print(c,"is COMPOSITE TT")
  


##Modular Operation
##a,b,c = map(int,input().split())
##print((a+b)%c,(a-b)%c,(a*b)%c)



##Prime Sieve with time limit exceeded
##l=[]
##a,b = map(int,input().split())
##for i in range(1,a+1):
##    l.append(i)
##co = 1
##for i in l:
##
##    prime = True
##    
##    if i <= 1:
##        prime = False
##    else:
##        for j in range(2,i):
##            if j*j > i:
##                co+=1
##                break
##            elif i % j == 0:
##                prime = False
##                break
##print(co)
##for i in range(b):
##    prime = True
##    c = int(input())
##   
##    if c <= 1:
##        prime = False
##    else:
##        for i in range(2,c):
##            if i*i > c:
##                break
##            elif c % i == 0:
##                prime = False
##                break
##    if prime:
##        print(1)
##    else:
##        print(0)



##longest common subsequence index out of range
##x=input()
##y=input()
##m=[[0 for i in range(len(x)+1)]for j in range(len(y)+1)]
##for i in range(len(x)):
##    for j in range(len(y)):
##        
##        if x[i] == y[j]:
##            m[i][j] = m[i-1][j-1]+1
##        else:
##            m[i][j] = max(m[i-1][j],m[i][j-1])
##print(m[-1][-1])

                   
##a = input()
##b = input()
##def lcs(s1, s2):
##    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
##    for i in range(len(s1)):
##        for j in range(len(s2)):
##            if s1[i] == s2[j]:
##                if i == 0 or j == 0:
##                    matrix[i][j] = s1[i]
##                else:
##                    matrix[i][j] = matrix[i-1][j-1] + s1[i]
##            else:
##                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)
##
##    cs = matrix[-1][-1]
##
##    return len(cs), cs
##
##s = lcs(a,b)
##print(s[0],s[1])


##Jumping Mario
##tot = []
##h = 0
##l = 0
##a=int(input())
##for j in range(a):
##    b = int(input())
##    c = [int(i) for i in input().split()]
##    for i in range(b-1):
##        
##        if c[i] < c[i+1]:
##            h+=1
##        elif c[i] > c[i+1]:
##            l+=1
##    print(f"Case {j+1}:",h,l)
##    l=0
##    h=0


##reverse binary (remember in b[-1::-1] -> b[start:end:step])
##su = 0
##a = int(input())
##b = bin(a)[2:]
##c = b[-1::-1]
##d = len(str(c))-1
##for i in c:
##    su += (2**d)*int(i)
##    d -=1
##print(su)


##mame & skate
##k,m,n = map(int,input().split())
##while True:
##    k -= m
##    if k < n:
##        print('Mame')
##        break
##    k -= n
##    if k < m:
##        print("Skat")
##        break

##Robot Instructions
##x = 0        
##l = []
##a = int(input())
##for i in range(a):
##    b = int(input())
##    for j in range(b):
##        c = input()
##        if c[-1] == 'T':
##            f = 0
##        else:
##            d = int(c.split()[-1])
##        if c == 'LEFT':
##            x-=1
##            l.append(-1)
##        elif c=='RIGHT':
##            x+=1
##            l.append(1)
##        else:
##            l.append(l[d-1])
##            x += l[d-1]
##    print(x)
##    x=0
##    l.clear()


##Dyanmic len(set(a[L:R]))
##a,b = map(int,input().split())
##c = [int(i) for i in input().split()]
##for i in range(b):
##    d,e,f = input().split()
##    e = int(e)
##    f = int(f)
##    if d == 'Q':
##        su = set(c[e:f])
##        print(len(su))
##    else:
##        c[e] = f

##cinema crowd(kattis)
##a,b = map(int,input().split())
##c =[int(i) for i in input().split()]
##su = 0
##l = []
##for i in range(b):
##    d = su + c[i]
##    if d <= a:
##        su += c[i]
##        l.append(c[i])
##print(len(c)-len(l))


##baby bites(kattis)
##n=int(input())
##b = input().split()
##su = 0
##for i in range(n):
##    if b[i] == 'mumble':
##        su+= i+1
##    else:
##        b[i] = int(b[i])
##        su += b[i]
##a = n*(n+1)/2
##if a == su:
##    print("makes sense")
##else:
##    print("something is fishy")



##score
##a = int(input())
##su = 0
##l = []
##for i in range(a):
##    b = input()
##    for j in b:
##        if j == 'O':
##            su+=1
##            l.append(su)
##        if j == 'X':
##            su = 0
##    print(sum(l))
##    l.clear()
##    su = 0
    
    
##cacho method 1
##l = []
##a = int(input())
##for i in range(a):
##    b = [int(i) for i in input().split()]
##    for i in range(len(b)-1):
##            if b[i]+1 == b[i+1]:
##                l.append(1)
##            else:
##                l.append(2)
##    d = set(l)
##    if d == {2}:
##        print('N')
##    elif len(d) == 1:
##        print('Y')
##    else:
##        print('N')
##    l.clear()

##cacho method 2
##escala = True
##a = int(input())
##for i in range(a):
##    b = [int(i) for i in input().split()]
##    for i in range(len(b)-1):
##            if b[i]+1 == b[i+1]:
##                escala = True
##            else:
##                escala = False
##                break
##    if escala == True:
##        print('Y')
##    else:
##        print('N')


##Reverse and Add **
##su = 1
##a = int(input())
##for i in range(a):
##    b = input()
##    while True:
##        c = b[-1::-1]
##        b = int(b) + int(c)
##        b = str(b)
##        c = b[-1::-1]
##        if c == b:
##            break
##        su += 1
##    print(su,b)
##    su = 1



##vinyl records
##from math import pi
##a = int(input())
##b = [int(i) for i in input().split()]
##l = []
##tot = 0
##for i in b:
##    area = pi*(i**2)
##    l.append(area)
##l.sort(reverse=True)
##for i in range(len(l)-1):
##    if i % 2 == 0:
##        sub = l[i+1] - l[i]
##        tot+=sub
##tot = round(tot,6)
##print(tot)



####coffee(old method 1)
##coffee = []
##person = []
##multi = []
##for k in range(5,101,5):
##    multi.append(k)
##a = int(input())
##for _ in range(a):
##    c,p = map(int,input().split())
##    for i in range(c):
##        d = input().split()
##        coffee.append(d)
##    for i in range(p):
##        e = input().split()
##        person.append(e)
##
##    for i in range(c):
##        for j in range(3):
##            coffee[i][j+1] = int(coffee[i][j+1])
##    delivery = 100//p
##    
##
##    for i in range(p):
##        if person[i][1] == 'small':
##            for j in range(c):
##                if person[i][2] == coffee[j][0]:
##                    su = delivery + coffee[j][1]
##            
##            for f in multi:
##                if su == f+1 or su == f-1:
##                    su = f
##            print(person[i][0],su)
##            
##        elif person[i][1] == 'medium':
##            for j in range(c):
##                if person[i][2] == coffee[j][0]:
##                    su = delivery + coffee[j][2]
##
##            for f in multi:
##                if su == f+1 or su == f-1:
##                    su = f
##            print(person[i][0],su)
##     
##
##        elif person[i][1] == 'large':
##            for j in range(c):
##                if person[i][2] == coffee[j][0]:
##                    su = delivery + coffee[j][3]
##
##            for f in multi:
##                if su == f+1 or su == f-1:
##                    su = f
##            print(person[i][0],su)
##    coffee.clear()
##    person.clear()

##method 2: coffee
##list_coffee = []
##list_person = []
##multiple_five = []
##
##for i in range(5,101,5):
##    multiple_five.append(i)
##
##a = int(input())
##for i in range(a):
##    c,p = map(int,input().split())
##    delivery = 100// p
##    for j in range(c):
##        coffee = input().split()
##        list_coffee.append(coffee)
##    for j in range(p):
##        person = input().split()
##        list_person.append(person)
##      
##    for _ in range(p):
##        if list_person[_][1] == 'small':
##            for j in range(c):
##                if list_coffee[j][0] == list_person[_][2]:
##                    total = delivery + int(list_coffee[j][1])
##                    break   
##        elif list_person[_][1] == 'medium':
##            for j in range(c):
##                if list_coffee[j][0] == list_person[_][2]:
##                    total = delivery + int(list_coffee[j][2])
##                    break
##        else:
##            for j in range(c):
##                if list_coffee[j][0] == list_person[_][2]:
##                    total = delivery + int(list_coffee[j][3])
##                    break
##                
##        if total-1 in multiple_five:
##            total = total-1
##        elif total+1 in multiple_five:
##            total = total+1
##        print(list_person[_][0],total)
##        
##    list_person.clear()
##    list_coffee.clear()



##Timmy the Lamb
##a = input().split()
##for i in a[0]:
##    if i in a[1]:
##          yes = True
##    else:
##        yes = False
##        break
##if yes and len(a[0]) == len(a[1]):
##    print('true')
##else:
##    print('false')


##Derivative **
##a = input().upper()
##a = a.split()
##alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##l = ''
##for i in range(len(a[0])):
##    if a[0][i] in alpha:
##        l += a[0][i]
##        ind = i
##        break
##if l in a[0] and l != '':
##    print(a[0][0:ind])
##else:
##    print(0)
    


##century **
##a = int(input())
##b = a // 100
##c = a % 100
##if c == 0:
##    print(b)
##else:
##    print(b+1)



##Back to High School Physics
##while 1:
##    try:
##        a,b = map(int,input().split())
##        c = a*(b*2)
##        print(c)
##    except:
##        break

##Parity Sort
##a = int(input())
##b = [int(i) for i in input().split()]
##eve = []
##odd = []
##for i in b:
##    if i % 2 == 0:
##        eve.append(i)
##    else:
##        odd.append(i)
##eve.sort()
##odd.sort()
##tot = eve+odd
##for i in tot:
##    print(i,end=' ')
        

##Compress        
##a = int(input())
##b = input().split()
##su = 0
##su2 = 0
##su3 = 0
##for i in range(a):
##    su += int(b[i][0])
##for i in range(a):
##    su2 += int(b[i][1])
##for i in range(a):
##    su3 += int(b[i][2])
##print(su,su2,su3)


##probability assignment
##from the module of random intake only randint(random integers generator)
##from random import randint
##
####Empty list for the random numbers
##randomList = []
##
####create a flag
##correct = False
##
####as long as the user input don't satisfy the warning error pop up
##while not correct:
##    num = int(input('how many random numbers you want to generate: '))
##    print('Enter the range of your random numbers to be generated')
##    ##This task should be performed because the second while loop will be infinite if not.
##    print(f'!!!Warning please Enter the range which can include at least {num} numbers!!!')
##    intial = int(input('Enter the starting number: '))
##    final = int(input('Enter the final number: '))
##
####entered range numbers of integer capacity  
##    element = (final - intial) + 1
##    if element < num:
##        print("you don't follow the warning enter again")
##        correct = False
##    else:
##        correct = True
##
####randint inculdes the intial and final in number in the random selection
##randomNum = randint(intial,final)
##
##for i in range(num):
####    To avoid number duplication we have inserted this code
##    while randomNum in randomList:
##        randomNum = randint(intial,final)
##    randomList.append(randomNum)
##
##print('The final generated random numbers are listed below')
##for number in randomList:
##    ##iterating in the list print the random numbers in horizontal manner
##    print(number,end = ' ')



##puwagime(ጳጉሚ) 6&5 calculator
##num = int(input('current year'))
## ጳጉሚ start from year 3 and there difference is 4(not finished project find for ጳጉሚ 7)
##using arthimetic sequence
##difference = 4
##startingYear = 3
##position = ((num - startingYear)/difference)+1
##position = str(position)
##if position[-2:] == '.0':
##    print('ጳጉሚ 6',position)
##else:
##    print('ጳጉሚ 5',position)
q










































































     
                











    
        











































        













    



























































































































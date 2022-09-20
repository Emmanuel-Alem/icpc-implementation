##guessing number game
##import random
##guess = int(input("choose a no between 1 and 5: "))
##rand = random.randint(1,5)
##if guess == rand:
##    print("well done")
##else:
##    if guess < rand:
##        print("too low")
##    else:
##        print("too high")
##    guess2 = int(input("pick second no"))
##    if guess2 == rand:
##        print("Correct")
##    else:
##        print("You lose")
##print("The hidden no is",rand)

#Star
##x,b,c = map(int,input().split())
##for i in range(x):
##    print(" "*(x-(i+1))+"*"*(i+1))
##print()
##
##for i in range(b):
##    print(" "*(b-(i+1))+"*"*(i+1))
##print()
##
##for i in range(c):
##    print(" "*(c-(i+1))+"*"*(i+1))
##print()


#x,*l = [int(i) for i in input().split()]


#reverse
##L=[]
##a = int(input())
##for i in range(a):
##    c = int(input())
##    L.append(c)
##L.reverse()
##for i in L:
##    print(i)


##a = input()
##c =0
##for i in range(len(a)):
##    if a[i]=="s" and a[i+1]=="s":
##        c += 1
##    else:
##        c =0
##if c >0:
##    print("hiss")
##else:
##    print("no hiss")

##License to Launch
##a = int(input())
##b=[int(i) for i in input().split()]
##c=min(b)
##print(b.index(c))


##Line Them Up
##L = []
##b = int(input())
##for i in range(b):
##    a = input()
##    L.append(a)
##
##if L == sorted(L):
##    print("INCREASING")
##elif L == sorted(L,reverse=True):
##    print("DECREASING")
##else:
##    print("NEITHER")


##Hissing Microphone
##a = input()
##if "ss" in a:
##    print("hiss")
##else:
##    print("no hiss")

##What does the fox say?
##n=int(input())
##for x in range(n):
##    a = input().split()
##    while 1:
##        b = input()
##        if b == "what does the fox say?":
##            break
##        c = b.split(" goes ")
##        while c[1] in a:
##            a.remove(c[1])
##    s=" "
##    s=s.join(a)
##    print(s)


##I've Been Everywhere
##L =[]
##a = int(input())
##for i in range(a):
##    v = int(input())
##    for i in range(v):
##        c = input()
##        L.append(c)
##    z = set(L)
##    print(len(z))
##    L.clear()




##Modulo
##L =[]
##for i in range(10):
##    a = int(input())
##    b = a%42
##    L.append(b)
##d=set(L)
##print(len(d))



##Seven Wonders
##a = input()
##d = {"C":0,"T":0,"G":0}
##for i in a:
##    d[i]+=1
##y=0
##m = min(d.values())
##
##for i in d:
##    y+=(d[i]**2)
##y += 7*m
##print(y)
    

##pot
##n=int(input())
##x=0
##for i in range(n):
##    m=int(input())
##    a=m%10
##    b=m//10
##    c=pow(b,a)
##    x+=c
##print(x)

##Candle Box
##a=int(input())
##b=int(input())
##c=int(input())
##d=[]
##e=[]
##for i in range(4,b+c+1):
##    f=(i*(i+1))//2-6
##    if f>b+c:
##        break
##    d.append(f)
##for i in range(a-1):
##    e.append(0)
##for i in range(3,b+c+1):
##    f=(i*(i+1))//2-3
##    if f>b+c:
##        break
##    e.append(f)
##for i in range(len(d)):
##    if d[i]+e[i] == b+c:
##        ind=i
##        break
##print(b-d[ind])
    

##Permuted Arithmetic Sequence
##a=int(input())
##for i in range(a):
##   b=[int(i) for i in input().split()]
##   c=b[1:]
##   if c[0]<c[1]:
##      mi=c[1]-c[0]
##      art=True
##      for i in range(1,len(c)-1):
##         if mi!=c[i+1]-c[i]:
##            art=False
##            break
##   else:
##      mi=c[0]-c[1]
##      art=True
##      for i in range(1,len(c)-1):
##         if mi!=c[i]-c[i+1]:
##            art=False
##            break
##   if art:
##      print("arithmetic")
##   else:
##      c.sort()
##      if c[0]<c[1]:
##         mi=c[1]-c[0]
##         art=True
##         for i in range(1,len(c)-1):
##            if mi!=c[i+1]-c[i]:
##               art=False
##               break
##      else:
##         mi=c[0]-c[1]
##         art=True
##         for i in range(1,len(c)-1):
##            if mi!=c[i]-c[i+1]:
##               art=False
##               break
##      if art:
##         print("permuted arithmetic")
##      else:
##         print("non-arithmetic")
            



##3D Printed Statues
##no_statues = int(input())
##count = 0
##while 1:
##   printer=pow(2,count)
##   if printer >= no_statues:
##      break
##   count+=1
##print(str(printer)+" number of printer has been created")
##print(str(count+1)+" number of day used to print statue")


##Bus
##a=[]
##for i in range(30):
##   if i==0:
##      a.append(1)
##   else:
##      a.append(int((a[i-1]+0.5)*2))
##n=int(input())
##for i in range(n):
##   b=int(input())
##   print(a[b-1])


##Watch Out For Those Hailstones!
##c=[]
##def h(n):
##   if n==1:
##      return c
##   elif n%2 == 0:
##      c.append(n//2)
##      return h(n//2)
##   else:
##      c.append(3*n+1)
##      return(h(3*n+1))
##a=int(input())
##c.append(a)
##print(sum(h(a)))




##printing books on cpd day7(not working)
##a= int(input())
##L=[]
##for i in range(a):
##    c,d=[int(i) for i in input().split()]
##    for i in range(d,1000000000000001):
##            f=str(i)
##            L.append(len(f))
##            if sum(L) == c:
##                print(len(L))
##                L.clear()
##                break
            
                
        

##Maximum Sum of Digits on cpd day7(not working)
##a=int(input())
##s1=0
##s2=0
##
##if a%2 == 0:
##    b=a//2
##    y=b-1
##    z=b+1
##    y=str(y)
##    for i in y:
##        s1+=int(i)
##    z=str(z)
##    for i in z:
##        s2+=int(i)
##else:
##    b=a//2
##    y=b
##    z=b+1
##    y=str(y)
##    for i in y:
##        s1+=int(i)
##    z=str(z)
##    for i in z:
##        s2+=int(i)
##
##print(s1+s2)







##count=0
##a=int(input())
##L=[]
##for i in range(a):
##    b,c=[int(i) for i in input().split()]
##    for i in range(c,1000000000000000):
##        i=str(i)
##        if count < b:
##            L.append(i)
##            count+=len(i)
##        else:
##            break
##    print(len(L))
##    L.clear()
    


##10 green bottles
##num = 10
##while num != 0:
##    print("There are",num,"green bottles hanging on the wall,\nif 1 green bottle should accidentally fall")
##    ans = int(input("how many green bottles will be hanging? "))
##    while 1:
##        if ans == num-1:
##            num-=1
##            break
##        else:
##            ans = int(input("NO,try again"))
##            if ans == num-1:
##                num-=1
##                break
##print("There are no bottles hanging")






            
        



















    

























    




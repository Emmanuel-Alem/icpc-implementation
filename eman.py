
##inp=input()
##for i in range(3):
##    print(inp,end=" ")
##
##a,b=[int(i) for i in input().split()]
##print((a*(b-1)+1))
##
##n=int(input())
##for i in range(n):
##    co=0
##    nn=[int(i) for i in input().split()]
##    c=nn[1:]
##    for i in c:
##        co+=(i-1)
##    print(co+1)
##
##a,b=(int(i) for i in input().split())
##print(a+b)
##
##
##a,b=input().split()
##if int(a)<int(b):
##    print(int(a),end=' ')
##    print(int(b),end=' ')
##else:
##    print(int(b),end=' ')
##    print(int(a),end=' ')
##    

##a=[i for i in input().split()]
##du=0
##for i in range(len(a)):
##    du+=a.count(a[i])
##
##if du==len(a):
##    print("yes")
##else:
##    print("no")


##FizzBuzz
##a,b,c = map(int,input().split())
##for i in range(c):
##    if (i+1)%a==0 and (i+1)%b==0:
##        print("FizzBuzz")
##    elif (i+1)%a==0:
##        print("Fizz")
##    elif (i+1)%b==0:
##        print("Buzz")
##    else:
##        print(i+1)

##no duplicate
##a=[i for i in input().split()]
##b=set(a)
##if len(b)==len(a):
##    print("yes")
##else:
##    print("no")
##h=[int(i) for i in input().split()]
##h.sort()
##y=input().upper()
##for i in y:
##    if i=='A':print(h[0],end=' ')
##    elif i=='C':print(h[-1],end=' ')
##    else:print(h[1],end=' ')



##Judging Moose
##a,b=(int(i) for i in input().split())
##if a==0 and b==0:
##    print("Not a mooose")
##elif a != b:
##    if a>b:
##        print("Odd",(2*a))
##    else:print("Odd",(2*b))
##elif a == b:
##    print("Even",(a+b))



##abc
##m=sorted([int(i) for i in input().split()])
##a=input().upper()
##for i in range(len(a)):
##    if a[i]=="A":
##        print(m[0],end=' ')
##    elif a[i]=="B":
##        print(m[1],end=' ')
##    elif a[i]=="C":
##        print(m[2],end=' ')

##sideways sorting



##arithmetic sequence
##n=int(input()) 
##print(n*(n+1)/2)

##apaxiaaans
##x=input()
##m=[x[0]]
##for i in x:
##    if i!=m[-1]:
##        m.append(i)
##print(m)
##print("".join(m))


##bonus string
##L=[]
##for i in range(3):
##    x=input()
##    L.append( (len(x),x) )
##L.sort()
##for i in L:
##    print(i[1])

##quadrant selection
##a=int(input())
##b=int(input())
##if a>0 and b>0:
##    print(1)
##elif a<0 and b>0:
##    print(2)
##elif a<0 and b<0:
##    print(3)
##else:
##    print(4)

##petrol station
##sum1=0
##sum2=0
##a=int(input())
##b=[int(i)for i in input().split()]
##c=[int(i)for i in input().split()]
##for i in range(a):
##    sum1+=b[i]
##for k in range(a):
##    sum2+=b[k]*c[k]
##
##print(sum1,end=" ")
##print(sum2)


##Evaluation
##n=0
##k=1
##a=input().upper()
##
##for i in range(len(a)):
##    if a[i]=="O":
##        n+=k
##        k=k+1
##    if a[i]=="X":
##        k=1
##print(n)


##Calculating memory
##a=int(input())
##su=0
##for i in range(a):
##    b,c = input().split()
##    c = int(c)
##    if b == "bool":
##        su+=1*c
##    if b == "char":
##        su+=1*c
##    if b == "float":
##        su+=4*c
##    if b == "int":
##       su+=4*c
##    if b == "double":
##        su+=8*c
##print(su)

##Even and Odd
##a=int(input())
##b=[int(i) for i in input().split()]
##sEven=0
##sOdd=0
##for i in range(a):
##    if b[i]%2 == 0:
##        sEven+=b[i]
##    else:
##        sOdd+=b[i]
##print(sOdd,"<=>",sEven)        


























































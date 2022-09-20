#f-Strings
##d=365
##print(f"There are {d} in a year")

##s = [1,2,3,4,5]
##for i in s:
##    if i>=3:
##        print("invalid ",i)
##        continue
##    print(i)


##a=[1,2,3]
##b=[5,4,6]
##d=a+b
##d.insert(2,8)
##print(d)
##print(round(4.5))

##from random import randint
##n= randint(1,5)
##print(n)

##import random as r
##n= r.randint(1,5)
##print(n)

##print(123_323_322)

##print('i the most "amazing" person') 

##a="the "
##b="is "
##temp=a
##a=b
##b=temp
##print(a+b)

#BMI CALCULATOR
##w = float(input("what's your weight in kilogram: "))
##h = float(input("what's your height in meters: "))
##bmi = round(w/h**2,2)
##if bmi<18.5:
##    print("your bmi is ",bmi)
##    print("underweight")
##elif 18.5<=bmi<=25:
##    print("your bmi is ",bmi) 
##    print("Normal weight")
##elif 25<bmi<=30:
##    print("your bmi is ",bmi)
##    print("over weight")
##elif bmi>30:
##    print("your bmi is ",bmi)
##    print("obese")
##else:
##    print("your bmi is ",bmi)
##    print("Clinically obese")


##wrong subtraction
##a,b = [int(i) for i in input().split()]
##for i in range(b):
##    if a%10 == 0:
##        a/=10
##    else:
##        a-=1
##print(int(a))


#Allocation kick start 2020
##add=0
##count=0
##testCase=int(input())
##for i in range(testCase):
##    num_house,badget=[int(i) for i in input().split()]
##    d = sorted([int(i) for i in input().split()])
##    for j in range(num_house):
##        add+=d[j]
##        if add <= badget:
##            count+=1
##        else:
##            break
##    print("Case #"+str(i+1)+":",count)
##    count=0
##    add=0

##co=0
##testCase=int(input())
##for i in range(testCase):
##    a,b=[int(i) for i in input().split()]
##    d=input().upper()
##for i in range(1,a+1):
##    z=i
##    w=a-i+1
##    print(d[z-1],d[w-1])
##    if d[z-1]!=d[w-1]:
##        co+=1
##print(co-1)    
##        


##a=int(input())
##total_weeks=90*52
##total_days=90*365
##total_month=90*12
##print(f"You have {total_days-(a*365)} days, {total_weeks -(a*52)} weeks and {total_month - (a*12)} months left.")


##print("welcome to tip cal")
##a=float(input("total bill? $"))
##b=int(input("percent?"))
##c=int(input("people split?"))
##print(f"each person pay: {round(((a*(b/100))+a)/c,2)}")


##nested if/else statement
##height = float(input("what's your height?"))
##if height < 120:
##    print("YOU ARE NOT ALLOWED!")
##else:
##    age = int(input("enter age")) 
##    if age <= 18:
##        print("wellcome you must pay $7")
##    elif 45 <= age <=55:
##        print("you can ride for free")
##    else:
##        print("wellcome you must pay $12")
##

##Leap year calculator(in leap year February becomes 29 days)
##method 1
##year = int(input("year checking?"))
##if year%400 == 0:
##    print("Leap year")
##else:
##    if year%100 == 0:
##        print("not leap year")
##    elif year%4 == 0:
##        print("leap year")
##    else:
##        print("not leap year")
##method 2
##year = int(input("year checking?"))
##if year%4 == 0:
##    if year%100 != 0:
##        print("Leap")
##    else:
##        if year%400 == 0:
##            print("Leap")
##        else:
##            print("not Leap")
##else:
##    print("not leap")
   

##pizza order
##size = input("what size? s,m,l")
##add_pepperoni = input("want pepperoni? y,n")
##extra_chesse = input("want chesse? y,n")
##sp=15
##mp=20
##lp=25
##bill = 0
##if size == 's':
##    bill += sp
##    if add_pepperoni == 'y':
##        bill += 2
##    if extra_chesse == 'y':
##        bill += 1
##elif size == 'm':
##    bill += mp
##    if add_pepperoni == 'y':
##        bill += 3
##    if extra_chesse == 'y':
##        bill += 1
##elif size == 'l':
##    bill += lp
##    if add_pepperoni == 'y':
##        bill += 3
##    if extra_chesse == 'y':
##        bill += 1
##else:
##    print("wrong input")
##print(bill)    
        
##Love calculator
##name1 = input("what is your name?").lower()
##name2 = input("what is their name?").lower()
##true_count= name1.count('t')+name2.count('t')+name1.count('r')+name2.count('r')+name1.count('u')+name2.count('u')+name1.count('e')+name2.count('e')
##love_count= name1.count('l')+name1.count('o')+name1.count('v')+name1.count('e')+name2.count('l')+name2.count('o')+name2.count('v')+name2.count('e')a
##score = str(true_count)+str(love_count)
##score = int(score)
##
##if score<10 or score>90:
##    print(f"your score is {score} , you go together like coke and mentos.")
##elif 40 < score < 50:
##    print(f"you score is {score} , you are alright together.")
##else:
##    print(score)

##end of file
##while True:
##        try:
##            s=input()
##            while s!= 'CLOSE':
##                a,b,c = map(str,input().split())
##                c = int(c)
##        except EOFError:
##            break

##import random
##while True:
##    try:
##        a= random.choice(["Rock","Paper","scissor"])
##        b= input()
##        if b != "Rock" or b != "Paper" or b != "scissor":
##            print("invalid input")
##        elif a=='Rock' and b=='paper':
##            print('win')
##        elif a == 'paper' and b=='scissor':
##            print('win')
##        elif a == 'scissor' and b=='Rock':
##            print('win')
##        elif a == b:
##            print('draw')
##        else:
##            print('lose')
##        print(a,b)
##    except EOFError:
##        break


##pypassword creator
##import random
##l=[]
##tot=[]
##print("Welcome to the PyPassword Generator")
##a=int(input("how many letters"))
####b=int(input("how many symbols"))
##c=int(input("how many numbers"))
##d= "ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
##e= "0123456789"
##for i in d:
##    l.append(i)
##for i in range(a):
##    f=random.choice(l)
##    tot.append(f)
##l.clear()
##for i in e:
##    l.append(i)
##for i in range(c):
##    k=random.choice(l)
##    tot.append(k)
##random.shuffle(tot)
##for i in range(a+c):
##    print(tot[i],end='')

##hang man
##import random
##l=[]
##a =["batman", "superman" ,"fast" ,"slow"]
##b=random.choice(a)
##print(f"enter {len(b)} letter word")
##for i in b:
##    print('-',end='')
##q=''
##for i in range(7):
##    c=input().lower()
##    if len(c) != len(b):
##        print("enter a correct number of letter")
##        print(f"you have lost {i+1} chance")
##        for i in b:
##            print('-',end='')
##    else:
##        if c == b:
##            print("win")
##            q+="win"
##            break
##        else:
##            for j in range(len(b)):
##                if b[j] == c[j]:
##                    l.append(b[j])
##                else:
##                    l.append("-")
##            print(f"you have lost {i+1} chance")
##            for k in l:
##                print(k,end='')
##            l.clear()
##if q!="win":
##    print("lose")



##caesar cipher('%26' is most important concept understand it!)
##alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
##tot=[]
##for i in alpha:
##    tot.append(i)
##a=input("encode or decode\n")
##if a!= 'encode' and a!= 'decode':
##    print('wrong input')
##    a=input("encode or decode\n")
##while True:
##    if a == 'encode':
##        b=input("type message").lower()
##        L=""
##        c=int(input("shift number"))%26
##        for i in b:
##            if i in alpha:
##                l = alpha.index(i)+c 
##                L += tot[l]
##            else:
##                L += i
##        print("encode result:",L)
##        L=""
##        d = input("yes or no")
##        if d == 'no':
##            print("Good bye")
##            break
##        elif d == 'yes':
##            a=input("encode or decode\n")
##    else:
##        b=input("type message").lower()
##        c=int(input("shift number"))%26
##        for i in b:
##            if i in alpha:
##                l = alpha.index(i)-c 
##                L += tot[l]
##            else:
##                L += i
##        print("decode result:",L)
##        L=''
##        d = input("yes or no")
##        if d == 'no':
##            print('Goodbye')
##            break
##        elif d == 'yes':
##            a=input("encode or decode\n")


##prime checker with time limit exceeded error
##n=int(input())
##prime = True
##for i in range(2,n):
##    if n % i == 0:
##        prime = False
##        break
## 
##if prime:
##    print("it is a prime number")
##else:
##    print("not prime number")



##prime and composite number checker
##prime=True
##n = int(input())
##if n <=1:
##    print('it is neither prime nor composite number')
##for i in range(2,n):
##    if i*i > n:
##        break
##    elif n%i == 0:
##        prime=False
##        break
##if prime:
##    print("it is a prime number")
##else:
##    print('it is a composite number')
        

#secret auction using dictionary
##print("welcome to the auction")
##l={}
##while True:
##    a=input("name")
##    b=int(input("your bid"))
##    l[a] = b 
##    c=input("any other bidders (yes or no)")
##    if c == 'no':
##        break
##co = 0
##wo = ''
##for i in l:
##    if l[i] > co:
##        co = l[i]
##        wo = i
##print(wo,co)

#calculator
##a=int(input("what's the first numbers?: "))
##print("+\n-\n*\n/\n")
##b=input("pick an operation: ")
##c=int(input("What's the next number?: "))
##def cal():
##    global tot
##    if b == '+':
##        tot = a+c
##        print(tot)
##    elif b == '-':
##        tot=a-c
##        print(tot)
##    elif b == '*':
##        tot = a*c
##        print(tot)
##    else:
##        tot = a/c
##        print(tot)
##cal()
##
##while True:
##    try:
##
##        d= input(f"type 'y' to continue from {tot} or 'n' from new")
##        if d == 'y':
##            b=input("pick an operation: ")
##            c=int(input("What's the next number?: "))
##            if b == '+':
##                tot += c
##                print(tot)
##            elif b == '-':
##                tot -= c
##                print(tot)
##            elif b == '*':
##                tot *= c
##                print(tot)
##            else:
##                tot /= c
##                print(tot)
##        else:
##            a=int(input("what's the first numbers?: "))
##            print("+\n-\n*\n/\n")
##            b=input("pick an operation: ")
##            c=int(input("What's the next number?: "))
##            cal()
##            
##            
##    except EOFError:
##        break


##black jack
##cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
##player = []
##comp = []
##
##import random
##
##deal  = input("do you want to deal(enter yes or no)")
##if deal == 'yes':
##    for i in range(2):
##        card_1 = random.choice(cards)
##        player.append(card_1)    
##    su = sum(player)
##    comp_card = random.choice(cards)
##    comp.append(comp_card)
##    su2 = comp_card
##    print(f"your cards: [{player[0]},{player[1]}]")
##    print("computer's first card:",comp_card)
##
##    while su2 <= 21:
##        comp_card = random.choice(cards)
##        if comp_card == 11 and su2 + comp_card > 21:
##            comp_card = 1
##        su2 += comp_card
##        if su2 > 21:
##            break
##        else:
##            comp.append(comp_card)
##
##    another_card = input("type 'y' to get another card, type 'n' to pass:")
##    if another_card == 'y':
##        card_3 = random.choice(cards)
##        if card_3 == 11 and su + card_3 > 21:
##            card_3 = 1
##        su += card_3
##        player.append(card_3)
##        print("your cards are",player)
##        while su <= 21:
##            
##            if sum(player) > 21:
##                break
##            else:
##                
##                another_card = input("type 'y' to get another card, type 'n' to pass:")
##                if another_card == 'n':
##                    break
##                else:
##                    card_3 = random.choice(cards)
##                    if card_3 == 11 and su + card_3 > 21:
##                        card_3 = 1
##                    su += card_3
##                    player.append(card_3)
##                    print("your cards are",player)
##    else:
##        print('you have finished')
##else:
##    print('good bye')
##
##print("players cards",player)
##print("computer cards",comp)
##if sum(player) > 21:
##    print('you lose')
##elif sum(player) > sum(comp):
##    print('you win')
##elif sum(player) == sum(comp):
##    print('you are tie')
##else:
##    print('you are loser')
    

##number guessing game
##from random import randint
##print('welcome to number guessing game')
##print("I'm thinking of a number between 1 and 100")
##a = input("Choose a difficulty. Type 'easy' or 'hard': ")
##b = randint(1,100)
##if a == 'easy':
##    su = 0
##    for i in range(10):
##        print(f'you have {10-i} attempts to guess the number.')
##        c = int(input('make a guess: '))
##        if c > b:
##            su += 1
##            if su != 10:
##                print('Too high.')
##                print('guess again')           
##        elif c < b:
##            su += 1
##            if su != 10:
##                print('Too low.')
##                print('guess again')         
##        else:
##            print('you have won; got the number')
##            break
##        if su == 10:
##            print("You've run out of guesses, you lose.")
##            print(f'the number was {b}')
##elif a == 'hard':
##    su = 0
##    for i in range(5):
##        print(f'you have {5-i} attempts to guess the number.')
##        c = int(input('make a guess: '))
##        if c > b:
##            su += 1
##            if su != 5:
##                print('Too high.')
##                print('guess again')
##        elif c < b:
##            su += 1
##            if su != 5:
##                print('Too low.')
##                print('guess again') 
##        else:
##            print('you have won; got the number')
##            break
##        if su == 5:
##                print("You've run out of guesses, you lose.")
##                print(f'the number was {b}')


##higherLower Game
##file = [('a',1),('b',2),('c',3),('d',4),('e',5)]
##import random
##newGame = True
##while newGame:
##    l = []
##    su = 0
##    b = random.choice(file)
##    c = random.choice(file)
##    while b == c:
##        b = random.choice(file)
##    l.append(b)
##    l.append(c)
##    print(b[0],c[0])
##    win = True
##    while win:
##        choice = input('higher or lower')
##        if choice == 'higher':
##            if l[-1][1] > l[-2][1]:
##                print('your right')
##                win = True
##                su+=1
##            else:
##                print("you'r wrong")
##                win = False
##        elif choice == 'lower':
##            if l[-1][1] > l[-2][1]:
##                print("you'r wrong")
##                win = False
##            else:
##                print("your right")
##                win = True
##                su+=1
##        if win:
##            wholeListAccessedChecker = 0
##            e = random.choice(file)
##            while e in l:
##                e = random.choice(file)
##                wholeListAccessedChecker +=1
##                if wholeListAccessedChecker > 100000:
##                    print('you have won the whole game')
##                    win = False
##                    break
##            if wholeListAccessedChecker < 100000:
##                print(l[-1][0],e[0])
##                l.append(e)
##    print(su)
##    newGame = input('do you want to play again? y/n')
##    if newGame == 'y':
##        newGame = True
##    elif newGame == 'n':
##        newGame = False
##    else:
##        newGame = False

##coffee machine
##menu = {
##    'espresso':{
##        'ingredients':{
##            'water':50,
##            'coffee':18,
##            'milk':0
##            },
##        'cost':1.5},
##    'latte':{
##        'ingredients':{
##            'water':200,
##            'coffee':24,
##            'milk':150
##            },
##        'cost':2.5},
##    'cappuccino':{
##        'ingredients':{
##            'water':250,
##            'coffee':24,
##            'milk':100
##            },
##        'cost':3.0},
##    }
##
##
##resources = {
##    "water":300,
##    "milk":200,
##    "coffee":100
##    }
##
##money = 0
##while True:
##    choice = input('what would you like?(espresso/latte/cappuccino) or you want to access info?(report) ')
##    if choice == 'report':
##        for i in resources:
##            print(i,resources[i])
##        print(f'Money: ${money}')
##
##    elif choice == 'latte':
##        if resources["water"] < menu['latte']['ingredients']['water']:
##            print('sorry there is not enough water')
##        else:
##            print('please insert coins.')
##            quart = int(input('how many quarters?: '))
##            dime = int(input('how many dimes?: '))
##            nickle = int(input('how many nickles?: '))
##            penny = int(input('how many pennies?: '))
##            bill = quart*.25 + dime*.10 + nickle*.5 + penny*.01
##            if bill < menu['latte']['cost']:
##                print("sorry that's not enough money. Money refunded.")
##            elif bill >= menu['latte']['cost']:
##                resources["water"] -= menu['latte']['ingredients']['water']
##                resources["milk"] -= menu['latte']['ingredients']["milk"]
##                resources["coffee"] -= menu['latte']['ingredients']["coffee"]            
##                money += menu['latte']['cost']
##                change = bill - menu['latte']['cost']
##                change = round(change,2)
##                print(f'here is ${change} in change.')
##                print('here is your latte enjoy')
##
##    elif choice == 'espresso':
##        if resources["water"] < menu['espresso']['ingredients']['water']:
##            print('sorry there is not enough water')
##        else:
##            print('please insert coins.')
##            quart = int(input('how many quarters?: '))
##            dime = int(input('how many dimes?: '))
##            nickle = int(input('how many nickles?: '))
##            penny = int(input('how many pennies?: '))
##            bill = quart*.25 + dime*.10 + nickle*.5 + penny*.01
##            if bill < menu['espresso']['cost']:
##                print("sorry that's not enough money. Money refunded.")
##            elif bill >= menu['espresso']['cost']:
##                resources["water"] -= menu['espresso']['ingredients']['water']
##                resources["milk"] -= menu['espresso']['ingredients']["milk"]
##                resources["coffee"] -= menu['espresso']['ingredients']["coffee"]
##                money += menu['espresso']['cost']
##                change = bill - menu['espresso']['cost']
##                change = round(change,2)
##                print(f'here is ${change} in change.')
##                print('here is your espresso enjoy')
##        
##    elif choice == 'cappuccino':
##            if resources["water"] < menu['cappuccino']['ingredients']['water']:
##                print('sorry there is not enough water')
##            else:
##                print('please insert coins.')
##                quart = int(input('how many quarters?: '))
##                dime = int(input('how many dimes?: '))
##                nickle = int(input('how many nickles?: '))
##                penny = int(input('how many pennies?: '))
##                bill = quart*.25 + dime*.10 + nickle*.5 + penny*.01
##                if bill < menu['cappuccino']['cost']:
##                    print("sorry that's not enough money. Money refunded.")
##                elif bill >= menu['cappuccino']['cost']:
##                    resources["water"] -= menu['cappuccino']['ingredients']['water']
##                    resources["milk"] -= menu['cappuccino']['ingredients']["milk"]
##                    resources["coffee"] -= menu['cappuccino']['ingredients']["coffee"]
##                    money += menu['cappuccino']['cost']            
##                    change = bill - menu['cappuccino']['cost']
##                    change = round(change,2)
##                    print(f'here is ${change} in change.')
##                    print('here is your cappuccino enjoy')
##
##    else:
##        break

    
                
    
                
    
    



        


























     
   










     

  






































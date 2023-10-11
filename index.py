    #1------------------------------------------------------------
    def distance(x1,y1,x2,y2):
        dist=(((x1-x2)**2)+((y1-y2)**2))**0.5
        return dist
        
    x1,y1,x2,y2=[float(input()) for i in range(4)]

    print(distance(x1,y1,x2,y2))
    #2-----------------------------------------------   -------------
    def power(a,n):
        res=1
        
        if n>0:
            for i in range(int(n)):
                res*=a
            return res
        elif n<0:
            for i in range(abs(int(n))):
                res*=a
            return 1/res
        else:
            return res
        
    a,n=[float(input()) for i in range(2)]

    print(power(a,n))
    #3------------------------------------------------------------
    def fib(n):
        if n==1 or n==2:
            return 1
        else:
            return fib(n-1)+fib(n-2)

    n=int(input())
    print(fib(n))
    #4------------------------------------------------------------
    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('Да')
    else:
        print('Нет')
    #5------------------------------------------------------------
    def square(a):
        p = 4*a
        s = a*a
        d = (a**2) / 2
        d = d**0.5
        
        k = (p, s, d)
        
        return k
        
    print(square(16))
    #6------------------------------------------------------------
    def season(month):

        if month == 12 or month < 3:
            return "Зима"
        elif month == 3 or month < 6:
            return "Весна"
        elif month == 6 or month < 9:
            return "Лето"
        else:
            return "Осень"

    #7------------------------------------------------------------
    def bank():
        stavka = 10
        n = int(input("Сколько у Вас денег?""\n""-> "))
        years = int(input("На сколько лет хотите сделать вклад?""\n""-> "))

        for i in range(years):
            n = int(n+stavka*n/100)
            print("По итогу вы получаете", n, "рублей")
    bank()
    #8------------------------------------------------------------
    def is_prime(x):
        f=True
        for i in range(2,int(x**0.5)):
            if x%i == 0:
                f=False
            return(f)
    a= int(input("ввести число: "))
    print(is_prime)
    #9------------------------------------------------------------
    def check_date(d,m,y):
        if d<0 or m<0 or n<0:
            return False
        mon=[31,28,31,30,31,30,31,31,30,31,30,31]
        if y%400==0 or ((y%4==0) and (y%100 != 0)):
            mon[1]=29
        if m>=1 and m<=12:
        if d>0 and d<=mon[m-1]:
            return True
        return False

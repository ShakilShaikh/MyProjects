# In the name of Allah
# MyPy 3.0
# By Shakil

# ============================= Imports ================================

import time,os,sys

# -------------------------------- X --------------------------------

def say(x): # To Print anything
    print x

def wait(n): # Wait in Seconds
    time.sleep(n)

def fprint(filename): # print file content
    try:
        x=open(filename,'r').read()
        print x
    except IOError,e:
        print e
def get_file_content(filename): # get file content
    try:
        x=open(filename,'r').read()
        return x
    except IOError,e:
        raise IOError

def d2b(num): # Decimal to Binary
    n=int(num)
    return '{0:b}'.format(n)

def d2o(num): # Decimal to Octal
    o=str(num)
    a=int(o,8)
    return a

def d2h(num): # Decimal to Hexa
        a=num/16
        res=str(a)
        b=num%16
        c=str(b)
        rem=""
        if c=="0":
                rem+="0"
        elif c=="1":
                rem+="1"
        elif c=="2":
                rem+="2"
        elif c=="3":
                rem+="3"
        elif c=="4":
                rem+="4"
        elif c=="5":
                rem+="5"
        elif c=="6":
                rem+="6"
        elif c=="7":
                rem+="7"
        elif c=="8":
                rem+="8"
        elif c=="9":
                rem+="9"
        elif c=="10":
                rem+="A"
        elif c=="11":
                rem+="B"
        elif c=="12":
                rem+="C"
        elif c=="13":
                rem+="D"
        elif c=="14":
                rem+="E"
        elif c=="15":
                rem+="F"
        ans=res+rem
        return ans

def b2d(num): # Binary to Decimal
    b=str(num)
    a=int(b,2)
    return a

def b2o(num): # Binary to Octal
    b=str(num)
    a=int(b,2)
    d2o(a)

def b2h(num): # Binary to Hexa
    b=str(num)
    a=int(b,2)
    d2h(a)

def o2d(num): # Octal to Decimal
    a=num/8
    b=num%8
    c=str(a)
    d=str(b)
    ans=c+d
    return int(ans)

def o2b(num): # Octal to Binary
    a=num/8
    b=num%8
    c=str(a)
    d=str(b)
    ans=c+d
    d2b(int(ans))

def o2h(num): # Octal to Hexa
    a=num/8
    b=num%8
    c=str(a)
    d=str(b)
    ans=c+d
    d2h(int(ans))


def h2d(hexa): # Hexa to Decimal
    hexa=str(hexa)
    hexi=int(hexa,16)
    return hexi

def h2b(hexa): # Hexa to Binary
    hexa=str(hexa)
    hexi=int(hexa,16)
    d2b(hexi)

def h2o(hexa): # Hexa to Octal
    hexa=str(hexa)
    hexi=int(hexa,16)
    d2o(hexi)

# Created on 23 April 2020
# by Gus Yudha

#Penjumlahan Geometri
"""
Input 1 :
3
Output 1 :
1.875

Input 2 :
4
Output 2 :
1.93750
"""

#################################
def gJumlah(s):
    if s==0:
        return 1
    cal=1/(2**s)
    r=gJumlah(s-1)
    hasil=r+cal
    return hasil
s=int(input())
x=gJumlah(s)
print("%.5f" %x)


#Cek Palindrom (Rekrusif)
"""
Input 1 :
racecar
Output 1:
true

Input 2 :
ninja
Output 2:
false
"""

#################################
def Palindrome(str):
    ukuran = len(str)
    if ukuran <= 1:
        return True
    if str[0] != str[ukuran-1]:
        return False
    return Palindrome(str[1:-1])

from sys import setrecursionlimit as srl
srl(11000)
str = input()
if Palindrome(str):
    print('true')
else:
    print('false')


#Penjumlahan Angka (Rekrusif)
"""
Input 1 :
12345
Output 1 :
15

Input 2 :
9
Output 2 :
9
"""

#################################
def jumlahAngka(n):
    if n == 0:
        return 0

    sA = jumlahAngka(n // 10)
    return sA + n % 10

from sys import setrecursionlimit as srl
srl(11000)
n = int(input())
print(jumlahAngka(n))


#Perkalian (rekrusif)
"""
Input 1 :
3
5
Output 1 :
15

Input 2 :
4
0
Output 2 :
0
"""

#################################
def kali(m, n):
    if m == 0 or n == 0:
        return 0

    if n > 0:
        sA = kali(m, n - 1)
        return sA + m

    else:
        sA = kali(m, n + 1)
        return sA - m

from sys import setrecursionlimit as srl
srl(11000)
m = int(input())
n = int(input())
print(kali(m, n))


#Hitung Nol
"""
Input 1 :
10204
Output 1 :
2

Input 2 :
708000
Output 2 :
4
"""

#################################
def hitungNol(n):
    if n < 0:
        n *= -1

    if n < 10:
        if n == 0:
            return 1
        return 0

    sA = hitungNol(n // 10)
    if n % 10 == 0:
        sA += 1
    return sA

from sys import setrecursionlimit as srl
srl(11000)
n = int(input())
print(hitungNol(n))


#String ke Integer
"""
Input 1 :
1231
Output 1 :
1231

Input 2 :
12567
Output 2 :
12567
"""

#################################
def string_int(n):
    a=int(n)
    return a

n=input()
r=string_int(n)
print(r)


#Sepasang bintang
"""
Input 1 :
hello
Output 1:
hel*lo

Input 2 :
aaaa
Output 2 :
a*a*a*a
"""

#################################
def pasangBintang(Input, Output, i=0):
    Output = Output + Input[i]

    if (i == len(Input) - 1):
        print(Output)
        return;

    if (Input[i] == Input[i + 1]):
        Output = Output + '*';

    pasangBintang(Input, Output, i + 1);

if __name__ == "__main__":
    Input = input()
    Output = ""
    pasangBintang(Input, Output);


#Cek AB
"""
Input 1 :
abb
Output 1 :
true

Input 2 :
abababa
Output 2 :
false
"""

#################################
def cekAB(str):
    if (len(str) == 0):
        return True

    if (str[0] == 'a'):
        if (len(str[1:]) > 1 and str[1:3] == 'bb'):
            return cekAB(str[3:])

        else:
            return cekAB(str[1:])

    else:
        return False

str = input()
if (cekAB(str)):
    print('true')
else:
    print('false')


#Tangga
Input 1 :
4
Output 1 :
7

Input 2 :
5
Output 2 :
13

#################################
def tangga(n):
    if (n < 3):
        return n

    if n == 3:
        return 4
    return tangga(n - 1) + tangga(n - 2) + tangga(n - 3)

n = int(input())
hitung = tangga(n)
print(hitung)

# Created on 01 December 2020
# by Gus Yudha

#Pangkat
Input 1 :
3 4
Output 1 :
81

Input 2 :
2 5
Output 2 :
32

#################################
def pangkat(X,N):
    output=X**N
    return output

str=input().split()
x,n=int(str[0]),int(str[1])
r=pangkat(x,n)
print(r)


#Penjumlahan Array
Input 1 :
3
9 8 9
Output 1 :
26

Input 2 :
3
4 2 1
Output 2 :
7

#################################
n=int(input())
li=[int(x) for x in input().split()]
jumlah = 0
for list_ele in li:
    jumlah=jumlah+list_ele
print(jumlah)


#Cek angka pada array
Input 1 :
3
9 8 10
8
Output 1 :
true

Input 2 :
3
9 8 10
2
Output 2 :
false

#################################
def angkaDiArray(li):
    if x in li:
        print("true")
    else:
        print("false")

from sys import setrecursionlimit as srl

srl(11000)
n = int(input())
li = [int(x) for x in input().split()]
x = int(input())
angkaDiArray(li)


#Temukan Index angka pertama pada array
Input :
4
9 8 10 8
8
Output :
1

#################################
def indexPertama(a,x):
    l=len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    sL=a[1:]
    sLO=indexPertama(sL,x)
    if sLO==-1:
        return -1
    else:
        return sLO+1

from sys import setrecursionlimit as srl
srl(11000)
n=int(input())
a=list(int(i) for i in input().strip().split(' '))
x=int(input())
r=indexPertama(a,x)
print(r)


#Temukan Index angka terakhir pada array
Input :
4
9 8 10 8
8
Output :
3

#################################
def indexTerakhir(a,x):
    l=len(a)
    if l==0:
        return -1
    sL=a[1:]
    sLO=indexTerakhir(sL,x)
    if sLO != -1:
        return sLO+1
    else:
        if a[0]==x:
            return 0
        else:
            return -1

from sys import setrecursionlimit as srl
srl(11000)
n=int(input())
a=list(int(i) for i in input().strip().split(' '))
x=int(input())
r=indexTerakhir(a,x)
print(r)

# Created on 05 May 2020
# by Gus Yudha

#Pangkat
"""
Input 1 :
3 4
Output 1 :
81

Input 2 :
2 5
Output 2 :
32
"""

#################################
def pangkat(x, n):
    if n == 0:
        return 1

    sA = pangkat(x, n - 1)

    return sA * x

from sys import setrecursionlimit as srl
srl(11000)
x, n = list(int(i) for i in input().strip().split(' '))
print(pangkat(x, n))


#Array Simpangan
"""
Input 1 :
6
2 6 8 5 4 3
4
2 3 4 7
Output 1 :
2
4
3

Input 2 :
4
2 6 1 2
5
1 2 3 4 2
Output 2 :
2
2
1
"""

#################################
def simpangan(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            print(arr1[i])
            i += 1
            j += 1

n1 = int(input())
arr1 = list(int(i) for i in input().strip().split(' '))
n2 = int(input())
arr2 = list(int(i) for i in input().strip().split(' '))
simpangan(arr1, arr2)


#Temukan elemen unik
"""
Input :
7
2 3 1 6 3 6 2
Output :
1
"""

#################################
def cariUnik(li):
    ele = li[0]
    for i in range(1, len(li)):
        ele = ele ^ li[i]
    return ele

n = int(input())
li = [int(x) for x in input().split()]
unik = cariUnik(li)
print(unik)


#Duplikasi dalam array
"""
Input:
9
0 7 2 5 4 7 1 3 6
Output:
7
"""

#################################
def angkaDuplikat(arr):
    n = len(arr) - 2
    jumlahTotal = 0

    for i in arr:
        jumlahTotal += i

    #jumlah n, angka natural
    jumlah = int(n*(n+1)/2)
    return jumlahTotal - jumlah

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
hasil=angkaDuplikat(arr)
print(hasil)


#Pasangan penjumlahan dalam array
"""
Input:
9
1 3 6 2 5 4 3 2 4
7
Output :
1 6
3 4
3 4
2 5
2 5
3 4
3 4
"""

#################################
n = int(input())
a = [int(x) for x in input().split()]
jumlah = int(input())

for i in range (len(a)):
    for j in range (i+1,len(a)):
        if a[i]+a[j]==jumlah:

            if(a[i]<a[j]):
                print(a[i]," ",a[j])

            else:
                print(a[j]," ",a[i])


#Penjumlahan tiga serangkai
"""
Input:
7
1 2 3 4 5 6 7
12
Output:
1 4 7
1 5 6
2 3 7
2 4 6
3 4 5
"""

#################################
def hitung(arr, x):
    pencacah = 0
    for i in arr:

        if i == x:
            pencacah += 1

    return pencacah

def penjumlahan(arr, x):
    arr.sort()

    for k in range(len(arr) - 2):
        i, j = k + 1, len(arr) - 1
        while j > i:

            if arr[i] + arr[j] + arr[k] == x:
                dup_j = hitung(arr[i + 1:], arr[j])

                for z in range(dup_j):
                    print(arr[k], arr[i], arr[j])

                i += 1

            elif arr[i] + arr[j] + arr[k] > x:
                j -= 1

            elif arr[i] + arr[j] + arr[k] < x:
                i += 1

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
jumlahnya = int(input())
penjumlahan(arr, jumlahnya)

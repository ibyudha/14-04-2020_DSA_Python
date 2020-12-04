# Created on 04 December 2020
# by Gus Yudha

#Balik LL
"""
Input :
1 2 3 4 5 -1
Output :
5 4 3 2 1
"""

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(kepala):
    def __init__(self):
        kepala = None
    sebelum = None
    sekarang =kepala
    while(sekarang is not None):
        selanjutnya = sekarang.next
        sekarang.next = sebelum
        sebelum = sekarang
        sekarang = selanjutnya
    kepala = sebelum
    return kepala

def ll(arr):
    if len(arr)==0:
        return None
    kepala = Simpul(arr[0])
    ekor = kepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return kepala
def printll(kepala):
    while kepala:
        print(kepala.data, end=' ')
        kepala = kepala.next
    print()

from sys import setrecursionlimit as srl
srl(10000)
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
r=reverse(l)
printll(r)


#Titik tengah LL
"""
Input 1 :
1 2 3 4 5 -1
Output 1 :
3

Input 2 :
1 2 3 4 -1
Output 2 :
2
"""

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def midpoint_linkedlist(kepala):
    belakang=kepala
    depan=kepala
    while (depan.next!=None) and (depan.next.next!=None):
        belakang=belakang.next
        depan=depan.next.next
    return belakang

def ll(arr):
    if len(arr)==0:
        return None
    kepala = Simpul(arr[0])
    ekor = kepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return kepala

arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
simpul = midpoint_linkedlist(l)
if simpul:
    print(simpul.data)


#Gabung 2 LL terurut
"""
Input :
 2 5 8 12 -1
 3 6 9 -1
Output :
 2 3 5 6 8 9 12
"""

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(kepala1,kepala2):
    temp = None
    if kepala1 is None:
        return kepala2
    if kepala2 is None:
        return kepala1
    if kepala1.data <= kepala2.data:
        temp = kepala1
        temp.next = merge(kepala1.next, kepala2)
    else:
        temp = kepala2
        temp.next = merge(kepala1, kepala2.next)
    return temp

def ll(arr):
    if len(arr)==0:
        return None
    kepala = Simpul(arr[0])
    ekor = kepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return kepala

def printll(kepala):
    while kepala:
        print(kepala.data, end=' ')
        kepala = kepala.next
    print()

from sys import setrecursionlimit as srl
srl(50000)
arr1=list(int(i) for i in input().strip().split(' '))
arr2=list(int(i) for i in input().strip().split(' '))
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)


#Kode : Merge Sort
"""
Input :
1 4 5 2 -1
Output :
1 2 4 5
"""

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.kepala = None

def ambilTengah(kepala):
    if (kepala == None):
        return kepala
    belakang = kepala
    depan = kepala
    while (depan.next != None and depan.next.next != None):
        belakang = belakang.next
        depan = depan.next.next
    return belakang

def mergeTerurut(a, b):
    hasil = None
    if a == None:
        return b
    if b == None:
        return a
    if a.data <= b.data:
        hasil = a
        hasil.next = mergeTerurut(a.next, b)
    else:
        hasil = b
        hasil.next = mergeTerurut(a, b.next)
    return hasil

def mergeSort(kepala):
    if kepala == None or kepala.next == None:
        return kepala
    tengah = ambilTengah(kepala)
    lanjutKeTengah = tengah.next
    tengah.next = None
    kiri = mergeSort(kepala)
    kanan = mergeSort(lanjutKeTengah)
    listTerurut = mergeTerurut(kiri, kanan)
    return listTerurut

def ll(arr):
    if len(arr) == 0:
        return None
    kepala = Simpul(arr[0])
    ekor = kepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return kepala

def printll(kepala):
    while kepala:
        print(kepala.data, end=' ')
        kepala = kepala.next
    print()

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)


#Temukan sebuah simpul di LL (recursif)
"""
Input 1 :
3 4 5 2 6 1 9 -1
5
Output 1 :
2

Input 2 :
3 4 5 2 6 1 9 -1
6
Output 2 :
4
"""

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def cariSimpul(kepala,number, index):
    if (kepala == None):
        return -1
    if (kepala.data == number) :
        return index
    return cariSimpul(kepala.next,number, index+1)

def ll(arr):
    if len(arr)==0:
        return None
    kepala = Simpul(arr[0])
    ekor = kepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return kepala

def printll(kepala):
    while kepala:
        print(kepala.data, end=' ')
        kepala = kepala.next
    print()

from sys import setrecursionlimit as srl
srl(11000)
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
angkaYangDicari=int(input())
index = cariSimpul(l,angkaYangDicari, 0)
print(index)


#EaD LL
"""
Input 1 :
1 4 5 2 -1
Output 1 :
1 5 4 2

Input 2 :
1 11 3 6 8 0 9 -1
Output 2 :
1 11 3 9 6 8 0 
"""

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def arranged_LL(kepala):
    oH=None
    oT=None
    eH=None
    eT=None
    if kepala is None or kepala.next is None:
        return kepala
    while kepala!=None:
        if kepala.data%2==1:
            if oH is None:
                oH=kepala
                oT=kepala
                kepala=kepala.next
            else:
                oT.next=kepala
                oT=oT.next
                kepala=kepala.next
        else:
            if eH is None:
                eH=kepala
                eT=kepala
                kepala=kepala.next
            else:
                eT.next=kepala
                eT=eT.next
                kepala=kepala.next
    if oH is not None:
        if eH is not None:
            oT.next=eH
            eT.next=None
        else:
            oT.next=None
        return oH
    else:
        eT.next=None
        return eH
def ll(arr):
    if len(arr)==0:
        return None
    kepala = Simpul(arr[0])
    ekor = kepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return kepala

def printll(kepala):
    while kepala:
        print(kepala.data, end=' ')
        kepala = kepala.next
    print()

arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = arranged_LL(l)
printll(l)


#Hapus setiap simpul N
"""
Input 1 :
1 2 3 4 5 6 7 8 -1
2
2
Output 1 :
1 2 5 6

Input 2 :
1 2 3 4 5 6 7 8 -1
2
3
Output 2 :
1 2 6 7
"""

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def lewatiMHapusN(kepala, M, N):
    if kepala is None:
        return

    t1 = kepala
    i = 0
    j = 0
    while i < M - 1:
        if t1 is not None:
            t1 = t1.next
        else:
            return
        i += 1

    while j < N:
        if t1.next is not None:
            t1.next = t1.next.next
        else:
            return
        j += 1

    t2 = t1.next

    lewatiMHapusN(t2, M, N)
    return kepala

def ll(arr):
    if len(arr) == 0:
        return None
    kepala = Simpul(arr[0])
    ekor = kepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return kepala

def printll(kepala):
    while kepala:
        print(kepala.data, end=' ')
        kepala = kepala.next
    print()

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
m = int(input())
n = int(input())
l = lewatiMHapusN(l, m, n)
printll(l)


#tukar 2 simpul LL
"""
Input 1 :
3 4 5 2 6 1 9 -1
3 4
Output 1 :
3 4 5 6 2 1 9

Input 2 :
3 4 5 2 6 1 9 -1
2 4
Output 2 :
3 4 6 2 5 1 9
"""

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def tukarSimpul(kepala, i, j):
    skrg = kepala
    sebelum = sebelumi = skrgi = sebelumj = skrgj = None
    hitung = 0
    while skrg != None:
        if hitung == i:
            sebelumi = sebelum
            skrgi = skrg
        elif hitung == j:
            sebelumj = sebelum
            skrgj = skrg
        sebelum = skrg
        skrg = skrg.next
        hitung += 1
    if (skrgi == None or skrgj == None):
        return

    if sebelumi == None:
        kepala = skrgj
    else:
        sebelumi.next = skrgj

    if sebelumj == None:
        kepala = skrgi
    else:
        sebelumj.next = skrgi

    skrg = skrgi.next
    skrgi.next = skrgj.next
    skrgj.next = skrg
    return kepala

    pass

def ll(arr):
    if len(arr) == 0:
        return None
    kepala = Simpul(arr[0])
    ekor = kepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return kepala

def printll(kepala):
    while kepala:
        print(kepala.data, end=' ')
        kepala = kepala.next
    print()

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
i, j = list(int(i) for i in input().strip().split(' '))
l = tukarSimpul(l, i, j)
printll(l)


#kBalik
"""
Input 1 :
1 2 3 4 5 6 7 8 9 10 -1
4
Output 1 :
4 3 2 1 8 7 6 5 10 9

Input 2 :
1 2 3 4 5 -1
2
Output 2 :
2 1 4 3 5

Input 3 :
1 2 3 4 5 6 7 -1
3
Output 3 :
3 2 1 6 5 4 7
"""

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def kBalik(kepala, n):
    sekarang = kepala
    selanjutnya = None
    sebelum = None
    hitung = 0
    while (sekarang is not None and hitung < n):
        selanjutnya = sekarang.next
        sekarang.next = sebelum
        sebelum = sekarang
        sekarang = selanjutnya
        hitung += 1
    if selanjutnya is not None:
        kepala.next = kBalik(selanjutnya, n)
    return sebelum

def ll(arr):
    if len(arr) == 0:
        return None
    kepala = Simpul(arr[0])
    ekor = kepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return kepala

def printll(kepala):
    while kepala:
        print(kepala.data, end=' ')
        kepala = kepala.next
    print()

# Baca element link list termasuk -1
arr = list(int(i) for i in input().strip().split(' '))
# Buat ll baru setelah menghapus 1 dari list
l = ll(arr[:-1])
i = int(input())
l = kBalik(l, i)
printll(l)


#Bubble Sort LL
"""
Input :
1 4 5 2 -1
Output :
1 2 4 5
"""

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def ambilTengah(kepala):
    if (kepala == None):
        return kepala
    belakang = kepala
    depan = kepala
    while (depan.next != None and depan.next.next != None):
        belakang = belakang.next
        depan = depan.next.next
    return belakang

def mergeTerurut(a, b):
    hasil = None
    if a == None:
        return b
    if b == None:
        return a
    if a.data <= b.data:
        hasil = a
        hasil.next = mergeTerurut(a.next, b)
    else:
        hasil = b
        hasil.next = mergeTerurut(a, b.next)
    return hasil

def mergeSort(kepala):
    if kepala == None or kepala.next == None:
        return kepala
    tengah = ambilTengah(kepala)
    lanjutKeTengah = tengah.next
    tengah.next = None
    kiri = mergeSort(kepala)
    kanan = mergeSort(lanjutKeTengah)
    listTerurut = mergeTerurut(kiri, kanan)
    return listTerurut

def ll(arr):
    if len(arr) == 0:
        return None
    kepala = Simpul(arr[0])
    ekor = kepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return kepala

def printll(kepala):
    while kepala:
        print(kepala.data, end=' ')
        kepala = kepala.next
    print()

# Baca element link list termasuk -1
from sys import setrecursionlimit as srl

srl(11000)
arr = list(int(i) for i in input().strip().split(' '))
# Buat ll baru setelah menghapus 1 dari list
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)

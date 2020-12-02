# Created on 02 December 2020
# by Gus Yudha


#Panjang LL
Input 1 :
1
3 4 5 2 6 1 9 -1
Output 1 :
7

Input 2 :
2
10 76 39 -3 2 9 -23 9 -1
-1
Output 2 :
8
0

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def cariPanjang(kepala):
    if kepala == None:
        return 0

    if kepala.next == None:
        return 1

    return cariPanjang(kepala.next) + 1

def ll(arr):

    if arr == []:
        return None

    kepala = Simpul(arr[0])
    ekor = kepala

    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next

    return kepala

from sys import setrecursionlimit as srl
srl(11000)

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
panjangnya = cariPanjang(l)
print(panjangnya)


#Print ith Simpul
Input 1 :
1
3 4 5 2 6 1 9 -1
3
Output 1 :
2

Input 2 :
2
3 4 5 2 6 1 9 -1
0
9 8 4 0 7 8 -1
3
Output 2 :
3
0

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def ithSimpul(ddkepala, i):
    hitung = 0
    sekarang = ddkepala
    while hitung < i and sekarang != None:
        sekarang = sekarang.next
        hitung = hitung + 1
    return sekarang

def ll(arr):
    if arr == []:
        return None
    ddkepala = Simpul(arr[0])
    ekor = ddkepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return ddkepala

from sys import setrecursionlimit as srl

srl(11000)
arr = list(int(i) for i in input().strip().split(' '))
i = int(input())
l = ll(arr[:-1])
hasil = ithSimpul(l, i)
if hasil:
    print(hasil.data)


#Hapus Simpul
Input 1 :
1
3 4 5 2 6 1 9 -1
3
Output 1 :
3 4 5 6 1 9

Input 2 :
2
3 4 5 2 6 1 9 -1
0
10 20 30 40 50 60 -1
7
Output 2 :
4 5 2 6 1 9
10 20 30 40 50 60

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def hapusRec(ddkepala, i):
    if (i < 0) :
        return ddkepala
    if (ddkepala == None):
        return None
    if (i == 0) :
        res = ddkepala.next
        return res
    ddkepala.next = hapusRec(ddkepala.next, i-1 )
    return ddkepala
    pass

def ll(arr):
    if len(arr)==0:
        return None
    ddkepala = Simpul(arr[0])
    ekor = ddkepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return ddkepala

def printll(ddkepala):
    while ddkepala:
        print(ddkepala.data, end=' ')
        ddkepala = ddkepala.next
    print()

from sys import setrecursionlimit as srl
srl(11000)

arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
i=int(input())
l = hapusRec(l, i)
printll(l)


#Temukan sebuah simpul di linked list
Input 1 :
2
3 4 5 2 6 1 9 -1
5
10 20 30 40 50 60 70 -1
6
Output 1 :
2
-1

Input 2 :
1
3 4 5 2 6 1 9 -1
6
Output 2 :
4

Penjelasan untuk Input 2 :
Mencari dengan 1 lompatan, N = 6 muncul di posisi 4 (dengan asumsi index dimulai dari 0)

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def cariSimpul(ddkepala,angka, index):
    if (ddkepala == None):
        return -1
    if (ddkepala.data == angka) :
        return index
    return cariSimpul(ddkepala.next,angka, index+1)

def ll(arr):
    if len(arr)==0:
        return None
    ddkepala = Simpul(arr[0])
    ekor = ddkepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return ddkepala

def printll(ddkepala):
    while ddkepala:
        print(ddkepala.data, end=' ')
        ddkepala = ddkepala.next
    print()

from sys import setrecursionlimit as srl
srl(11000)

arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
angkaCarian=int(input())
index = cariSimpul(l,angkaCarian, 0)
print(index)


#Menyelipkan dari depan
Input 1 :
2
1 2 3 4 5 -1
3
10 20 30 40 50 60 -1
5
Output 1 :
3 4 5 1 2
20 30 40 50 60 10

Input 2 :
1
10 6 77 90 61 67 100  -1
4
Output 2 :
90 61 67 100 10 6 77

Penjelasan untuk Input 2 :
Kita diminta memindahkan 4 simpul (90->61->67->100) kedepan list.
Ketika memindahkannya kedepan maka sisa simpulnya (10->6->77) di sambung setelah 100. 
Sehingga, list baru dibentuk dengan 90 sebagai kepala yang baru

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def panjang(ddkepala):
    hitung = 0
    while ddkepala is not None:
        ddkepala = ddkepala.next
        hitung += 1

    return hitung

def selipkanLL(ddkepala, n):
    if ddkepala == None or ddkepala.next == None:
        return ddkepala
    sekarang = ddkepala
    temp2 = ddkepala
    hitung = 0
    l = panjang(ddkepala)
    while hitung < l - n - 1:
        sekarang = sekarang.next
        hitung += 1
    temp1 = sekarang.next
    ddkepala = temp1
    sekarang.next = None
    while temp1.next != None:
        temp1 = temp1.next
    temp1.next = temp2
    return ddkepala

def ll(arr):
    if len(arr) == 0:
        return None
    ddkepala = Simpul(arr[0])
    ekor = ddkepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return ddkepala

def printll(ddkepala):
    while ddkepala:
        print(ddkepala.data, end=' ')
        ddkepala = ddkepala.next
    print()

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
i = int(input())
l = selipkanLL(l, i)
printll(l)


#Hilangkan duplikasi dari LL
Input 1 :
1
1 2 3 3 4 3 4 5 4 5 5 7 -1
Output 1 :
1 2 3 4 3 4 5 4 5 7

Input 2 :
2
10 20 30 40 50 -1
10 10 10 10 -1
Output 2 :
10 20 30 40 50
10

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def hilangkanDuplikasi(ddkepala):
    temp = ddkepala
    if temp is None:
        return
    while temp.next is not None:
        if temp.data == temp.next.data:
            new = temp.next.next
            temp.next = None
            temp.next = new
        else:
            temp = temp.next
    return ddkepala

def ll(arr):
    if len(arr) == 0:
        return None
    ddkepala = Simpul(arr[0])
    ekor = ddkepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return ddkepala

def printll(ddkepala):
    while ddkepala:
        print(ddkepala.data, end=' ')
        ddkepala = ddkepala.next
    print()

arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = hilangkanDuplikasi(l)
printll(l)


#Print LinkedList terbalik
Input 1 :
1
1 2 3 4 5 -1
Output 1 :
5 4 3 2 1

Input 2 :
2
1 2 3 -1
10 20 30 40 50 -1
Output 2 :
3 2 1
50 40 30 20 10

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(ddkepala):
    def __init__(self):
        ddkepala = None
    sebelumnya = None
    sekarang =ddkepala
    while(sekarang is not None):
        next = sekarang.next
        sekarang.next = sebelumnya
        sebelumnya = sekarang
        sekarang = next
    ddkepala = sebelumnya
    return ddkepala

def ll(arr):
    if len(arr)==0:
        return None
    ddkepala = Simpul(arr[0])
    ekor = ddkepala
    for data in arr[1:]:
        ekor.next = Simpul(data)
        ekor = ekor.next
    return ddkepala
def printll(ddkepala):
    while ddkepala:
        print(ddkepala.data, end=' ')
        ddkepala = ddkepala.next
    print()

from sys import setrecursionlimit as srl
srl(10000)
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
r=reverse(l)
printll(r)


#Palindrom LinkedList
Input 1 :
1
9 2 3 3 2 9 -1
Output 1 :
true

Input 2 :
2
0 2 3 2 5 -1
-1
Output 2 :
false
true

Penjelasan untuk input 2 :
Pada query pertama, list yang diberikan tidak palindrom, makanya outputnya 'false'.
Pada query kedua, listnya kosong, makanya outputnya 'true'.

#################################
class Simpul:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.ddkepala = None
        self.simpulEkor = None

    def selipkan(self, data):
        if self.simpulEkor is None:
            self.ddkepala = Simpul(data)
            self.simpulEkor = self.ddkepala
        else:
            self.simpulEkor.next = Simpul(data)
            self.simpulEkor = self.simpulEkor.next

    def ambilSimpulEkor(self,simpulEkor):
        sekarang = self.ddkepala
        while (sekarang and sekarang.next !=simpulEkor):
            sekarang = sekarang.next
        return sekarang

def cekPalindrom(llist):
    awal = llist.ddkepala
    ujung = llist.simpulEkor
    while (awal != ujung and ujung.next != awal):
        if awal.data != ujung.data:
            return False
        awal = awal.next
        ujung = llist.ambilSimpulEkor(ujung)
    return True

a_llist = LinkedList()

listData = input().split()
for data in listData:
    if int(data) != -1:
        a_llist.selipkan(int(data))

if cekPalindrom(a_llist):
    print('true')
else:
    print('false')

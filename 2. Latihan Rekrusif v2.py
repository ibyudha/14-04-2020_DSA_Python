# Created on 17 April 2020
# by Gus Yudha

#Hapus X
Input 1 :
xaxb
Output 1:
ab

Input 2 :
abc
Output 2:
abc

Input 3 :
xx
Output 3:

#################################
def hapusX(s,x):
    if len(s)==0:
        return s

    sO=hapusX(s[1:],x)

    if s[0]==x:
        return sO

    else:
        return s[0]+sO

s=input()
r=hapusX(s,'x')
print(r)


#Hapus Duplikasi yang rekrusif
Input 1 :
aabccba
Output 1 :
abcba

Input 2 :
xxxyyyzwwzzz
Output 2 :
xyzwz

#################################
def hapusDuplikasi(s):

    if len(s)==0 or len(s)==1:
        return s

    if s[0]==s[1]:
        sO=hapusDuplikasi(s[1:])
        return sO

    else:
        sO=hapusDuplikasi(s[1:])
        return s[0]+sO

s=input()
r=hapusDuplikasi(s)
print(r)


#Merge Sort
Input 1 :
6
2 6 8 5 4 3
Output 1 :
2 3 4 5 6 8

Input 2 :
5
2 1 5 2 3
Output 2 :
1 2 2 3 5

#################################
def mergeSort(arr, awal, akhir):
    ukuran = akhir - awal
    if ukuran <= 1:
        return
    tengah = (awal + akhir) // 2
    mergeSort(arr, awal, tengah)
    mergeSort(arr, tengah, akhir)

    # Merge 2 List yang telah terurut
    hasil = [0] * ukuran
    i = awal
    j = tengah
    k = 0
    while (i < tengah and j < akhir):
        if (arr[i] < arr[j]):
            hasil[k] = arr[i]
            k += 1
            i += 1
        else:
            hasil[k] = arr[j]
            k += 1
            j += 1
    while (i < tengah):
        hasil[k] = arr[i]
        k += 1
        i += 1
    while (j < akhir):
        hasil[k] = arr[j]
        k += 1
        j += 1
    for i in range(0, ukuran):
        arr[awal + i] = hasil[i]


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
for num in arr:
    print(num, end=" ")
print()


#Quick Sort
Input 1 :
6
2 6 8 5 4 3
Output 1 :
2 3 4 5 6 8

Input 2 :
5
1 5 2 7 3
Output 2 :
1 2 3 5 7

#################################
def partisi(a,si,ei):
    pivot=a[si]
    c=0
    for i in range(si,ei+1):
        if a[i] < pivot:
            c=c+1
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index=si+c
    i=si
    j=ei
    while i < j :
        if (a[i]<pivot):
            i=i+1
        elif a[j] >= pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i = i + 1
            j = j - 1
    return pivot_index

def quick_sort(a,si,ei):
    if si>=ei:
        return
    pivot_index=partisi(a,si,ei)
    quick_sort(a,si,pivot_index-1)
    quick_sort(a,pivot_index+1,ei)

n=int(input())
a=list(int(i) for i in input().strip().split(' '))
quick_sort(a,0,len(a)-1)
for x in a:
    print(x,end=" ")


#Tower Hanoi
Input 1 :
2
Output 1 :
a b
a c
b c

Input 2 :
3
Output 2 :
a c
a b
c b
a c
b a
b c
a c

#################################
def tower(n,a,b,c):

    if n==0:
        return

    if n==1:
        print(a,c )
        return

    tower(n-1,a,c,b)

    print(a,c)

    tower(n-1,b,a,c)

n=int(input())
tower(n,"a","b","c")

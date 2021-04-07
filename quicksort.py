def partition(a,p,r):
    x=a[r]
    i=p-1
    j=p
    for k in range(p,r):
        if a[j]<=x:
            i+=1
            #swap
            t=a[i]
            a[i]=a[j]
            a[j]=t
        j+=1
    #swap last element
    t=a[j]
    a[j]=a[i+1]
    a[i+1]=t
    return i+1
def quicksort(a,p,r):
    if(p<r):
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
a=[1,2,3,4,5,6,7,8]
quicksort(a,0,len(a)-1)
print(a)



# li=list(map(int,input().split(",")))
# di={}
# for i in li:
#     di.setdefault(i,0)

# for i in li:
#     di[i]=di[i]+1
# max=0
# for i in di.keys():


li=[5,4,7,14,1,3,7,8] 



# Bubble Sort
# for i in range(len(li)-1,0,-1):
#     for j in range(0,i):
#         if(li[j]>li[j+1]):
#             li[j],li[j+1]=li[j+1],li[j]
# print(li)



# Selection Sort
# for i in range(0,len(li)):
#     min=i
#     for j in range(i+1,len(li)):
#         if(li[j]<li[min]):
#             min=j
#     li[i],li[min]=li[min],li[i]
# print(li)



# Insertion Sort
for i in range(0,len(li)):
    temp=li[i]
    j=i-1
    c=0
    for j in range(j,-1,-1):
        if(temp<li[j]):
            li[j+1]=li[j]
            c=1
        else:
            break
    if(c==1):
        li[j+1]=temp
print(li)




# n1=int(input())
# n2=int(input())
# for i in range(1):
#     temp=li[n1]
#     for j in range(n1,n2+1):
#         li[j]=li[j+1]
#     li[n2]=temp

# print(li)

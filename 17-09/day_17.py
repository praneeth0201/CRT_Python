# l=[5,3,1,6,7,8,4,2,17,3]
k=int(input())
# ans=[]
# for i in range(0,len(l)-(k-1)):
#     sum=0
#     for j in range(i,i+k):
#         sum+=l[j]
#     ans.append(sum)
# print(ans)


# def x(li,i,k):
#     sub=""
#     for j in range(i,i+k):
#         print(li[j],end=" ")
# sum=0
# j=0
# min=l[0]
# max=0
# minI=0
# maxI=0
# for i in range(0,len(l)):
#     j+=1
#     if(j==k):
#         sum+=l[i]
#         ans.append(sum)
#         if(sum<min):
#             min=sum
#             minI=i-(k-1)
#         if(max<sum):
#             max=sum
#             maxI=i-(k-1)
#         sum-=l[i-(k-1)]
#         j-=1
#     else:
#         sum+=l[i]

# print(ans)
# print(f"Max window is {max} with the window number {maxI+1} with the values")
# x(l,maxI,k)
# print(f"min window is {min} with the window number {minI+1} with the values")
# x(l,minI,k)

s="abacddcbkbb"

y=set()
sub=""
for i in range(0,len(s)):
    if(s[i] in sub):
        sub+=s[i]
        sub=sub[1:k]
        print(sub)
        continue
    sub+=s[i]
    if(len(sub)==k):
        y.add(sub)
        print(sub)
        sub=sub[1:k]
        print(sum)
print(y)


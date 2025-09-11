# n=int(input())
# temp=n
# sum=0
# while(temp>=10):
#     sum=sum+temp%100
#     temp//=10
# print(sum)


# n=int(input())
# temp=n
# prod=1
# while(temp!=0):
#     prod=prod*(temp%10)
#     temp//=10
# print(prod)

# write a program to convert any given base to desired base
# constrain: conversion range will be 1-10

def is_valid(n,g,d):
    temp=n
    while(temp!=0):
        if(temp%10>=g):
            return False
        else:
            temp=temp//10
    return True

# n=int(input())
# g=int(input("Enter the given Base: "))
# d=int(input("Enter the desired base"))
# if((g>=1 and g<=10) and (d>=1 and d<=10)):
#     if(is_valid(n,g)):
#         if()
#     else:
#         print("the given number with the base is not valid")
# else:
#     print("The given base or desired base should be between 1-10")


def to_base_ten(n,g):
    temp=n
    x=0
    desired=0
    while(temp!=0):
        desired=desired+temp%10*(g**x)
        x+=1
        temp=temp//10
    return(desired)
def to_ten_desired(n,d):
    



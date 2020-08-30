# a=int(input("enter number:"))
# b=a-1
# for i in range(a):
#     for j in range(a):
#         if(i == j):
#             print("x",i,end=" ")
#         elif (b == j):
#             print("x",b,end=" ")
#             b-=1
#         else:
#             print(" ",end=" ")
#     print("\n")
# #zip and  filter
 
# CTemp_a=[]
# RTemp_a=[]
# cross_a=[]
# Per_a=[]
# a=int(input("enter no.:"))
# Row_temp=1
# cross=a
# for i in range(1,a+1):
#     Col_temp=i                        
#     for j in range(1,a+1):
#         print(Col_temp,end=" ")    
#         CTemp_a.append(Col_temp)    
#         Col_temp+=a     
#     Per_a.append(CTemp_a)
#     for k in range(1,a+1):         
#         print(Row_temp)
#         RTemp_a.append(Row_temp)
#         Row_temp+=1
#     Per_a.append(RTemp_a)
#     for l in range(1,a):
#         if (i == l):
#             print(i)
#             cross_a.append(i)
#         elif(cross == l):
#             print(cross)
#             cross_a.append(cross)
#             cross-=1
#         else:
#             print(" ")
#     RTemp_a=[]
#     CTemp_a=[]
# Per_a.append(cross_a)
# cross_a=[]
# print(CTemp_a)
# print(Per_a)

'''
1 2 3 
4 5 6
7 8 9
'''
# winnig=[]

# horizontalTemp = []
# horizontalStart = 1

# verticalTemp = []

# forwordCrossTemp = []
# forwordstart=1

# backwordCrossTemp = []
# backwordstart = matrix_size
# backtemp=matrix_size

# for i in range(1,matrix_size+1):
#     verticalStart = i
#     for j in range(1,matrix_size+1):
#         horizontalTemp.append(horizontalStart)
#         horizontalStart += 1

#         verticalTemp.append(verticalStart)
#         verticalStart+=matrix_size

#         if (i == j):
#             forwordCrossTemp.append(forwordstart)
#         forwordstart+=1

#         if (backtemp == j):
#             backwordCrossTemp.append(backwordstart)
#     backwordstart+=(matrix_size-1)

#     winnig.append(horizontalTemp)
#     winnig.append(verticalTemp)
#     verticalTemp = []
#     horizontalTemp = []
# backtemp-=1
# winnig.append(forwordCrossTemp)
# winnig.append(backwordCrossTemp)

# print(winnig)
# print(horizontal)
# print(vertical)
# print(forwordCross)
# print(backwordCross)


# l1=[2, 4, 6, 8]
# l2=[1, 3, 5, 7, 9]
# l3=[[1, 2, 3], [1, 4, 7], [4, 5, 6], [2, 5, 8], [7, 8, 9], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
# if l1 in l3:
#     print("win")
# x=l2.count(l3)
# print(x)

# from itertools import permutations 
# import itertools
# l2=[]
# l1 = [1, 3, 5, 7]
# l3=[[1, 2, 3], [1, 4, 7], [4, 5, 6], [2, 5, 8], [7, 8, 9], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
# for L in range(0, len(l1)+1):
#     for subset in itertools.combinations(l1, L):
#         l2.append(subset)
# print(l2)
# x=l2.count(l3)

# def intersection(l1, l3): 
#     lst3 = [list(filter(lambda x: x in l1, sublist)) for sublist in l3] 
#     for i in l3:
#         for j in lst3:
#             if (i == j):
#                 print("win")
#     return lst3

# l3=[[1, 2, 3], [1, 4, 7], [4, 5, 6], [2, 5, 8], [7, 8, 9], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
# l1=[1,3,5,7]  
# print(intersection(l1, l3)) 
# temp=0
# l3=[[1, 2, 3], [1, 4, 7], [4, 5, 6], [2, 5, 8], [7, 8, 9], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
# l1=[1,3,5,7] 
# for i in range(len(l3)):
#     for j in range(len(l3[i])):
#         if l3[i][j] in l1:
#             temp+=1
#         else:
#             print(j)
#             #continue
#     if(temp == 3):
#         print("win")
#         break
#     else:
#         temp=0

for i in range(5):
    for j in range(5):
        print("hello",j)
        if (j==3):
            continue
        print("hi",j)

    

#set(l1).intersection(set(l3))
#a=0
#set(l3) & set(l1)

# for i in l3:
    # if i in l1:
    #     print("yes")
    # print(i)
    # for j in l1:
    #     if j in i:
    #         # a+=1
    #         # print(a)
    #         print("yes")

           # if(a >= 3):
                #print("yes")
            # x=i.count(j)
            # if(x>=3):
            #     print(x)

    # set(i) & set(l3)
    # i_set = set(i)
    # l3_set = set(l3)
    # if (i_set & l3_set):
    #     print("win")
    # else:
    #     print("loss")
    # if i in l1:
    #     print("win")
    # x=i.count(l1)
    # print(x)
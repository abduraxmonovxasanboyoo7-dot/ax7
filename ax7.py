# # # # # #7masala
# # # # # # # # a=int(input("a="))
# # # # # # # # b=int(input("b="))  
# # # # # # # # c=int(input("c=")) 
# # # # # # # # s = c<b<a 
# # # # # # # # print(s) 

# # # # # #8xato
# # # # # # # a=int(input("a="))
# # # # # # # b=int(input("b=")) 
# # # # # # # s = a and b = %2!=0
# # # # # # # print(s)   


# # # # # #8masala
# # # # # # a = int(input("a = "))
# # # # # # b = int(input("b = "))
# # # # # # s = (a % 2 != 0) and (b % 2 != 0)
# # # # # # print(s)


# # # # # #9masala 
# # # # # a=int(input("a="))
# # # # # b=int(input("b="))
# # # # # s = (a % 2 !=0 ) or (b%2 != 0 )
# # # # # print(s)


# # # # #11masla 
# # # # a=int(input("a="))
# # # # b=int(input("b="))
# # # # s = (a % 2!=0 and b % 2 !=0 ) or (a % 2 == 0 and b % 2 ==0 )
# # # # print(s)     


# # # #12masala 
# # # a=int(input("a="))
# # # b=int(input("b=")) 
# # # c=int(input("c=")) 
# # # s = (a>0 and b>0 and c>0 )
# # # print(s) 

# # #13masala 
# # a=int(input("a="))
# # b=int(input("b=")) 
# # c=int(input("c=")) 
# # s = (a>0 or b>0 or c>0 )
# # print(s) 

# #14masala 
# a=int(input("a="))
# b=int(input("b=")) 
# c=int(input("c=")) 
# s = (a>0) ^ (b>0) ^ (c>0) and not (a>0 and b>0 and c>0)
# print(s)   
 

#15masala x
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s=(a>0 or a<0 and b>0 or b<0 and c>0 or c<0 )
# print(s)

# #15masala !
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s = (a > 0 and b > 0 and c <= 0) or \
#     (a > 0 and c > 0 and b <= 0) or \
#     (b > 0 and c > 0 and a <= 0)
# print(s)


#16masala
# a=int(input("a="))
# s=(a >= 10 and a <= 99) and a%2==0
# print(s) 

#17masala
# a=int(input("a="))
# s=(a>=100 and a<=999) and a%2==0
# print(s)

#18masala
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s=( a==b or a==c) or (b==a or b==c) or (c==a or c==b)
# print(s) 

#19masala 
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s=a==-b or a==-c or b==-c 
# print(s) 

#20masala x
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s=a//100 and (b//10)%10 and c%10
# print(s)

#20masala
# a = int(input("Uch xonali son = "))

# x = a // 100
# y = (a // 10) % 10
# z = a % 10

# s = (x != y) and (x != z) and (y != z)
# print(s) 


#21masala 
# son = int(input("Uch xonali son = "))

# y = son // 100          # yuzlik
# o = (son // 10) % 10    # o'nlik
# b = son % 10            # birlik

# result = (y < o) and (o < b)
# print(result)    
  

#22masala 
# son = int(input("Uch xonali son = "))

# y = son // 100          # yuzlik
# o = (son // 10) % 10    # o'nlik
# b = son % 10            # birlik

# osuvchi = (y < o) and (o < b)
# kamayuvchi = (y > o) and (o > b)

# result = osuvchi or kamayuvchi
# print(result) 

#23masala 
# a=int(input("a="))
# y = a // 100
# o = (a//10)% 10
# b = a%10
# s=  y==b
# print(s)

#24masala 
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))

# if a == 0:
#     print("A noldan farqli bo'lishi kerak")
# else:
#     D = b*b - 4*a*c
#     result = D >= 0
#     print(result)

#25masala 
# x=int(input("x="))
# y=int(input("y="))
# s=(x<0)and (y>0)
# print(s) 

#26masala
# x=int(input("x="))
# y=int(input("y="))
# s=(x>0) and (y<0)
# print(s)

#27masala
# x=int(input("x="))
# y=int(input("y="))
# s=((x>0) and (y>0)) or((x>0) and (y<0))
# print(s) 
#28masala
# x=int(input("x="))
# y=int(input("y="))
# s=((x>0)and (y>0)) or ((x<0) and (y<0))
# print(s)

#30masala 
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s= a==b and a==c and b==c 
# print(s) 

#31massala 
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s = (a==b!=c) or (a==c!=b) or (b==c!=a)
# print(s) 

# #32masala 
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s=(a*a+b*b==c*c) or (a*a+c*c==b*b) or (b*b+c*c==a*a) 
# print(s)

#33masala 
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s= (a+b>c) and (a+c>b) and (b+c>a)
# print(s)   

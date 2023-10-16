#while 21
# s = 0
# n =int(input('vvedite chislo >0:'))
# if n<=0:
#     print('ti osel?')
# else:
#     while n!=0:
#         s = n%10
#         n=n//10
#     if s % 2!=0:
#         print (True)
#     else:
#         print(False)



#series 8
# n = int(input('vvedite kolichestvo chisel:'))
# numbers = []
# numberchet = []
# for i in range(1,n+1):
#     numbers.append(i)
#     if i%2==0:
#         numberchet.append(i)
# print('vse chisla:',numbers)
# print('chetnie:',numberchet,'kol-vo:',len(numberchet))

#ЗАДАЧА 3
# import random
# tries = 0
# orel = 0
# reshka = 0
#
# while tries < 20:
#     coin = random.randint(0, 1)
#     tries += 1
#     if coin > 0:
#         orel +=1
#         print('orel')
#     elif coin < 1:
#         reshka += 1
#         print('reshka')
# print(f"Монета подброшена {tries} раз")
# print(f"Орел {orel}")
# print(f"Решка {reshka}")






#theTwo15
# s = 0
# n = int(input('vvedite chislo 12 i menshe:'))
# if n<=12 and n>0:
#     while n!=0:
#         s +=n**n/(n*(n+1))
#         n=n-1
#     print(s)
# else:
#     print('ti osel?')


#theTwo21
# n = int(input('vvedite chislo ne bolee 8-mi znachaschix cifr:'))
# s = []
# c = 0
# if n<=0:
#     print('ti osel?')
# else:
#     while n!=0:
#         s.append(n%10)
#         n//=10
#     for i in range(len(s)-1):
#         if s[i]<s[i+1]:
#             c +=1
#     # if s[0]<s[1]<s[2]<s[3]<s[4]<s[5]<s[6]<s[7]:
#     #     print('vozrast')
# if c == (len(s)-1):
#     print('vozrast')
# else:
#     print('net')



#6
# n = int(input('vvedite celoe chislo:'))
# x = float(input('vvedite veschestvennoe chislo:'))
# su = 1
# if abs(x)<1:
#     for i in range(1,n+1):
#         su += x**i
#     print(su)
# else:
#     print('vvedite drugoi x:')
# fx = 1/1-x
# print(fx)

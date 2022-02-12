#Question 1#

print("Question 1\n")

Val = input("Please give an input- ")
Val=Val.lower().strip()
i=0

dict={}
if " " not in Val:
     while i<len(Val):
          use=0
          k=0
          while k<len(Val):
               if Val[i]==Val[k]:
                    use=use+1
                    k=k+1
               else:
                    k=k+1
          
          dict[f"{Val[i]}"]=use
          i=i+1
else:
     
     list = str.split(Val)
     
     while i<len(list):
          use=0
          k=0
          while k<len(list):
               if list[i]==list[k]:
                    use=use+1
                    k=k+1
               else:
                    k=k+1
                    dict[f"{list[i]}"]=use
          i=i+1
print("Total occurances")
for key,value in dict.items():
    print(f"{key}-{value}\n")

#Question 2#
print("Question 2\n")

def is_leap_year(year:int) -> bool:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("year - "))
    if (date< 1) or (date> 31) or (month< 1) or (month> 12) or (year < 1800) or (year > 2025):
       print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
       continue
    if month in (4,6,9,11) and date == 31:
        print("The given month has only 30 days\nPlease enter a valid date\n")
        continue
    elif month == 2 and date>= 29:
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date\n")
            continue
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date\n")
            continue
    break
if month == 2:
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if date == max_days:
    date = 1
    if month == 12:
       month = 1
       year += 1
    else:
        month += 1
else:
    date += 1
print("Next Date is:%d/%d/%d,\n" %(date,month,year))


#Question 3#
print("Question 3\n")

incoming = eval(input("Enter the list: "))
outgoing= []
for i in incoming:
    outgoing.append((i,i**2))
print("Output:\n",outgoing)


#Question 4#
print("Question 4 \n")

given_table = [ ["A+","Outstanding",10],
                ["A","Excellent",9],
                ["B+","Very Good",8],
                ["B","Good",7],
                ["C+","Average",6],
                ["C","Below Average",5],
                ["D","Poor",4] ]
while True:                                                                                                         #loop for making sure the user inputs the value between 4 and 10
    grade_point = eval(input("Enter the grade point of the student: "))
    if 4 <= grade_point <= 10:
        break
    else:
        print("The grade point must be between 4 and 10")
for i in given_table:                                                                                               #i is for iterating through the lists in the list and j is for iterating through the elements of each list
    for j in i:
        if j == int(grade_point):
            print("Your Grade is '%s' and %s Performance \n" % (i[0],i[1]))


#Question 5#
print("Question 5\n")

given_string = "ABCDEFGHIJK"
f = 0
while len(given_string) - f*2 >= 1:
    print(" "*f + given_string[0 : len(given_string) - f*2])
    f += 1


#Question 6#

print("Question 6\n")

dict1 = {}
while True:                                                                                                         #Loop for inputting values
    name = input("Enter the name of the student: ")
    SID = int(input("Enter the SID of %s: " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    while True:
        more_data = input("Do you want to enter more data? ")
        if more_data in ("N","n","No","no","NO"):
            more_data = 0
            break
        elif more_data in ("Y","y","Yes","yes","YES"):
            more_data = 1
            break
        else:
            print("\nPlease say yes or no")
            continue
    if more_data == 0:
        break
print("\na. Student Details:")                                                                                      #Q6(a)
for i in dict1:
    print("The SID of %s is %d" % (dict1[i],i))
dict2 = {}
for sorted_value in sorted(dict1.values()):                                                                         #Sorting the dictionary using student names
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details (sorted with respect to names):")                                                       #Q6(b)
for i in dict2:
    print("The SID of %s is %d" % (dict2[i],i))
dict3 = {}
for sorted_key in sorted(dict1):                                                                                    #Sorting the dictionary using SIDs
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details (sorted with respect to SIDs):")                                                        #Q6(c)
for i in dict3:
    print("The SID of %s is %d" % (dict3[i],i))
print("\nd. ", end="")                                                                                              #Q6(d)
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print("The name of student whose SID is %d is %s" % (search_SID,dict1[search_SID]))
        break
    else:
        print("The SID you entered isn't entered\nPlease enter a valid SID to be searched\nList of valid SIDs: %s\n" % list((dict1.keys())))
        continue


#Question 7#

print("Question 7\n")

a = 0
b = 1
sum = 0
while True:                                                                                                         #While loop is just for asking the user to input the value again if user enters a -ve value
    num = int(input("Enter the no. of terms of the Fibonacci sequence: "))
    if num < 0:
        print("Number of terms must be non-negative\nPlease enter again\n")
        continue
    if num == 0:
        print("As the number of terms = 0, the average of all terms = 0")
        break
    else:
        print("The Fibonacci sequence is as follows:")
        print(a,end=" ")
        for i in range(1,num):
            sum += b
            print(b, end=" ")
            c = a + b
            a = b
            b = c
        print("The average of the terms of Fibonacci sequence upto %d terms is %0.2f\n" % (num,sum/num))
        break

#Question 8#
print("Question 8\n")

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print("a. Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)
print("b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)
print("d. Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)
print("e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)            

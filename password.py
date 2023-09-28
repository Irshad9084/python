##def validate(password):
##    requirements = {"letter", "uppercase", "number", "symbol"}
##    found = set()
##
##    min_length = 8
##
##    if len(password) < min_length:
##        print("Insufficient length")
##        return False
##
##    for char in password:
##        # Checking for lowercase and uppercase letters
##        if char.isalpha():
##            if char.islower():
##                found.add("letter")
##            elif char.isupper():
##                found.add("uppercase")
##        # Check for numbers 0-9
##        elif char.isdigit():
##            found.add("number")
##        # Check for symbol (not alphanumeric)
##        elif not char.isalnum():
##            found.add("symbol")
##        else:
##            print("User may have used a non-ASCII character!")
##            return False
##
##    # Check the requirements
##    missing = requirements - found
##    for req in missing:
##        if req == "letter":
##            print("Missing a lowercase letter in the password!")
##        elif req == "uppercase":
##            print("Missing an uppercase letter in the password!")
##        elif req == "number":
##            print("No number in the password!")
##        elif req == "symbol":
##            print("No symbol in the password!")
##        return False
##
##    print("Password is good. Carry on.")
##    return True
##
### Test the function
##validate("Asqwqs2@")
##
##
##
##
##
##
##
##def validate(password):
##    if len(password) < 8:
##        return "Insufficient length"
##
##    has_lower = any(char.islower() for char in password)
##    has_upper = any(char.isupper() for char in password)
##    has_digit = any(char.isdigit() for char in password)
##    has_symbol = any(not char.isalnum() for char in password)
##
##    if not has_lower:
##        return "Missing a lowercase letter in the password!"
##    if not has_upper:
##        return "Missing an uppercase letter in the password!"
##    if not has_digit:
##        return "No number in the password!"
##    if not has_symbol:
##        return "No symbol in the password!"
##
##    return "Password is good. Carry on."
##
##
##password = input("Enter your password: ")
##print(validate(password))



##
##
##
##
##
##def validate(password):
##a_set = set()
##min_length = 8
##if len(password) < min_length:
##print("Insufficient length")
##return False
##for char in password:
### Checking alphabet: a-z A-Z is in password characters
##if(ord(char)>64 and ord(char)<91):
##a_set.add("big")
##if char.isalpha() == True:
##a_set.add("letter")
##continue
### Check for numbers 0-9
##elif char.isdigit() == True:
##a_set.add("number")
##continue
### Check for symbol (not alphanumeric)
##elif char.isalnum() == False:
##a_set.add("symbol")
##continue
##else:
##print("User may use a non ASCII keyboard!")
##return False
##
### Check if all: letter, number and symbol in the set
##if "letter" not in a_set:
##print("No letter in password!")
##return False
##elif "number" not in a_set:
##print("No number in password!")
##return False
##elif "symbol" not in a_set:
##print("No symbol in password!")
##return False
##elif "big" not in a_set:
##print("No big char in password!")
##return False
##else:
##print("Password is good. Carry on.")
##return True
##validate("qwqs2@")
##






##write a python program to count the number of string from a given list from a given
##list of strings.the string length is 2 or more and the first and last characters are
##the same
##Sample List: ['abc','xyz','abc'.'1221']
##expected result :2




##
##
##
##
##def count_matching_strings(strings):
##    count = 0
##    for s in strings:
##        if len(s) >= 2 and s[0] == s[-1]:
##            count += 1
##    return count
##
##sample_list = ['abc', 'xyz', 'abc', '1221']
##print(count_matching_strings(sample_list))






##Sample List : [(2,5),(1,2),(4,4),(2,3),(2,1)]
##Expected Output : [(2,1),(1,2),(2,3),(4,4),(2,5)]


##
##def Lst(item):
##    return item[1]
##
##sample_list = [(2,5),(1,2),(4,4),(2,3),(2,1)]
##
##sorted_list = sorted(sample_list, key=Lst)
##
##print(sorted_list)








##removing duplicate in list

A = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
Lst = []



##for item in A:
##    if item not in Lst:
##        Lst.append(item)
##print(Lst)


##for item in A:
##    if item in Lst:
##        pass
##    else:
##        Lst.append(item)
##print(Lst)




##
##string are anagram  or not

##
##print("Enter the First String:")
##s1= str(input())
##print("Enter the Second String:")
##s2 = str(input())
##found=0
##notFound=0
##lenOne = len(s1)
##lenTwo = len(s2)
##if lenOne == lenTwo:
##    for i in range(lenOne):
##        found = 0
##        for j in range(lenOne):
##            if s1[i] == s2[j]:
##                found = 1
##                break
##        if found==0:
##            notFound = 1
##            break
##    if notFound==1:
##        print("\nStrings are Not Anagram")
##    else:
##        print("\nStrings are Anagram")
##else:
##    print("\nLength of Strings are not Equal")
##


##
##String1 = input("Enter the string to be checked: ")
##n = len(String1)
##
##half = String1[:n//2]
##m = 0
##for i in range(n-1,n//2,-1):
##    if String1[i] == half[m]:
##        m = m+1
##    else:
##        print("The string is not palindrome")
##        break
##if m == len(half):
##    print("The string is a palindrome")




##create a tuple
tuplex = ("ram","rom","rom","ram" ,"pom","tom")
print(tuplex)
count = tuplex.count("ram")
print(count)





























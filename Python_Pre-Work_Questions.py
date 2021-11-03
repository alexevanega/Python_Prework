# ## Question 1:
# # Write a function to print "hello_USERNAME!"
# #  USERNAME is the input of the function.
 
def hello_username(user_name):
    """prints a simple greeting to the user"""
    print("hello_" + user_name + "!")

hello_username('USERNAME')
# prints Hello USERNAME!

## Question 2:
#  Write a function, first_odds, that prints the odd numbers
#  from 1-100 and returns nothing
 
def first_odds():
    """prints odd numbers from 1 to 100"""
    odd_nums = list(range(1,101,2))
    for n in odd_nums:
        print(n)

first_odds()
# will print odd numbers from 1 to 100
# alternative answer:
# def first_odds():
    # """prints odd numbers from 1 to+9 100"""
    # hundred = list(range(1,101))
    # for n in hundred:
    #     if n%2 == 0:
    #         continue
    #     else:
    #         print(n)    

# ## Question 3:
# # Please write a function 'max_num_in_list 
# # to return the max number of a given list.

def max_num_in_list(a_list):
    """prints out the max number in a given list"""
    print(max(a_list))

practice_list = [1, 6, 8, 9, 75, 0, 12, 19]

max_num_in_list(practice_list)
# will print 75

## Question 4:
# Write a function to return if the give year is a leap year.
# A leap year is divisible by 4 but not by 100, unless it is also divisible by 400.
# The return should be a boolean.

def is_leap_year(a_year):
    """Will tell whether a year is a leap year or not"""
    if a_year%4 == 0 and a_year%100 != 0:
        return True
    elif a_year%400 == 0 and a_year%100 == 0:
        return True
    else:
        return False

print(is_leap_year(2000))
# will return True
print(is_leap_year(1954))
# will return false
    
        
## Question 5:
# Write a function to check to see if all the numbers in a list
# are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive
# numbers, but [1,2,4,5] are not consecutive numbers. Return should be 
# a boolean type.
 
def in_consecutive(a_list):
    """Will tell if numbers in a list are consecutive"""
    n_list = list(range(min(a_list), max(a_list) + 1))
    if a_list == n_list:
        return True
    else:
        return False
    

test_1 = [2,3,4,5,6,7]
test_2 = [1,2,4,5]
test_3 = [1,2,3,4,4,5,6]

print(in_consecutive(test_1))
# will return True
print(in_consecutive(test_2))
# will return False
print(in_consecutive(test_3))
# will return false

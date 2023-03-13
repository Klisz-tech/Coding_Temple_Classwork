#Question 1:
#def hello_name(user_name):
#    print(f"Alrighty {user_name}! Ready for the journey that awaits? ")

#name = input("Hello, what is your username? ")
#hello_name(name)

#Question 2:
#def first_odds(num):
#    for num in range(1,101):
#        if num % 2 == 0:
#            continue
#            print("Nope, that is an even number" )
#        else:
#            print(f"Here is {num}")


#number_int = list(range(1,101))            
#first_odds(number_int)

#Question 3:
#def max_num_in_list(a_list):

#    maximal_val = a_list[0]
#    for num in a_list:
#        if (num > maximal_val):
#            maximal_val = num
#        return maximal_val


#print(max_num_in_list([1,20,202,101,56,73,19]))

#Question 4:
#year_check = int(input("What year: "))
#def is_leap_year(year_check):
#    if (year_check % 4 == 0 and year_check % 100 != 0) or year_check % 400 == 0:
#        return True
#    else:
#        return False
#if is_leap_year(year_check):
#      print("That is a leap year.")
#else:
#      print("Not a leap year.")


#Question 5
def is_consecutive(ab_list):
    b_list = ab_list[:]
    b_list.sort
    for i in range(1, len(b_list)):
        if b_list[i] != b_list[i-1]+1:
            return False
        return True
    
print(is_consecutive([1,2,3,4,5,2,8]))
        




            


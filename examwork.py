### 1 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.
# datetime.now().
# datetime.timedelta().
# random.randint(a, b).
# random.choice()



### 2 Question
# Кадом методхо ва функсияхоро барои кор бо файл медонед.
# open().
# read().
# readline().
# write().


### 3 Question
# Github чист? Командахои GitHub-ро фахмонед.
# GitHub як платформаи  барои идоракунии версияҳои код мебошад. Он як система барои тагирот дар файлҳо мебошад. GitHub ба шумо
# ёрдам медихад коди худ идора кунед.
# git init.
# git add.
# git commit.




# task 1



# my_list = [10, 20, 30, 40, 50]

# element = 25
# position = 2

# my_list.insert(position, element)

# print(my_list)









# task 2



# import datetime


# today = datetime.date.today()


# two_days_before = today - datetime.timedelta(days=2)
# two_days_after = today + datetime.timedelta(days=2)


# print(two_days_before)
# print(today)
# print(two_days_after)








# task 3



# import datetime


# today = datetime.date.today()


# five = today - datetime.timedelta(days=5)


# print(five)









# task 4



# def sum_vowels(s):
    
#     vowels = {'A': 4, 'E': 3, 'I': 1, 'O': 0, 'U': 0}
    
#     sum = 0
    
#     s = s.upper()
    
#     for i in s:
        
#         if i in vowels:
#             sum += vowels[i]
    
#     return sum

# res = sum_vowels("Do I get the correct output?")
# print(res)  



# task 5




# def line_n(a, n):
#     with open(a, "r") as file:
     
#         lines = file.readlines()
#         if 0 < n <= len(lines):
#             print(lines[n-1].strip())
#         else:
#             print("EROR")


# number = int(input())

# print(line_n("my_file.txt", number))




# task 8

# N = int(input())

# dict = {i: i**2 for i in range(1, N + 1)}

# print(dict)



# task 9



# def char_appears(s, a):
#     s = s.lower()
#     a = a.lower()
    
#     words = s.split()
    
#     res = [word.count(a) for word in words]
    
#     return res

# s = "She sells sea shells by the seashore."
# a = "s"
# print(char_appears(s, a))

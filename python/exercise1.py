#############################
#### FUNCTION EXERCISES #####
#############################

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# ใช้ indexing เพื่อ print out ให้ได้ผลดังต่อไปนี้:
# 'd'
# print(s[0])

# 'o'
# print(s[-1])

# 'djan'
# print(s[:4])

# 'jan'
# print(s[1:5])

# 'go'
# print(s[5:])

# Bonus: ลองใช้ index จากท้าย
# print(s[:-1:-1])


###############
## Problem 2 ##
###############

# Given this nested list:
l = [3, 7, [1, 4, 'hello']]
# จงแก้ค่า hello เป็น goodbye
l[2][2] = "Goodbye"


###############
## Problem 3 ##
###############

# จง print out ค่า hello ออกมาจาก dicitionry ด้านล่าง:

d1 = {'simple_key': 'hello'}

# print(d1['simple_key']+" d1 ")

d2 = {'k1': {'k2': 'hello'}}
# print(d2['k1']['k2']+" d2")

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
# print(d3['k1'][0]['nest_key'][1][0]+" d3")

#####################
## -- PROBLEM 4 -- ##
#####################

# เขียนฟังก์ชั่นที่รับ list ของเลข integer โดยจะ return True ถ้ามี list ของเลข 1, 2, 3 อยู่ใน list ที่รับเข้ามา

# For example:

# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True


def arrayCheck(nums): 
  nums = ''.join(str(x) for x in nums)
  # # print('true') if '123' in nums else print('false')

arrayCheck([1, 1, 2, 3, 1])
arrayCheck([1, 1, 2, 4, 1])
arrayCheck([1, 1, 2, 1, 2, 3])
arrayCheck([1, 0, 2, 0, 3])


#####################
## -- PROBLEM 5 -- ##
#####################

# เขียนฟังก์ชั่นที่รับ string เข้ามา แล้ว return string ที่แสดงตัวอักษร ตัว-เว้น-ตัว จาก string ที่รับเข้ามา

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

# def stringBits(str):
#   for i in range (len(str)):
#     if i%2==0:
#       print(str[i],end="")
#   print()
# stringBits('Hello')
# stringBits('Hi')
# stringBits('Heeololeo')

#####################
## -- PROBLEM 6 -- ##
#####################

# จง return จำนวนเลขบวกใน list ที่ส่งเข้ามาในฟังก์ชั่น
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0


def count_evens(*nums):
  num = 0
  for i in nums[0]:
    if i%2 == 0: num += 1
  # print(num)
count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5])
# CODE GOES HERE

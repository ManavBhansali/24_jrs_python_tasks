# Q.1)

# x = input()
# count = 0
# # .isalpha only if the string contains only alphabets
# # if there is a mixture of string and numbers use for loop.
# if x.isalpha():
#   print("Please enter an integer")
# else:
#   for i in x:
#     count += 1
# print(count)



# Q.2)

# x=input()
# fact=1
# if x.isalpha():
#   print("Please enter an integer")
# else:
#   x=int(x)
#   for i in range (1,x+1):
#     fact=fact*i
#   print(fact)



# Q.3)

# Computers ={
#   "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
#   "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
#   "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
# }

# brand=[]
# OS=[]
# for i in Computers:
#   brand.append(Computers[i]['brand'])
#   OS.append(Computers[i]['OS'])
# print(brand)
# print(OS)



#Leetcode problem

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         l=[]
#         for i in range(len(nums)):
#             other= target-nums[i]
#             if other in nums and nums.index(other)!=i:
#                 l.append(i)
#                 l.append(nums.index(other))
#                 return l





# Leetcode problem

# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         candidate = None

#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)

#         return candidate





# Leetcode Problem

# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         for i in ransomNote:
#             if(i in magazine):
#                 magazine = magazine.replace(i,'',1)
#             else:
#                 return False
#         return True





# Leetcode Problem

# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         char_count = {}
#         for char in s:
#             if char in char_count:
#                 char_count[char] += 1
#             else:
#                 char_count[char] = 1
#     
#         for index, char in enumerate(s):
#             if char_count[char] == 1:
#                 return index
#         return -1

# def longestPalindrome(self, s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     longest = ""
#     maxLength = 1
#     start = 0
#     low = 0
#     high = 0
#     string = s
#     length = len(s)
#     for i in range(1, length):
#         low = i - 1
#         high = i
#         while low >= 0 and high < length and string[low] == string[high]:
#             low -= 1
#             high += 1
#
#         low += 1
#         high -= 1
#         if string[low] == string[high] and high - low + 1 > maxLength:
#             start = low
#             maxLength = high - low + 1
#
#         low = i - 1
#         high = i + 1
#         while low >= 0 and high < length and string[low] == string[high]:
#             low -= 1
#             high += 1
#         low += 1
#         high -= 1
#         if string[low] == string[high] and high - low + 1 > maxLength:
#             start = low
#             maxLength = high - low + 1
#
#     return string[start:start + maxLength]
# longestPalindrome("fffffafffff")


def maxArea(height) -> int:
    height.sort()
    left=0
    right=len(height)-1
    width=right-left+1
    ans=0
    while (left<right):
        if width * min(height[left],height[right])>ans:
            ans =width*min(height[left],height[right])
            right-=1
            width-=1
        else:
            left+=1
            width-=1
    return ans

    # ans = 0
    # for i in range(len(height)-1):
    #     width = 1
    #     for j in range(i+1,len(height)):
    #         if width * min(height[j],height[i]) > ans:
    #             ans = width * min(height[j], height[i])
    #         width += 1
    #
    # return ans

# a=10
# b=38
#
# print(["*"]*5)
# a=[1,2,3,4,5,6,7]
# lg=list(range(len(a)))
# print(lg)
# a=[0,1,0,1,0,1,0,1,0,1,0]
# i=0
# for k in a:
#     if k==0:
#         i+=1
#     else:
#         break
# j=a[i:]
# for i in a:
#     if i==0:
#         a.pop()
#     else:
#         break
# print(j)


# # def left_area(li):
# #     if not li:
# #         return 0
# #     sec_val = max(li)
# #     sec_index = li.index(sec_val)
# #
# #     cur_area = sec_val * (len(li)-sec_index) - sum(li[sec_index:])
# #     print(cur_area)
# #     return left_area(li[0:sec_index]) + cur_area
# #
# # def right_area(li):
# #     if not li:
# #         return 0
# #     sec_val = max(li)
# #     sec_index = li.index(sec_val)
# #
# #     cur_area = sec_val * (sec_index+1) - sum(li[0:sec_index+1])
# #     print(cur_area)
# #     return right_area(li[sec_index+1:]) + cur_area
# #
# #
# #
# # class Solution:
# #     def trap(self, height) -> int:
# #         if not height:
# #             return 0
# #
# #         max_val = max(height)
# #         max_index = height.index(max_val)
# #
# #         return left_area(height[0:max_index]) + right_area(height[max_index+1:])
# # s =Solution()
# # ret = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
# # print(ret)
#
#
# class Solution:
#     def compressString(self, S: str) -> str:
#         len1 = len(S)
#         ret = ""
#         prev = ""
#         count = 0
#         index = 0
#         for i in S:
#             cur = i
#
#             if cur == prev:
#                 count += 1
#             else:
#                 if index != 0:
#                     ret += str(count)
#                 ret += i
#                 count = 1
#             prev = cur
#             index += 1
#         ret += str(count)
#         print(ret)
#         len2 = len(ret)
#         return ret if len1 > len2 else S
# s = Solution()
# ret = s.compressString('aabcccccaaa')
# print(ret)

# l = ["","",12,""]
# for "" in l:

# Solution of LeetCode Problems 0-19
Creator: Renjun Hu
Date: 2015/9/20


2015/9/20 0TwoSum

问题：给定一个数组的整数以及一个目标数。在数组中找两个数使得这两个数的和为给定的目标数。
题目保证解唯一，即有且仅有两个数满足要求。

思路：两次穷举下标肯定是可以的，复杂度是O(n^2)。本题可以借助hashmap来优化，这样只要穷举一次，
然后利用hash快速判断另一个数是否存在(实现中用的是map，底层是基于红黑数，一次查询的复杂度是O(lg n))。
这里注意数组中出现两个相同数，特别是两个相同的数的和恰为目标数的情况，需要特殊处理。


2015/9/20 1AddTwoNumbers

问题：输入两个非负整数，用链表存，个位在前。求这两个整数的和，用相同格式存。

思路：单纯的链表操作。


2015/9/21 2LongestSubstring

问题：Given a string, find the length of the longest substring without repeating characters.

思路：对于字符串s，设置两个index i and j，表示s[i]到s[j]没有出现出现重复的字符。初始化i=0以及j=-1。[P] 
考虑s[j+1]，如果s[j+1]没有在s[i]-s[j]中出现，则j右移+1，表示当前s[i]与s[j]仍满足要求；否则保持j不变，i右移+1。
如果j没有到最后，则回到[P]处。否则结束。
在这个过程中，随时用当前长度更新最优的长度，以及别忘了最后的更新。
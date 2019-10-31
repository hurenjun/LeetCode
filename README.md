# Solution of LeetCode Problems
Creator: Renjun Hu

**4. Median of Two Sorted Arrays**
(a) binary-search the # of [numbers <= median] in the shorter array; 
(b) the # of [numbers <= median] in the other array can be determined in O(1) time;
(c) check whether the current split is valid.

**5. Longest Palindromic Substring**
* O(N^2) algorithm: fix the middle position and expand both sides;
* O(N) Manacher's Algorithm: maintain the palindromic substring expanding to the right-most position (with id, mx), reuse the palindromic substring if i <= mx;

**11. Container With Most Water**
* O(N^2) brute force algorithm  
* O(N) better algorithm that always moves the short line. This can effectively reduce the N^2 search space.

**16. 3Sum Closest**
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target
* O(N^2) algorithm, decrease the search space effectively
	S0: sort nums 
	S1: enumerate i in (0, len(nums)), j = i + 1, k = len(nums)
	S2: move j = j+1 of sum < target, or move k = k-1 of sum > target, or return sum=target
	
**18. 4Sum (exactly match target)**
* O(N^2) algorithm, split 4 numbers into 2+2 combinations

**19. Remove Nth Node From End of List**
Requirement: one-pass scanning
* O(N) algorithm: two pointer x & y, x starts to move after n steps

**25. Reverse Nodes in k-Group**
Requirement: Only constant extra memory is allowed.
* O(N) algorithm: go forward k steps and manipulate reverse on the original linkedList

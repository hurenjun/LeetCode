# Main ideas of solutions

**Contact info.: hurenjun[at]buaa.edu.cn[end]**

---

**4. Median of Two Sorted Arrays**  
S1: binary-search the # of [numbers <= median] in the shorter array;  
S2: the # of [numbers <= median] in the other array can be determined in O(1) time;  
S3: check whether the current split is valid.  

**5. Longest Palindromic Substring**  
(a) O(N^2) algorithm: fix the middle position and expand both sides;  
(b) O(N) Manacher's Algorithm: maintain the palindromic substring expanding to the right-most position (with id, mx), reuse the palindromic substring if i <= mx;  

**11. Container With Most Water**  
(a) O(N^2) brute force algorithm  
(b) O(N) better algorithm that always moves the short line. This can effectively reduce the N^2 search space.  

**16. 3Sum Closest**Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target  
(a) O(N^2) algorithm, decrease the search space effectively  
	S0: sort nums  
	S1: enumerate i in (0, len(nums)), j = i + 1, k = len(nums)  
	S2: move j = j+1 of sum < target, or move k = k-1 of sum > target, or return sum=target  
	
**18. 4Sum (exactly match target)**  
(a) O(N^2) algorithm, split 4 numbers into 2+2 combinations

**19. Remove Nth Node From End of List** (Requirement: one-pass scanning)  
(a) O(N) algorithm: two pointer x & y, x starts to move after n steps

**25. Reverse Nodes in k-Group** (Only constant extra memory is allowed.)  
(a) O(N) algorithm: go forward k steps and manipulate reverse on the original linkedList



On October 31, 2019 

---

**29. Divide Two Integers** (divide two integers without using multiplication, division and mod operator.)  
(a) mimic how we divide two integers in primary school.  

**30. Substring with Concatenation of All Words**  
S1: maintain a sketch as the frequency of chars in the current substring and check the substring if the sketch matches with the one of the list;  
S2: slice, sort, and compare one word by one word when checking.  

On November 7, 2019

---

**32. Longest Valid Parentheses**  
(a) O(n) DP algorithm: maintain the longest valid parentheses.   
(a) O(n) stack algorithm:  
	S0: initialize the stack with starter -1;  
	S1: push index for '(' and pop+validate for ')';  
	S2: if pop fails, reset the starter in stack with the current index.   

On November 8, 2019  

---

**41. First Missing Positive** (Your algorithm should run in O(n) time and uses constant extra space.)  
(a) Revised bin count algorithm:  
	S1: scan the array of numbers and set numbers outsite [1, n] to zero (n is the length of array);  
	S2: re-scan the array. For some number k with k % (n+1) > 0, plus the corresponding bin (re-use the array) with number (n + 1);  
	S3: re-scan the array and find the first number which is < n + 1.  

**42. Trapping Rain Water**  
(a) O(n) time and O(1) space algorithm: maintain left_max and right_max heights; move left pointer to right and right pointer to right; update #water accordingly.   

On November 11, 2019

---

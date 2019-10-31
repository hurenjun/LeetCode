#include <iostream>
#include <string>

using namespace std;

int lengthOfLongestSubstring(string s) {
	int result = 0;
	bool charOcc[256];
	std::fill(charOcc, charOcc + 256, false);
	int len = 0;
	int i = 0, j = 0;
	while (j < s.length()) {
		if (!charOcc[s[j]]) {
			charOcc[s[j]] = true;
			j++;
			len++;
		}
		else {
			if (len > result) result = len;
			charOcc[s[i]] = false;
			i++;
			len--;
		}
	}
	if (len > result) result = len;
	return result;
}

int main() {
	string s = "aab";
	cout << lengthOfLongestSubstring(s) << endl;
}

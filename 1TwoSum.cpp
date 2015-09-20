#include <iostream>
#include <map>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
	map<int, int> val2ind;
	vector<int> result;
	for (int i = 0; i < nums.size(); i++) {
		if (val2ind.find(nums[i]) != val2ind.end() && nums[i] * 2 == target) {
			result.push_back(val2ind.find(nums[i])->second);
			result.push_back(i + 1);
			return result;
		}
		val2ind.insert(pair<int, int>(nums[i], i + 1));
	}
	for (int i = 0; i < nums.size(); i++) {
		if (nums[i] * 2 != target && val2ind.find(target - nums[i]) != val2ind.end()) {
			result.push_back(i + 1);
			result.push_back(val2ind.find(target - nums[i])->second);
			break;
		}
	}
	return result;
}

int main() {
	vector<int> nums;
	nums.push_back(3);
	nums.push_back(2);
	nums.push_back(4);
	vector<int> result = twoSum(nums, 6);
	cout << result[0] << " " << result[1] << endl;
}
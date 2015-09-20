#include <iostream>
#include <map>
#include <vector>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
	ListNode* p = l1;
	ListNode* q = l2;
	ListNode * sum = NULL;
	ListNode * sumTail = NULL;
	int rest = 0;
	while (p != NULL || q != NULL) {
		int sumOfDigit = rest;
		if (p != NULL) {
			sumOfDigit += p->val;
			p = p->next;
		}
		if (q != NULL) {
			sumOfDigit += q->val;
			q = q->next;
		}
		rest = sumOfDigit / 10;
		sumOfDigit = sumOfDigit % 10;
		if (sum == NULL) {
			sum = new ListNode(sumOfDigit);
			sumTail = sum;
		}
		else {
			ListNode * ln = new ListNode(sumOfDigit);
			sumTail->next = ln;
			sumTail = ln;
		}
	}
	if (rest > 0) {
		ListNode * ln = new ListNode(rest);
		sumTail->next = ln;
		sumTail = ln;
	}
	return sum;
}

ListNode * createLinkedList(int val) {
	ListNode* ln = new ListNode(val);
	return ln;
}

ListNode* addNode(ListNode * tail, int val) {
	ListNode* ln = new ListNode(val);
	tail->next = ln;
	return ln;
}

void deleteLinkedList(ListNode * l) {
	while (l != NULL) {
		ListNode * next = l->next;
		delete(l);
		l = next;
	}
}

void printLinkedList(ListNode* l) {
	while (l != NULL) {
		ListNode * next = l->next;
		cout << l->val << " ";
		l = next;
	}
	cout << endl;
}

int main() {
	ListNode * l1 = createLinkedList(2);
	ListNode * l1Tail = l1;
	//l1Tail = addNode(l1Tail, 4);
	//l1Tail = addNode(l1Tail, 3);
	ListNode * l2 = createLinkedList(8);
	ListNode * l2Tail = l2;
	l2Tail = addNode(l2Tail, 9);
	l2Tail = addNode(l2Tail, 9);
	ListNode * sum = addTwoNumbers(l1, l2);
	printLinkedList(sum);
	deleteLinkedList(sum);
	deleteLinkedList(l1);
	deleteLinkedList(l2);
}

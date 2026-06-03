/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    ListNode* res;
    int i = 0;
public:
    ListNode* middleNode(ListNode* head) {
        res = head;
        while( head != NULL )
        {
            if( i%2 == 1 )
                res = res->next;
            head = head->next;
            i++;
        }
        return res;
    }
};
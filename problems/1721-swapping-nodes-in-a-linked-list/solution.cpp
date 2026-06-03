class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* leftNode = head;
        ListNode* rightNode = head;
        
        for (int i = 1; i < k; i++) {
            leftNode = leftNode->next;
        }
        
        ListNode* current = leftNode;
        while (current->next != nullptr) {
            current = current->next;
            rightNode = rightNode->next;
        }
        
        int temp = leftNode->val;
        leftNode->val = rightNode->val;
        rightNode->val = temp;
        
        return head;
    }
};
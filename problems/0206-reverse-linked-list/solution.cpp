class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* temp = nullptr;
        ListNode* head2 = nullptr;

        while (head != nullptr) {
            temp = head;

            head = head->next;

        
            temp->next = head2;

            head2 = temp;
        }

        
        return head2;
    }
};
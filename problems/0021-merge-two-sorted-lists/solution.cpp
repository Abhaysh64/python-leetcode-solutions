
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* prev=NULL;
        ListNode* head=list1;
        ListNode* ans=NULL;
        if(list1==NULL){
            return list2;
        }
        if(list2==NULL){
            return list1;
        }

        if(head->val > list2->val){
            list1=list2;
            list2=list2->next;
            list1->next=head;
            prev=list1;
        }
 
        while(list2!=NULL && head!=NULL){
            if(head->val > list2->val){
            ans=list2;
            list2=list2->next;
            prev->next=ans;
            ans->next=head;
            prev=ans;
            }
             else{
                prev=head;
                if(head->next==NULL){
                break;
             }  
             head=head->next;
             }
            }

            if(list2!=NULL){
               head->next=list2;
            }
        return list1;
    }
};
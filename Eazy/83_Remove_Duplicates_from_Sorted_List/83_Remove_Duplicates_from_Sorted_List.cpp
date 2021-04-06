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
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *count = head;
        ListNode *temp = count;
        int pre;
        if(temp != NULL){
            pre = temp->val;
            temp = temp->next;
        }
        else{
            return head;
        }
        while(temp != NULL){
            if(temp->val != pre){
                count->next = temp;
                pre = temp->val;
                count = count->next;
            }
            temp = temp->next;
        }
        count->next = temp;

        return head;
    }
};
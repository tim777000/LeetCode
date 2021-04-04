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
    ListNode* swapPairs(ListNode* head) {
        ListNode *first = head;
        ListNode *second = NULL; 
        ListNode *temp = NULL;
        ListNode *pre = NULL;
        if(first == NULL){
            return head;
        }
        else if(first->next != NULL){
            second = first->next;
            head = second;
        }
        while(first->next != NULL){
            second = first->next;

            temp = second->next;
            second->next = first;
            first->next = temp;
            if(pre != NULL){
                pre->next = second;
            }
            pre = first;

            first = first->next;
            if(first == NULL){
                break;
            }
        }

        return head;
    }
};
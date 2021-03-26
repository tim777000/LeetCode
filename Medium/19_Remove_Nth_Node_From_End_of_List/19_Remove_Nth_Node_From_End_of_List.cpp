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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* prev = NULL;
        ListNode* first = head;
        ListNode* second = head;
        int counter = n - 1;
        while(counter > 0){
            first = first->next;
            counter--;
        }
        while(first != NULL){
            if(first->next == NULL){
                break;
            }
            first = first->next;
            prev = second;
            second = second->next;
        }
        if(prev != NULL){
            prev->next = second->next;
        }
        else{
            head = second->next;
        }
        return head;
    }
};
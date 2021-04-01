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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* answer = NULL;
        ListNode* temp = NULL;
        if(l1 == NULL || l2 == NULL){
            if(l1 == NULL){
                answer = l2;
            }
            else if(l2 == NULL){
                answer = l1;
            }
            return answer;
        }
        if(l1->val > l2->val){
            answer = l2;
            l2 = l2->next;
        }
        else{
            answer = l1;
            l1 = l1->next;
        }
        temp = answer;
        while(true){
            if(l1 == NULL || l2 == NULL){
                if(l1 == NULL){
                    temp->next = l2;
                }
                else if(l2 == NULL){
                    temp->next = l1;
                }
                break;
            }
            if(l1->val > l2->val){
                temp->next = l2;
                l2 = l2->next;
                temp = temp->next;
            }
            else{
                temp->next = l1;
                l1 = l1->next;
                temp = temp->next;
            }
        }
        return answer;
    }
};
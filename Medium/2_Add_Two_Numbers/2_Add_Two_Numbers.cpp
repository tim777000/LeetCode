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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int l1_d, l2_d, carryout = 0, target;
        ListNode* l3 = new ListNode();
        ListNode* ans = l3;
        while(true){
            l1_d = 0, l2_d = 0;
            if (l1 != nullptr){
                l1_d = l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr){
                l2_d = l2->val;
                l2 = l2->next;
            }
            target = (l1_d + l2_d + carryout) % 10;
            carryout = (l1_d + l2_d + carryout) / 10;
            //printf("%d %d\n", target, carryout);
            l3->val = target;
            if (l1 == nullptr && l2 == nullptr){
                if (carryout == 0)
                    break;
            }
            l3->next = new ListNode();
            l3 = l3->next;
        }
        return ans;
    }
};
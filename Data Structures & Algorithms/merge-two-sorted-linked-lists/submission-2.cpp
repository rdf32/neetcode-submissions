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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        vector<int> inter_store;

        while (list1){
            inter_store.push_back(list1->val);
            list1 = list1->next;
        }

        while (list2){
            inter_store.push_back(list2->val);
            list2 = list2->next;
        }

        if (inter_store.empty())
            return nullptr;

        std::sort(inter_store.begin(), inter_store.end());

        ListNode* head = new ListNode(inter_store[0]);
        ListNode* curr = head;
        for (int i = 1; i < inter_store.size(); i++){
            curr->next = new ListNode(inter_store[i]);
            curr = curr->next;
        }

        return head;
    }
};

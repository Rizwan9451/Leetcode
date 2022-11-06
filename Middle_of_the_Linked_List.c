/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head){
      int c=0;
      struct ListNode*start=NULL;
      start=head;
      while(head!=NULL){
          head=head->next;
          c+=1;
      }
        int s=c/2;
        // printf(s,c);
        while(s){
            start=start->next;
            s-=1;
        }
        return start;
}
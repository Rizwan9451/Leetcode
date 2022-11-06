/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head){
  struct ListNode*pre=NULL;
  struct ListNode*curr=head;
  struct ListNode*nxt=NULL;
  if(head==NULL){
      return head;
  }
  while(curr!=NULL){
      nxt=curr->next;
      curr->next=pre;
      pre=curr;
      curr=nxt;
  }
  return pre;

}
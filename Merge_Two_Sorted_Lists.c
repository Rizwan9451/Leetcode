/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode*new;
    struct ListNode*start;
     if(list1==NULL){
         return list2;
     }
     if(list2==NULL){
         return list1;
     }
     if(list1->val<=list2->val){
         new=list1;
         list1=list1->next;
         start=new;
     }
     else{
         new=list2;
         list2=list2->next;
         start=new;
     }
     while(list1!=NULL && list2!=NULL){
         if(list1->val<=list2->val){
              new->next=list1;
              list1=list1->next;
         }
         else{
             new->next=list2;
             list2=list2->next;
         }
         new=new->next;
     }
     if(list1==NULL){
         new->next=list2;
     }
     if(list2==NULL){
         new->next=list1;
     }
     return start;
}



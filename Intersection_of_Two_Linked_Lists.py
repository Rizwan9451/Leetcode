/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode*hA=NULL;
    struct ListNode*hB=NULL;
    hA=headA;
    hB=headB;
    int n1=0;
    int n2=0;
    while(headA!=NULL){
        headA=headA->next;
        n1+=1;
    }
    while(headB!=NULL){
        headB=headB->next;
        n2+=1;
    }
    int n=abs(n2-n1);
    if(n2>n1){
        while(n){
            hB=hB->next;
            n--;
        }
    }
    else{
        while(n){
            hA=hA->next;
            n--;
        }
    }
    while(hA!=NULL){
        if(hA==hB){
            return hA;
        }
        hA=hA->next;
        hB=hB->next;
    }
    return NULL;
}
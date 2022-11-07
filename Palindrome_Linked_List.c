/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head){
    int a[100000];
    int i=0;
    while(head!=NULL){
        a[i]=head->val;
        head=head->next;
        i+=1;
    }
    int n=i;
    for(int j=0;j<(n)/2;j++){
        if(a[j]!=a[i-1]){
           return false;
        }
        i--;
    }
    return true;

}
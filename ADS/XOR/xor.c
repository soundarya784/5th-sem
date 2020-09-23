
#include <stdio.h> 
#include <stdlib.h> 
#include <inttypes.h> 


struct Node 
{ 
	int data; 
	struct Node* npx; /* XOR of next and previous node */
}; 


struct Node* XOR (struct Node *a, struct Node *b) 
{ 
	return (struct Node*) ((uintptr_t) (a) ^ (uintptr_t) (b)); 
} 


void insert_end (struct Node **head, int data) 
{ 
  struct Node *new_node = (struct Node *) malloc (sizeof (struct Node) );
  new_node->data = data; 

  struct Node *curr = *head; 
  struct Node *prev = NULL; 
  struct Node *npx; 



  while (curr->npx != NULL) 
  {   
      
      npx = XOR (prev, curr->npx); 
      prev = curr; 
      curr = npx; 
  } 

  prev->npx = XOR(new_node, (XOR(NULL, prev->npx)));
  new_node->npx = XOR(NULL, prev);
} 


void insert_beg(struct Node **head_ref, int data) 
{ 
	
	struct Node *new_node = (struct Node *) malloc (sizeof (struct Node) ); 
	new_node->data = data; 


	new_node->npx = *head_ref; 


	if (*head_ref != NULL) 
	{ 
		
		(*head_ref)->npx = XOR(new_node, (*head_ref)->npx); 
	} 


	*head_ref = new_node; 
} 

 
void printList (struct Node *head) 
{ 
	struct Node *curr = head; 
	struct Node *prev = NULL; 
	struct Node *next; 

	printf (" nodes of Linked List: \n"); 

	while (curr != NULL) 
	{ 

		printf ("%d ", curr->data); 
		next = XOR (prev, curr->npx); 

		prev = curr; 
		curr = next; 
	} 
} 
int main () 
{ 

	struct Node *head = NULL; 
  insert_beg(&head, 50);
   insert_beg(&head, 60);
	insert_beg(&head, 1); 
	insert_beg(&head, 5); 
	insert_beg(&head, 9); 
	insert_beg(&head, 40); 
  

	printList (head); 

	return (0); 
} 


#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
   	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 3);
	add_nodeint_end(&head, 4);
	add_nodeint_end(&head, 5);
	add_nodeint_end(&head, 6);
	add_nodeint_end(&head, 7);
	add_nodeint_end(&head, 8);
	add_nodeint_end(&head, 9);
	add_nodeint_end(&head, 10);
	add_nodeint_end(&head, 11);
	add_nodeint_end(&head, 10);
	add_nodeint_end(&head, 9);
	add_nodeint_end(&head, 8);
	add_nodeint_end(&head, 7);
	add_nodeint_end(&head, 6);
	add_nodeint_end(&head, 5);
	add_nodeint_end(&head, 4);
	add_nodeint_end(&head, 3);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 1);

    print_listint(head);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return (0);
}

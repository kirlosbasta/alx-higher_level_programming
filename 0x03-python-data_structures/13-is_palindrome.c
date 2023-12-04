#include "lists.h"

/**
 * is_palindrome - check if a number in reverse is the same as normal
 * @head: head of the list
 *
 * Return: 0 if it's not palindrome 1 if it's
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL, *next;

    if (*head == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    if (fast != NULL)
        slow = slow->next;

    while (prev != NULL && prev->n == slow->n)
    {
        slow = slow->next;
        prev = prev->next;
    }

    return (prev == NULL);
}

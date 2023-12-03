#include "lists.h"

/**
 * is_palindrome - check if a number in reverse is the same as normal
 * @head: head of the list
 *
 * Return: 0 if it's not palindrome 1 if it's
 */

int is_palindrome(listint_t **head)
{
	int *list = malloc(sizeof(int) * 10);
	int size_list = 10;
	int count = 0, i;
	listint_t *current = *head;

	if (list == NULL)
		return (0);
	if (current == NULL || current->next == NULL)
	{
		free(list);
		return (1);
	}
	while (current != NULL)
	{
		if (count > 9)
		{
			list = realloc(list, size_list + 1);
			if (list == NULL)
				return (0);
			size_list++;
		}
		list[count++] = current->n;
		current = current->next;
	}
	for (i = 0; i < (count / 2); i++)
	{
		if (list[i] != list[count - 1 - i])
		{
			free(list);
			return (0);
		}
	}
	free(list);
	return (1);
}

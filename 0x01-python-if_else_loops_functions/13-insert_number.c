#include "lists.h"

/**
 * insert_node - Add a node in sorted way ascending
 * @head: Head of the list
 * @number: intger to add
 *
 * Return: pointer to the new node or NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL, *tmp, *current;

	if (*head == NULL)
	{
		node = add_nodeint_end(head, number);
		return (node);
	}
	current = *head;
	while (current != NULL)
	{
		if (current->n > number)
		{
			node = malloc(sizeof(listint_t));
			if (node == NULL)
			{
				return (NULL);
			}
			node->n = number;
			node->next = current;
			tmp->next = node;
			return (node);
		}
		tmp = current;
		current = current->next;
	}
	node = add_nodeint_end(head, number);
	return (node);
}

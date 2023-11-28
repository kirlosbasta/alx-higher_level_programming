#include "lists.h"

/**
 * check_cycle - check if a singly linked list is a cycle or not
 * @list: head of the list
 *
 * Return: 0 if list has no cycle and 1 it has
 */

int check_cycle(listint_t *list)
{
	listint_t *speed1, *speed2;

	if (list == NULL)
	{
		return (0);
	}
	speed1 = list;
	speed2 = list;
	while (speed2 != NULL)
	{
		speed1 = speed1->next;
		if (speed2 != NULL)
			speed2 = speed2->next;
		if (speed2 != NULL)
			speed2 = speed2->next;
		if (speed1 == speed2 && speed1)
		{
			return (1);
		}
	}
	return (0);
}

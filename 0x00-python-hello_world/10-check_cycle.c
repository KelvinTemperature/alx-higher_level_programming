#include "lists.h"

/**
 * check_cycle - checks a linked list for a cycle
 * @list: list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *move_1;
	listint_t *move_2;

	move_1 = list;
	move_2 = list;

	while (move_1 && move_2 && move_2->next)
	{
		move_1 = move_1->next;
		move_2 = move_2->next->next;
		if (move_1 == move_2)
			return (1);
	}
	return (0);
}

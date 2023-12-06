#include "lists.h"

/**
 * is_palindrome - checks if a list is a pallindrome
 * @head: head of the list
 * Return: 1 on success, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	int list[10000];
	long int i = 0, j, k;
	listint_t *temp;

	if (*head == NULL)
		return (1);

	temp = *head;
	while (temp != NULL)
	{
		list[i] = temp->n;
		i++;
		temp = temp->next;
	}

	j = (i + 1) / 2;

	for (k = 0; k < j; k++)
	{
		if (list[k] == list[i - k - 1])
		{
		}
		else
			return (0);
	}
	return (1);
}

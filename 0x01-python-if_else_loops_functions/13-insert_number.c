#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: begining of the list
 * @number: the value to be inserted
 * Return: Address of new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *add_node, *temp;

	add_node = malloc(sizeof(listint_t));
	if (add_node == NULL)
		return (NULL);

	add_node->n = number;
	add_node->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		add_node->next = *head;
		*head = add_node;
		return (add_node);
	}
	else
	{
		temp = *head;
		while (temp->next != NULL && temp->next->n < add_node->n)
		{
			temp = temp->next;
		}
		add_node->next = temp->next;
		temp->next = add_node;
	}
	return (add_node);
}

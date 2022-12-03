#include "lists.h"

/**
 * insert_node - insert an int into a listint object
 * @head: head node of a listint object
 * @number: int to be inserted
 * Return: address of newly inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	if (!head)
		return (NULL);
	node->n = number;
	while (*head)
	{
		if ((*head)->n > number)
		{
			node->next = *head;
			node = *head;
		}
		head++;
	}
	return (node);
}

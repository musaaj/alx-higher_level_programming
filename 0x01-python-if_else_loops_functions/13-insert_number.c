#include "lists.h"

/**
 * insert_node - insert an int into a listint object
 * @head: head node of a listint object
 * @number: int to be inserted
 * Return: address of newly inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	if (!head)
		return (NULL);
	node->n = number;
	while ((*head)->next)
	{
		if (((*head)->next)->n  >= number)
		{
			tmp = (*head)->next;
			(*head)->next = node;
			node->next = tmp;
			return (node);
		}
		*head = (*head)->next;
	}
	*(head)->next = node;
	return (node);
}

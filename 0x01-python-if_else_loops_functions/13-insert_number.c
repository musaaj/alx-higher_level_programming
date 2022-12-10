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
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	if ((*head)->n >= number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while ((*head)->next && ((*head)->next)->n < number)
	{
		*head = (*head)->next;
	}
	node->next = (*head)->next;
	(*head)->next = node;
	return (node);
}

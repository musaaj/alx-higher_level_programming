#include "lists.h"

/**
 * insert_node - insert an int into a listint object
 * @head: head node of a listint object
 * @number: int to be inserted
 * Return: address of newly inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp = NULL, *dtmp;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	if (!tmp)
		return (NULL);
	if (!head)
		return (NULL);
	node->n = number;
	tmp = *head;
	while (tmp)
	{
		if (tmp->n < number)
			tmp++;
		else
			break;
	}
	dtmp = tmp->next;
	tmp->next = node;
	node->next = dtmp;
	*head = tmp;
	return (node);
}

#include "lists.h"

/**
 * check_cycle - check whether there is cylcle in
 * a linked list object
 * @list: head of a linked list
 * Return: 1 if there is cycle else 0
 */
int check_cycle(list_t *list)
{
	list_t p1, p2;

	if (list)
		return (0);
	p1 = malloc(sizeof(list_t));
	if (!p1)
		return (0);
	p2 = malloc(sizeof(list_t));
	if (!p2)
	{
		free(p1);
		return (0);
	}
	p1 = list;
	while (p1)
	{
		p2 = p1->next;
		if (p2 == p1)
			return (1);
		p1 = p2;
	}
	return (0);
}

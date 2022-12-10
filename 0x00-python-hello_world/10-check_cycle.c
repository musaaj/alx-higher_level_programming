#include "lists.h"
/**
 * check_cycle - check whether there is cylcle in
 * a linked list object
 * @list: head of a linked list
 * Return: 1 if there is cycle else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp, *tmp2, *tmp3;

	if (!list)
		return (0);
	if (!list->next)
		return (0);
	tmp = list;
	while (tmp->next)
	{
		tmp2 = tmp;
		tmp3 = list->next;
		while (tmp3->next)
		{
			if (tmp2 == tmp3->next)
				return (1);
			tmp3 = tmp3->next;
		}
		tmp = tmp->next;
		list = list->next;
	}
	return (0);
}

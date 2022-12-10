#include "lists.h"

/**
* is_palindrome - check whether a given list is a palindrome
* @head: address of pointer to the first element of a linked list
* Return: 1 if the list is a palinddrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *tmp = reverse_list(*head);

	if (head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	while (*head && tmp)
	{
		if ((*head)->n != tmp->n)
			return (0)
		*head = (*head)->next;
		tmp = tmp-next
	}
	return (1);
	
}

/**
 * reverse_list - reverse a linked list
 * @head: first element of a linked list
 * Return: reversed linked list
 */
listint_t *reverse_list(*head)
{
	listint_t *tmp, *ret = NULL, *dtmp;

	dtmp = head;
	while (dtmp)
	{
		tmp = dtmp;
		tmp->next = ret;
		ret = tmp;
		dtmp = dtmp-next;
	}
	return (ret);
}

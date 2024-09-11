#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to pointer to the first node of the list.
 * @number: Number to be inserted into the list.
 * Return: Address of the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node;
    listint_t *current;
    listint_t *prev = NULL;

    /* Create a new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    /* If the list is empty or the new node should be the new head */
    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        /* Traverse the list to find the insertion point */
        current = *head;
        while (current != NULL && current->n < number)
        {
            prev = current;
            current = current->next;
        }
        /* Insert the new node */
        new_node->next = current;
        prev->next = new_node;
    }

    return (new_node);
}


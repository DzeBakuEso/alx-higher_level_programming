i#include "lists.h"

/**
 * reverse_list - Reverses the linked list.
 * @head: Double pointer to the head of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
    return *head;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *second_half, *first_half;
    int result = 1; // Assume it is a palindrome

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    // Find the middle of the list
    slow = fast = *head;
    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the second half of the list
    second_half = reverse_list(&slow);

    // Compare the first and second half
    first_half = *head;
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            result = 0; // Not a palindrome
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // Restore the list (optional)
    reverse_list(&slow);

    return result;
}


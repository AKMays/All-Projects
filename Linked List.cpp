/*
Purpose: defines a templated class called "List" that implements a singly linked list
Authors: Adonte Mays
Date: 2023-22-04
Updated
*/

//included aspects in List.h file
#include "List.h"

// Default constructor
template <class T>
List<T>::List()
{
    // sets the head of the list to NULL, indicating an empty list
	head = NULL;
}

// Copy constructor
template <class T>
List<T>::List(const List<T>& mylist)
{
    // Create new nodes for the copied list
    if (mylist.head == NULL)
        head = NULL;
    else
    {
        // copies the head node of mylist to the new list
        head = new Node;
        head->item = mylist.head->item;
        Node* ptr = head;
        Node* myptr = mylist.head->next;
        // copies the rest of the nodes from mylist to the new list
        while (myptr != NULL)
        {
            ptr->next = new Node;
            ptr = ptr->next;
            ptr->item = myptr->item;
            myptr = myptr->next;
        }
        ptr->next = NULL;  // Set the next pointer of the last node to NULL
    }
}


// Destructor
template <class T>
List<T>::~List()
{
    // deallocate all the nodes in the list
    Node* ptr = head;
    // Loop through each node in the list.
    while (ptr != NULL)
    {
        Node* temp = ptr;
        ptr = ptr->next;
        delete temp;
    }
    head = NULL; //set head to Null
}

#This is not the entire code. I am uploading a portion due to this being an class project. Additionally, this code only works with the List.H file.
#If you'd like to see the entire program email me - mays_a1@denison.edu

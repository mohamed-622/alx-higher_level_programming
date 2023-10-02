#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers is None or list_of_integers == []:
        return None
    
    left, right = 0, len(list_of_integers) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Compare the middle element with its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return list_of_integers[left]

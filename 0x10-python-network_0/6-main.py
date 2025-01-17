#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))  # Should return 6
print(find_peak([4, 2, 1, 2, 3, 1]))  # Should return 4 or 3
print(find_peak([2, 2, 2]))  # Should return 2
print(find_peak([]))  # Should return None
print(find_peak([-2, -4, 2, 1]))  # Should return 2
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # Should return 4

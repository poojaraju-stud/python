Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def binary_search(arr, key):
...     low = 0
...     high = len(arr) - 1
... 
...     while low <= high:
...         mid = (low + high) // 2
... 
...         if arr[mid] == key:
...             return mid  # Key found at index mid
...         elif arr[mid] < key:
...             low = mid + 1
...         else:
...             high = mid - 1
... 
...     return -1  # Key not found
... 
... # Example usage
... sorted_list = [1, 3, 5, 7, 9, 11, 13]
... key_to_find = 7
... 
... result = binary_search(sorted_list, key_to_find)
... if result != -1:
...     print(f"Key found at index {result}")
... else:
...     print("Key not found")

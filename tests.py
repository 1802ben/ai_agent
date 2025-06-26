import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

test1 = run_python_file("calculator", "main.py")
test2 = run_python_file("calculator", "tests.py")
test3 = run_python_file("calculator", "../main.py")
test4 = run_python_file("calculator", "nonexistent.py")

print(test1)
print(test2)
print(test3)
print(test4)


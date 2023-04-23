Note : cannot remove Pylance import pytest error.
Probably, need to set path but not knowing proper syntax now.
Everything works, but only visual.

- for changing prompt use : python3 -m venv .venv --prompt ...

Exercise: Writing tests with pytest


In this short exercise, you will set up and write your first pytest tests!

Setup
Using your previous virtual environment project as a base, make sure you have pytest properly installed and activate your shell.

Writing tests
Start by creating a test folder in the project directory you created in the last exercise.
Create a __init__.py file within the test folder.
Then make a file called my_first_test.py.
Within the file, import pytest and write function definitions for the tests you plan on writing. From here, go ahead and write at least one assertion for the RegularPolygon class.
For example, write tests to see if the get_perimeter method can retrieve the polygon's perimeter as intended, following the recipe below:

Arrange: Create an instance of the polygon class.
Act: Calculate the expected perimeter.
Assert: Call the get_perimeter function to assert expected is equal to result.
Running tests
Run the command:

> pytest
Hopefully, you should see pytest flavored output for your tests. Make sure your tests pass and feel free to write more tests and explore pytest's capabilities!
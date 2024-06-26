UTF-8 Validation

This project aims to implement a method in Python that determines if a given dataset represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding standard that can represent every character in the Unicode character set.
Requirements
General

    Allowed Editors: vi, vim, emacs
    Operating System: Ubuntu 20.04 LTS
    Python Version: 3.4.3
    File Requirements: All files must end with a new line and start with #!/usr/bin/python3
    README: A README.md file is mandatory, providing an overview of the project and its usage.
    Coding Style: Code should adhere to PEP 8 style guidelines (version 1.7.x).
    Executable Files: All Python files must be executable.

Tasks

    UTF-8 Validation:
        Write a method validUTF8(data) that returns True if the given data set is a valid UTF-8 encoding, otherwise False.
        The input data is represented as a list of integers, where each integer represents 1 byte of data (8 bits).
        UTF-8 characters can be 1 to 4 bytes long, and the method should handle up to 4 bytes.

Concepts and Resources

To successfully complete this project, familiarity with the following concepts is beneficial:

    Bitwise Operations in Python: Manipulating bits using operators like &, |, ^, <<, >>.
    UTF-8 Encoding Scheme: Understanding how characters are encoded into bytes under UTF-8.
    Data Representation: Working with data at the byte level and handling LSB (Least Significant Bits).
    List Manipulation in Python: Iterating through lists and list comprehensions.
    Boolean Logic: Applying logical operations to make decisions in the program.

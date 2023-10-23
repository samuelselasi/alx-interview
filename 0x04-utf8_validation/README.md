# 0x04. UTF-8 Validation
#### `Algorithm` `Python`
![FSS-UTF_1992_UTF-8_1993](https://github.com/samuelselasi/alx-interview/assets/85158665/1c44f57a-ca98-4e17-96c4-63ff5d919368)

## Resources
**Read or watch**:

* [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
* [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu `20.04` LTS using `python3` (version `3.4.3`)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style (version `1.7.x`)
* All your files must be executable

## Tasks

[0. UTF-8 Validation](./0-validate_utf8.py)

Write a method that determines if a given data set represents a valid `UTF-8` encoding.

* Prototype: `def validUTF8(data)`
* Return: `True` if data is a valid `UTF-8` encoding, else return `False`
* A character in `UTF-8` can be `1` to `4` bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents `1` byte of data, therefore you only need to handle the `8` least significant bits of each integer

```
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$
```
```
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```

## Pseudocode
```
1. Initialize variable `remainingBytes` to 0
2. Define constant `BIT7` as (1 << 7)  # Represents the leftmost bit (bit 7)
3. Define constant `BIT6` as (1 << 6)  # Represents the second leftmost bit (bit 6)
4. Loop through each `byte` in the `data` list:
    5. Initialize `bitPosition` to `BIT7`
    6. If `remainingBytes` is 0:
        7. While `byte` & `bitPosition` is True:
            8. Increment `remainingBytes` by 1
            9. Right-shift `bitPosition` by 1
        10. If `remainingBytes` is still 0, continue to the next byte
        11. If `remainingBytes` is 1 or greater than 4, return False
    12. Else (there are still bytes left to complete a character):
        13. If `byte` & `BIT7` is False or `byte` & `BIT6` is True:
            14. Return False
    15. Decrement `remainingBytes` by 1
16. If `remainingBytes` is 0, return True, indicating a valid UTF-8 encoding
17. Otherwise, return False
```

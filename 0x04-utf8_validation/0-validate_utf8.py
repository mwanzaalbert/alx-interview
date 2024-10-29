#!/usr/bin/python3
"""
UTF-8 Validation Module

This module provides a function, `validUTF8`, to determine whether a list of
integers represents a valid UTF-8 encoding. Each integer in the list is treated
as a byte, and the function applies bitwise operations to validate multi-byte
UTF-8 characters according to the UTF-8 encoding scheme.
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    UTF-8 characters can be 1 to 4 bytes long, with specific bit patterns for
    each byte that define valid encodings:
      - 1-byte character: 0xxxxxxx
      - 2-byte character: 110xxxxx 10xxxxxx
      - 3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
      - 4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    Args:
        data (List[int]): A list of integers, each representing a byte (8 bits)
                         of data.

    Returns:
        bool: True if the data set represents a valid UTF-8 encoding,
              False otherwise.

    Example:
        >>> validUTF8([65])
        True
        >>> validUTF8([229, 65, 127, 256])
        False
    """

    # Track number of bytes remaining in the current UTF-8 character
    n_bytes: int = 0

    # Masks to check the leading bits in each byte
    mask1: int = 1 << 7  # 10000000
    mask2: int = 1 << 6  # 01000000

    for num in data:
        # Obtain only the last 8 bits (simulate one byte)
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            # 1-byte character or invalid UTF-8 (more than 4 bytes)
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Verify the byte starts with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    dataset = [80, 121, 116, 104, 111, 110, 32,
               105, 115, 32, 99, 111, 111, 108, 33]
    print()
    print(validUTF8(dataset))

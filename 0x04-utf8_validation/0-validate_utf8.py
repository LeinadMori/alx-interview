#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the most significant bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each byte in the data
    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1 byte character or invalid initial byte
            if num_bytes == 0:
                continue

            # If the number of bytes is greater than 4 or equal to 1, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes to process
        num_bytes -= 1

    # If we finished processing all bytes and there are no more expected continuation bytes
    return num_bytes == 0

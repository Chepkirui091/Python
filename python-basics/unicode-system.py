# Unicode is a standard for encoding characters in computing. It allows for the representation of a wide range of characters from different languages and scripts. In Python, strings are Unicode by default, which means they can contain characters from various languages and symbols.
# You can create Unicode strings in Python using the str type. For example:
# Creating a Unicode string
unicode_string = "Hello, 世界!"  # This string contains both English and Chinese characters
print(unicode_string)  # Output: Hello, 世界!

# A sequence of code points is represented in memory as a set of code units, mapped to 8-bit bytes. The rules for translating a Unicode string into a sequence of bytes are called a character encoding.
# Three types of encodings are present, UTF-8, UTF-16 and UTF-32. UTF stands for Unicode Transformation Format.
# UTF-8 is a variable-width encoding that uses one to four bytes to represent characters. It is the most commonly used encoding on the web and is compatible with ASCII.
# Encoding a Unicode string to UTF-8 bytes
utf8_bytes = unicode_string.encode("utf-8")
print(utf8_bytes)  # Output: b'Hello, \xe4\xb8\x96\xe7\x95\x8c!'
# UTF-16 is a variable-width encoding that uses two or four bytes to represent characters. It is commonly used in Windows and Java environments.
# Encoding a Unicode string to UTF-16 bytes
utf16_bytes = unicode_string.encode("utf-16")
print(utf16_bytes)  # Output: b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00\x97\x00\xc9\x00!\x00'
# UTF-32 is a fixed-width encoding that uses four bytes to represent characters. It is less commonly used due to its larger memory footprint.
# Encoding a Unicode string to UTF-32 bytes
utf32_bytes = unicode_string.encode("utf-32")
print(utf32_bytes)  # Output: b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00,\x00\x00\x00 \x00\x00\x00\x97\x00\x...

# You can also decode bytes back to a Unicode string using the decode() method. For example:
# Decoding UTF-8 bytes back to a Unicode string
decoded_string = utf8_bytes.decode("utf-8")
print(decoded_string)  # Output: Hello, 世界!

# In Python, you can also use Unicode escape sequences to represent characters that may not be easily typed on a keyboard. For example:
# Using Unicode escape sequences
unicode_escape_string = "Hello, \u4e16\u754c!"  # \u4e16 is the Unicode escape for '世' and \u754c is the escape for '界'
print(unicode_escape_string)  # Output: Hello, 世界!

# You can also use raw strings to avoid interpreting backslashes as escape characters. For example:
# Using raw strings
raw_string = r"Hello, \u4e16\u754c!"  # The backslashes will be treated as literal characters
print(raw_string)  # Output: Hello, \u4e16\u754c!

# In Python 3, all strings are Unicode by default, so you can directly use Unicode characters in your string literals without needing to specify an encoding. However, when working with files or network communication, you may need to specify the encoding to ensure that the data is correctly interpreted. For example:
# Writing a Unicode string to a file with UTF-8 encoding
with open("unicode_file.txt", "w", encoding="utf-8") as f:
    f.write(unicode_string)
    
# Reading a Unicode string from a file with UTF-8 encoding
with open("unicode_file.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)  # Output: Hello, 世界!
    
    # When working with network communication, you may also need to encode and decode Unicode strings to ensure that the data is correctly transmitted and received. For example:
# Simulating sending a Unicode string over a network
import socket
# Create a socket and connect to a server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.connect(("localhost", 12345))
# Send a Unicode string encoded as UTF-8 bytes
s.send(unicode_string.encode("utf-8"))
# Receive a response from the server and decode it back to a Unicode string
response = s.recv(1024).decode("utf-8")
print("Received from server:", response)
s.close()

#Pyhton Unicode support allows you to work with a wide range of characters and symbols, making it easier to create applications that can handle internationalization and localization.
var = "3/4"
print (var)
var = "\u00BE"
print (var) # Output: ¾ (the Unicode character for the fraction three-quarters)

#Code points are the unique numbers assigned to each character in the Unicode standard. They are represented in hexadecimal format and can be used to identify and manipulate characters in a Unicode string. For example:
# Getting the code point of a character
code_point = ord("\u00BE")
print(code_point)  # Output: 190 (the Unicode code point for the fraction three-quarters)
import zlib
string = "hello world!hello world!hello world!hello world!"
z = zlib.compress(string)
print zlib.decompress(z)

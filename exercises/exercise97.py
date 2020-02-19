import zlib
s = 'hello world!hello world!hello world!hello world!'
s = zlib.compress(s.encode())

print(zlib.decompress(s))

# In python3, zlib.compress() takes a bytes-like value.
# Therefore, when we do compress, the string needs to be encoded to be in byte-like value
# compress(s.encode()) will do this.
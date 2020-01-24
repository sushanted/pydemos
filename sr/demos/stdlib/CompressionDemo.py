import zlib

text = b'compress this text, please compress this text'

print("Actual length:", len(text))

compressed = zlib.compress(text)

print("compressed length:", len(compressed))

decompressed = zlib.decompress(compressed)

print("Decompressed:", decompressed)

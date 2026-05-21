# Read the data
with open('shakespeare.txt', 'r') as f:
    text = f.read()

# Find every unique character
chars = sorted(set(text))
vocab_size = len(chars)

print(f"Total characters in dataset: {len(text)}")
print(f"Unique characters (vocabulary size): {vocab_size}")
print(f"Vocabulary: {''.join(chars)}")

# Create mappings: character <-> integer
stoi = {ch: i for i, ch in enumerate(chars)}  # string to int
itos = {i: ch for i, ch in enumerate(chars)}  # int to string

# Encode and decode functions
def encode(s):
    return [stoi[c] for c in s]

def decode(tokens):
    return ''.join([itos[i] for i in tokens])

# Test it
sample = "Hello World"
encoded = encode(sample)
decoded = decode(encoded)

print(f"\nSample: {sample}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")

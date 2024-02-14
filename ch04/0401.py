n_files = 10
files = []

# Method 1 - this can fail because it doesn't close files (253 is maximum allowed)
for i in range(n_files):
    files.append(open(f"output1/sample{i}.txt", "w"))

# Method 2 - manually close files
for i in range(n_files):
    f = open(f"output1/sample{i}.txt", "w")
    files.append(f)
    f.close()

# Method 3 - the with context manager automatically closes files when finished
for i in range(n_files):
    with open(f"output1/sample{i}.txt", "w") as f:
        files.append(f)
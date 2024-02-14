n_files = 254
files = []

# Method 1
for i in range(n_files):
    files.append(open(f"output1/sample{i}.txt", "w"))

# Method 2
for i in range(n_files):
    f = open(f"output1/sample{i}.txt", "w")
    files.append(f)
    f.close()

# Method 3
for i in range(n_files):
    with open(f"output1/sample{i}.txt", "w") as f:
        files.append(f)
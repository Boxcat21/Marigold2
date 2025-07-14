import os

# Directory with depth images
depth_dir = "./data/batch1/depths"

# Output filenames list
output_dir = "./datasplit/tumor_depth"
train_file = os.path.join(output_dir, "filenames_train.txt")
val_file = os.path.join(output_dir, "filenames_val.txt")

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Gather all filenames (no extension)
filenames = sorted([
    os.path.splitext(f)[0]
    for f in os.listdir(depth_dir)
    if f.endswith(".png")
])


trainsplit_size = int(0.8 * len(filenames))  # 80% for training
valsplit_size = len(filenames) - trainsplit_size  # Remaining 20% for validation

# Write to file
with open(train_file, 'w') as f:
    for name in filenames[:trainsplit_size]:
        f.write("./data/batch1/images/" + name + " " + "./data/batch1/depths/" + name + "\n")
        
with open(val_file, 'w') as f:
    for name in filenames[trainsplit_size:]:
        f.write("./data/batch1/images/" + name + " " + "./data/batch1/depths/" + name + "\n")

print(f"Wrote {len(filenames)} filenames to {train_file} and {val_file}")

import os

# Set the base directory (dataset.dir from YAML)
base_dir = "/mnt/c/Users/Boxcat21/Documents/SoftwareWorkspace/Data/MarigoldData/batch1"
image_dir = os.path.join(base_dir, "images")
depth_dir = os.path.join(base_dir, "depths")

# Where to save the filename list files
output_dir = "./config/dataset_depth"
os.makedirs(output_dir, exist_ok=True)
train_file = os.path.join(output_dir, "filenames_train.txt")
val_file = os.path.join(output_dir, "filenames_val.txt")

# Get list of images (only .png files)
image_filenames = sorted([
    f for f in os.listdir(image_dir)
    if f.endswith(".png")
])

# Generate filename lines
filename_lines = []
for img in image_filenames:
    depth_name = img.replace(".png", "_1.png")
    img_rel = f"images/{img}"
    depth_rel = f"depths/{depth_name}"

    # Ensure depth file exists
    if os.path.exists(os.path.join(depth_dir, depth_name)):
        filename_lines.append(f"{img_rel} {depth_rel}")
    else:
        print(f"WARNING: Depth file missing for {img} → skipping.")

# Split into train/val if you want
split_index = int(len(filename_lines) * 0.8)
train_lines = filename_lines[:split_index]
val_lines = filename_lines[split_index:]

# Write files
with open(train_file, "w") as f:
    f.write("\n".join(train_lines))
print(f"Written {len(train_lines)} entries to {train_file}")

with open(val_file, "w") as f:
    f.write("\n".join(val_lines))
print(f"Written {len(val_lines)} entries to {val_file}")

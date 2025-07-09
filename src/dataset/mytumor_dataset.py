import os
import cv2
import numpy as np
from torch.utils.data import Dataset

class MyTumorDataset(Dataset):
    def __init__(self, root_dir, split='train', transform=None, filename_list_path=None, **kwargs):
        self.root_dir = root_dir
        self.transform = transform
        self.split = split

        self.image_dir = os.path.join(root_dir, 'images')
        self.depth_dir = os.path.join(root_dir, 'depths')

        if filename_list_path is not None:
            with open(filename_list_path, 'r') as f:
                self.samples = [line.strip() for line in f if line.strip()]
        else:
            self.samples = sorted([
                fname for fname in os.listdir(self.image_dir)
                if fname.endswith('.png')
            ])

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        img_name = self.samples[idx]
        img_path = os.path.join(self.image_dir, img_name)

        depth_name = img_name.replace('.png', '_1.png')
        depth_path = os.path.join(self.depth_dir, depth_name)

        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        depth = cv2.imread(depth_path, cv2.IMREAD_GRAYSCALE).astype(np.float32) / 255.0 * 0.002

        sample = {'image': image, 'depth': depth}

        if self.transform:
            sample = self.transform(sample)

        return sample

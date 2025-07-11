import os
import numpy as np
from src.dataset.base_depth_dataset import BaseDepthDataset, DatasetMode, DepthFileNameMode
from src.util.depth_transform import DepthNormalizerBase  # adjust path if needed


class MyTumorDataset(BaseDepthDataset):
    def __init__(
        self,
        mode: DatasetMode,
        filename_ls_path: str,
        dataset_dir: str,
        disp_name: str = "MyTumor",
        min_depth: float = 0.0,
        max_depth: float = 0.002,  # adjust if your depths go higher
        has_filled_depth: bool = False,
        name_mode: DepthFileNameMode = DepthFileNameMode.id,
        depth_transform: DepthNormalizerBase = None,
        augmentation_args: dict = None,
        resize_to_hw=None,
        move_invalid_to_far_plane: bool = True,
        rgb_transform=lambda x: x / 255.0 * 2 - 1,
        **kwargs,
    ):
        super().__init__(
            mode=mode,
            filename_ls_path=filename_ls_path,
            dataset_dir=dataset_dir,
            disp_name=disp_name,
            min_depth=min_depth,
            max_depth=max_depth,
            has_filled_depth=has_filled_depth,
            name_mode=name_mode,
            depth_transform=depth_transform,
            augmentation_args=augmentation_args,
            resize_to_hw=resize_to_hw,
            move_invalid_to_far_plane=move_invalid_to_far_plane,
            rgb_transform=rgb_transform,
            **kwargs,
        )

    def _read_depth_file(self, rel_path):
        """
        Override if your depths are stored in 8-bit PNG format and need conversion.
        Assumes values were saved as: (real_depth / 0.002 * 255).astype(np.uint8)
        """
        depth_img = self._read_image(rel_path)
        if depth_img.ndim == 3:
            depth_img = depth_img[:, :, 0]  # keep 1 channel
        depth_float = depth_img.astype(np.float32) / 255.0 * 0.002
        return depth_float

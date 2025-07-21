# 🧪 Training Marigold on a Custom Tumor Depth Dataset

This guide explains how to train the [Marigold](https://github.com/prs-eth/Marigold) monocular depth estimation model using a custom grayscale tumor dataset with corresponding depth maps.

---

## 📁 Dataset Structure

Ensure your dataset is organized in the following format:

```
./data/batch1/
├── images/
│   ├── img_000001.png
│   ├── img_000002.png
│   └── ...
└── depths/
    ├── img_000001.png
    ├── img_000002.png
    └── ...
```

Each RGB image in `images/` must have a matching depth map in `depths/` with the same filename.

---

## 🛠️ Environment Setup

1. **Clone the Marigold repository**:

```bash
git clone https://github.com/prs-eth/Marigold.git
cd Marigold
```

2. **Create and activate a virtual environment**:

```bash
python -m venv venv/marigold
source venv/marigold/bin/activate
```

3. **Install training dependencies**:

```bash
pip install -r requirements++.txt -r requirements+.txt -r requirements.txt
```

---

## 📥 Download Base Checkpoint

Before training, download the pretrained **Stable Diffusion v2.1** checkpoint:

- https://huggingface.co/stabilityai/stable-diffusion-2

Place the checkpoint files in a directory, for example:

```
../ckpt2/
└── v2-1_768-ema-pruned.ckpt  # or appropriate SDv2 UNet & scheduler structure
```

This path will be passed using `--base_ckpt_dir`.

---

## ⚙️ Configuration Files

Ensure the following config files are present and correctly set up:

- `config/train_marigold_mytumor.yaml`: Your main training config
- `config/dataset_train_mytumor.yaml`: Training dataset details
- `config/dataset_val_mytumor.yaml`: Validation dataset details

These YAMLs should define:
- Input directories (`images/`, `depths/`)
- Image preprocessing
- Output directories
- Number of epochs, batch size, etc.

---

## 🚀 Run Training

To launch training on your custom dataset, use the following command:

```bash
python script/depth/train.py \
  --config config/train_marigold_mytumor.yaml \
  --base_data_dir ./data \
  --base_ckpt_dir ../ckpt2 \
  --no_wandb
```

### Arguments:

| Flag              | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `--config`        | Training configuration YAML file                                            |
| `--base_data_dir` | Path containing your dataset (should contain `batch1/images` and `depths`) |
| `--base_ckpt_dir` | Directory containing the pretrained Stable Diffusion checkpoint             |
| `--no_wandb`      | Disable Weights & Biases logging                                            |

---

## 📦 Checkpoints and Inference

After training, checkpoints will be stored in:

```
output/train_marigold_mytumor/checkpoint/
└── latest/
    ├── unet/
    └── scheduler/
```

To use the model for inference:

1. Replace the corresponding `unet/` and `scheduler/scheduler_config.json` in an existing Marigold checkpoint.
2. Run the inference script:

```bash
python script/depth/run.py \
  --checkpoint output/train_marigold_mytumor/checkpoint/latest \
  --input_rgb_dir YOUR_RGB_DIR \
  --output_dir YOUR_OUTPUT_DIR \
  --fp16
```

---

## 🧪 Tips & Notes

- You can customize training epochs, resolution, and augmentation in your YAML configs.
- If using WSL, ensure CUDA is configured properly for GPU acceleration.
- Resume training with `--resume_run PATH_TO_CHECKPOINT`.

---

## 📄 Citation

Please cite the original Marigold paper if using this codebase:

```bibtex
@InProceedings{ke2023repurposing,
  title={Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation},
  author={Bingxin Ke and Anton Obukhov and Shengyu Huang and Nando Metzger and Rodrigo Caye Daudt and Konrad Schindler},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2024}
}
```

---

## 🔗 References

- Marigold repository: https://github.com/prs-eth/Marigold
- Hugging Face SDv2.1 checkpoint: https://huggingface.co/stabilityai/stable-diffusion-2

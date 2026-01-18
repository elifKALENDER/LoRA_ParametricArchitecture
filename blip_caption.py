from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from pathlib import Path
from tqdm import tqdm
import torch

from transformers import BlipProcessor
BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
print("OK")

# --- paths ---
IMAGE_DIR = Path("images")      # png/jpg dosyaların burada
CAPTION_DIR = Path("captions")  # txt'ler buraya yazılacak
CAPTION_DIR.mkdir(exist_ok=True)

# --- model ---
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
model.eval()

# --- optional LoRA token ---
TOKEN = "parametricfacade"

for img_path in tqdm(list(IMAGE_DIR.glob("*.png")) + list(IMAGE_DIR.glob("*.jpg"))):
    image = Image.open(img_path).convert("RGB")

    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs, max_length=50)

    caption = processor.decode(out[0], skip_special_tokens=True)

    # 🔥 LoRA için token ekle
    caption = f"{TOKEN}, {caption}"

    txt_path = CAPTION_DIR / f"{img_path.stem}.txt"
    txt_path.write_text(caption, encoding="utf-8")



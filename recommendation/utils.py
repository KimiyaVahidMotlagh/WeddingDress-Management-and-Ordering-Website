import torch
from diffusers import StableDiffusionPipeline
import safetensors.torch as sf
from peft import set_peft_model_state_dict
import logging
import os


os.environ['HF_HOME'] = 'C:/huggingface'
os.environ['TRANSFORMERS_CACHE'] = 'C:/huggingface'
os.environ['DIFFUSERS_CACHE'] = 'C:/huggingface'

logger = logging.getLogger(__name__)

MODEL_ID = "runwayml/stable-diffusion-v1-5"
MODEL_PATH = "recommendation/model/unet_lora_final.safetensors"

_device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {_device}")

# Load model once at startup - با مشخص کردن cache_dir
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32 if _device == "cpu" else torch.float16,
    safety_checker=None,
    cache_dir="C:/huggingface"  # 🔥 این خط اضافه شد
).to(_device)

print("✅ Model loaded from local cache")

# Load LoRA adapter - WITH ERROR HANDLING
try:
    lora_state = sf.load_file(MODEL_PATH)
    set_peft_model_state_dict(pipe.unet, lora_state, adapter_name="default")
    print("✅ LoRA adapter loaded successfully.")
except FileNotFoundError:
    logger.warning(f"LoRA adapter not found at {MODEL_PATH}. Proceeding with the base model only.")
    print("⚠️ LoRA adapter not found. Proceeding with base model.")
except Exception as e:
    logger.error(f"Error loading LoRA adapter: {e}")
    print(f"⚠️ An error occurred with the LoRA adapter: {e}. Proceeding with base model.")

def generate_dress_image(prompt, negative_prompt="", seed=42):
    g = torch.Generator(device=_device).manual_seed(seed)
    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        guidance_scale=7.5,
        num_inference_steps=25,
        generator=g,
        height=512, width=512,
    ).images[0]
    return image

BODY_RULES = {
    "hourglass": "cinched waist, structured bodice, balanced skirt",
    "pear": "A-line skirt, embellished bodice, cap sleeves",
    "apple": "empire waist, flowy skirt, deep V neckline",
    "rectangle": "ruffled skirt, sweetheart neckline, defined waist",
    "inverted_triangle": "ballgown skirt, off-the-shoulder neckline",
}

def build_prompt(body_type, sleeve, neckline, bodice, skirt, train, structure):
    base = BODY_RULES.get(body_type, "")
    prompt = f"elegant white wedding dress, {sleeve}, {neckline}, {bodice}, {skirt}, {train}, {structure}, {base}, high-quality fabric, realistic, studio lighting"
    negative = "low quality, blurry, deformed, bad anatomy, text, watermark"
    return prompt, negative
import torch
import os
from pathlib import Path
from diffusers.utils import load_image
from PIL import Image
import numpy as np

from diffusers import (
    StableDiffusionPipeline,    
    ControlNetModel,
    StableDiffusionControlNetPipeline,
    DPMSolverMultistepScheduler,
)
def load_pipe():
    controlnet = ControlNetModel.from_pretrained("control_v11e_sd15_ip2p", torch_dtype=torch.float16).to("cuda")                                                                                                                                                                             
    pipe = StableDiffusionControlNetPipeline.from_pretrained(
        "realistic-vision-v51", controlnet=controlnet, torch_dtype=torch.float16
    ).to("cuda")
    return pipe

def generate(pipe, img_path, weather):

    image = Image.open(img_path)
    # image = image.resize((512, 1024))
    # print(image.size)

    prompt = f"make it on {weather}"
    neg = "lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, username, watermark, signature"

    generator = torch.manual_seed(42)
    scheduler = DPMSolverMultistepScheduler(use_karras_sigmas = True)

    image = pipe(prompt,negative_prompt=neg, 
                height=1024, width=2048, 
                num_inference_steps=25, 
                generator=generator, 
                scheduler=scheduler, 
                image=image,
                guidance_scale = 5).images[0]
    # image = image.resize((2048,1024))
    return image        


if __name__ == "__main__":
    img_path = '/workspace/model1.jpg'
    weather = "night"
    pipe = load_pipe()
    img = generate(pipe, img_path, weather)    
    img.save("out.png")                                                                                                                                                           


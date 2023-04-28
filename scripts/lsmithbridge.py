import os
import random
import sys
import requests
import json
import gradio as gr

from modules import scripts, script_callbacks, shared
from modules.processing import Processed, create_infotext
from PIL import Image, ImageDraw
from io import BytesIO
import base64

default_url = "http://localhost:8000/api/images"

class LSmithBridgeScript(scripts.Script):
    def title(self):
        return "Lsmith Bridge"

    def show(self, is_img2img):
        return not is_img2img

    def ui(self, is_img2img):
        with gr.Row():
            lsmith_url = gr.Textbox(label='Lsmith URL', value=default_url)

        return [lsmith_url]

    def run(self, p, url):
        print("Lsmith Bridge")

        postdata = {
            "prompt":p.prompt,
            "negative_prompt":p.negative_prompt,
            "batch_size":p.batch_size,
            "batch_count":p.n_iter,
            "scheduler_id":"euler_a",
            "steps":p.steps, 
            "scale":p.cfg_scale,
            "image_width":p.width, 
            "image_height":p.height, 
            "seed":p.seed, 
        }
        print(json.dumps(postdata))

        headers = {'Content-Type': 'application/json'}

        response = requests.post(url+"/generate", data=json.dumps(postdata), headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to merge images, status code: {response.status_code}")

        result = json.loads(response.text)
        images = []
        for res in result["data"]["images"].keys():
            image = Image.open(BytesIO(base64.b64decode(res)))
            images.append(image)
        return Processed(p, images)

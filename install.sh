#!bin/bash

pip install requirements.txt
git lfs install
git clone https://huggingface.co/stablediffusionapi/realistic-vision-v51
git clone https://huggingface.co/lllyasviel/control_v11e_sd15_ip2p
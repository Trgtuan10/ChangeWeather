import os
from change import generate, load_pipe
import argparse

def make_folder(weather):
    os.makedirs(weather, exist_ok=True)
    for dir in ["test", "train", "val"]:
        os.makedirs(os.path.join(weather, dir), exist_ok=True)
        for destination in os.listdir(os.path.join(weather, dir)):
            os.makedirs(os.path.join(weather, dir, destination), exist_ok=True)


def gen(weather):
    pipe = load_pipe()
    image_dir = "leftImg8bit"
    for dir in ["test", "train", "val"]:
        for destination in os.listdir(os.path.join(image_dir, dir)):
            for img in os.listdir(os.path.join(image_dir, dir, destination)):
                img_path = os.path.join(image_dir, dir, destination, img)
                image = generate(pipe, img_path, weather)
                image.save(os.path.join(weather, dir, destination, img))


if __name__ == "__main__":
    #weather is a arg when run python main.py --weather
    parser = argparse.ArgumentParser()
    parser.add_argument("--weather", type=str, default="rainy",
                        help = "weather to change")
    args = parser.parse_args()
    make_folder(args.weather)
    gen(args.weather)
                
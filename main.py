import os
from change import generate

weather = ["sunny", "night"]
image_dir = "leftImg8bit"

for w in weather:
    os.makedirs(w, exist_ok=True)
    for dir in ["test", "train", "val"]:
        os.makedirs(os.path.join(w, dir), exist_ok=True)
        for destination in os.listdir(os.path.join(image_dir, dir)):
            os.makedirs(os.path.join(w, dir, destination), exist_ok=True)
            for img in os.listdir(os.path.join(image_dir, dir, destination)):
                img_path = os.path.join(image_dir, dir, destination, img)
                image = generate(img_path, w)
                image.save(os.path.join(w, dir, destination, img))
                    # print(os.path.join(w, dir, destination, img))
                
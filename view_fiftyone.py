import fiftyone as fo
import os

# Specify the parent directory containing all your image subfolders
parent_directory = "snow"

# Create a dataset
dataset = fo.Dataset("images_dataset")

# Recursively add all images in the parent directory to the dataset
for root, _, files in os.walk(parent_directory):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            file_path = os.path.join(root, file)
            sample = fo.Sample(filepath=file_path)
            dataset.add_sample(sample)

# Launch the FiftyOne app
session = fo.launch_app(dataset)
session.wait()

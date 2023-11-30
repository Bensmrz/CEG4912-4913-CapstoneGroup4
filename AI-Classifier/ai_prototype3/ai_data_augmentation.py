import os
import Augmentor

def augment_images(input_folder, output_folder, augmentation_count):
    # Create an Augmentor pipeline
    pipeline = Augmentor.Pipeline(input_folder, output_folder)

    # Define the augmentation operations you want to apply
    pipeline.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    pipeline.flip_left_right(probability=0.5)
    pipeline.zoom_random(probability=0.5, percentage_area=0.8)
    pipeline.flip_top_bottom(probability=0.5)

    # Execute the augmentation pipeline
    pipeline.sample(augmentation_count)

if __name__ == "__main__":
    # Specify the number of augmentations you want per image
    augmentation_count = 1

    # Iterate through subfolders and apply data augmentation
    root_img_path = "./photos"
    subfolders = ["A", "B", "C", "NO_SIGN"]

    for folder in subfolders:
        #if folder != None:
        if folder == "C":
            subfolder_path = os.path.join(root_img_path, folder)
            augment_images(subfolder_path, ".", augmentation_count)
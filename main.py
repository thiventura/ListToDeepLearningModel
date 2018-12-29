from google_images_download import google_images_download
import Augmentor
import os.path

# Download images
response = google_images_download.googleimagesdownload()

keywords = "pokemon charmander 3d"
limit = 2
format_image = "jpg"
color_type = "full-color"
size = "large"
offset = 1
print_urls = True
output_directory = os.path.join("dataset", "download")
image_directory = "charmander-3d"

#creating list of arguments
arguments = {
    "keywords": keywords,
    "limit": limit,
    "format": format_image,
    "color_type": color_type,
    "size": size,
    "offset": offset,
    "print_urls": print_urls,
    "output_directory": output_directory,
    "image_directory": image_directory
}

paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images


# Data augmentation
p = Augmentor.Pipeline(
    os.path.join(output_directory, image_directory),
    os.path.join("..", "..", "augmented", image_directory) )

p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
p.sample(10)
p.process()
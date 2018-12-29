from google_images_download import google_images_download
import Augmentor
import os.path


DOWNLOAD_QUANTITY_PER_CLASS = 2
AUGMENTATION_QUANTITY_IMAGES = 10
output_directory = os.path.join("dataset", "download")


# Load classes from CSV
classesFileName = os.path.join("samples", "pokemon.csv")
classesFile = open(classesFileName, "r")
for classData in classesFile:
    className, classKeywords = classData.split(",")

    # Download images
    response = google_images_download.googleimagesdownload()
    offset = 1
    arguments = {
        "keywords": classKeywords,
        "limit": DOWNLOAD_QUANTITY_PER_CLASS,
        "format": "jpg",
        "color_type": "full-color",
        "size": "large",
        "offset": offset,
        "print_urls": True,
        "output_directory": output_directory,
        "image_directory": className
    }
    response.download(arguments)

    # Data augmentation
    p = Augmentor.Pipeline(
        os.path.join(output_directory, className),
        os.path.join("..", "..", "augmented", className) )
    p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
    p.sample(AUGMENTATION_QUANTITY_IMAGES)
    p.process()
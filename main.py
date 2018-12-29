from google_images_download import google_images_download
import Augmentor
from retrain import retrain
import os.path


DOWNLOAD_QUANTITY_PER_CLASS = 50
AUGMENTATION_QUANTITY_IMAGES = 200
output_directory = os.path.join("dataset", "download")


# Load classes from CSV and creating dataset
classesFileName = os.path.join("samples", "pokemon151.csv")
classesFile = open(classesFileName, "r")
for classData in classesFile:
    className, classKeywords = classData.split(",")
    classFolder = os.path.join(output_directory, className)
    
    # Check how many images already were downloaded for this class
    # This will be useful if some error occured in previous execution
    try:
        imagesDownloaded = len([name for name in os.listdir(classFolder) if os.path.isfile(os.path.join(classFolder, name))])
    except:
        imagesDownloaded = 1

    # Download images
    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": classKeywords,
        "limit": DOWNLOAD_QUANTITY_PER_CLASS,
        "format": "jpg",
        "color_type": "full-color",
        "size": "large",
        "offset": imagesDownloaded,
        "print_urls": True,
        "output_directory": output_directory,
        "image_directory": className
    }
    response.download(arguments)

    # Check how many images already were augmented for this class
    # This will be useful if some error occured in previous execution
    classFolderAugmentation = os.path.join("dataset", "augmented", className)
    try:
        imagesAugmented = len([name for name in os.listdir(classFolderAugmentation) if os.path.isfile(os.path.join(classFolderAugmentation, name))])
    except:
        imagesAugmented = 0

    if imagesAugmented < AUGMENTATION_QUANTITY_IMAGES:
        # Data augmentation
        p = Augmentor.Pipeline(
                classFolder, 
                os.path.join("..", "..", "augmented", className))
        p.rotate(probability=0.7, max_left_rotation=25, max_right_rotation=25)
        p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
        p.crop_random(probability=0.7, percentage_area=0.8)  
        p.flip_left_right(probability=0.5)
        p.resize(probability=1.0, width=300, height=300)
        p.sample(AUGMENTATION_QUANTITY_IMAGES - imagesAugmented)
        p.process()


# Training model
retrain()
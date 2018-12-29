from google_images_download import google_images_download

# Download images
response = google_images_download.googleimagesdownload()

keywords = "pokemon charmander 3d"
limit = 2
format_image = "jpg"
color_type = "full-color"
size = "large"
offset = 1
print_urls = True
output_directory = "dataset"

#creating list of arguments
arguments = {
    "keywords": keywords,
    "limit": limit,
    "format": format_image,
    "color_type": color_type,
    "size": size,
    "offset": offset,
    "print_urls": print_urls,
    "output_directory": output_directory
}

paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images

# Creation of a image dataset and its deep learning model

## Summary
The ideia of this script is automatically to create a dataset and training the new model. Based on a list of classes and its keywords, the script will download several images from internet, perform data augmentation and training the model.

## Setting your classes and keywords
You just need to define one text file to create your deep learning model. A sample of this kind of file is in `samples` folder. You have to put one line for each class of your model. In each line you have to put the class name and keywords for this class. The script will use Google Images to query images for your class. 

## Run
Download the repository, unzip the file downloaded, and go to the directory. Then you can use the following command:

    $ python main.py --classes samples/pokemon151.csv

This command will read the sample file, download some images for each class, perform data augmentation generating more images and finally training a new model using transfer learning.

If you wish you can define how many images will be downloaded for each class, how many images will be generated by data augmentation, and others parameters. Type `--help` to see more details.

## Testing
You can test your new model with `label_image.py`:

    $ python label_image.py --image path/image.jpg

## Acknowledgements
[Google Images Download](https://github.com/hardikvasa/google-images-download)

[Augmentor](https://github.com/mdbloice/Augmentor)

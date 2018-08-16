# image_datasets

Provide easy access to images in a dataset. For now support classification and segmentation datasets.
The lib assumes the following structure for the dataset files (explained below). 

## Directory structures
* For segmentation: 
 * `IMAGE_FOLDER/[SET_FOLDER/]/INPUT_DIR/FILENAME`

## Classification datasets

Files should be organized as follows: `IMAGE_FOLDER/[SET_FOLDER/]CLASS_FOLDER/IMAGE_FILENAME` 

### Constructor

Parameters:

* `image_folder`: path to the dataset root folder
* `dirs`: list of of fold directories (`None` if the dataset is not splitted)
* `classes`: list of classes (if `None`, auto-detected from the folder structure)
* `encode_classes`: `True` for encoding classes as numbers in `{0, ..., n_class}`, `False` to keep folder names

```python
dataset = ImageClassificationDataset("~/my_dataset", dirs=["train", "test"])
dataset = ImageClassificationDataset("~/my_dataset", dirs=["train", "test"], classes=[5562, 23178], encode_classes=True)
```

### Method `all`

Returns the list of image filenames and classes (optionally for a given fold). 

Parameters:

* `dirs`: names of the folds of which the images information must be extracted (None, for taking images from all folds)
* `classes`: a subset of classes to select (`None` for all classes)
* `positive`: a subset of classes to consider as positive (`None` for keeping it multiclass)
* `negative`: a subset of classes to consider as negative (`None` for keeping it multiclass)
* `one_hot`: true for a one-hot encoding of the classes

```python
dataset = ImageClassificationDataset("~/my_dataset", dirs=["train", "test"])
x_train, y_train = dataset.all(dirs=["train"], one_hot=False)

# x_train is a list of strings containing the filenames
# y_train is the list of classes as integers 
```

### Method `batch`

Return a random batch of images and their classes. 

Parameters:

* `size`: size of the batch
* `dirs`: see method `all`
* `replace`: `True` for sampling with replacement
* `random_state`: a random state 
* `classes`: see method `all`
* `positive`: see method `all`
* `negative`: see method `all`
* `one_hot`: see method `all`

```python
dataset = ImageClassificationDataset("~/my_dataset", dirs=["train", "test"])
x_batch, y_batch = dataset.batch(12, dirs=["train"], one_hot=False)

# x_batch is a list of 12 strings containing the filenames of the batch
# y_batch is the list of classes as integers 
```

## Segmentation dataset

TODO

## Other 

Other utilities functions provided by the library.

### Function `ImageDataset.load_images`

Load all images from a list of filepaths into memory. Return them as a list. 

Parameters

* `files`: list of filepaths of the file to open
* `open_fn`: the function to use to open the images. By default, try to import OpenCV's `imread`. 

```python
dataset = ImageClassificationDataset("~/my_dataset", dirs=["train", "test"])
x_train, y_train = dataset.all(dirs=["train"], one_hot=False)
images_train = ImageDataset.load_images(x_train)
```

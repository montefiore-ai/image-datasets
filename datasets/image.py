from PIL import Image as pil_image


def load_crop_img(path, load_size, crop_size, grayscale=False, random=True, random_state=None):
    """Loads an image into PIL format and crop it at a given size.
    # Arguments
        path: Path to image file
        load_size: int or (int, int),
            If integer, size the smallest side should be resized to. Otherwise the (height, width) to which the
            image should be resized to
        crop_size: int or (int, int),
            Size of the random square crop to be taken in the image (should be less then or equal to load_size)
            If a tuple is given the random crop is a rectangle of given (height, width)
        grayscale: Boolean, whether to load the image as grayscale.
    # Returns
        A PIL Image instance.
    # Raises
        ImportError: if PIL is not available.
    """
    random_state = check_random_state(random_state)
    if pil_image is None:
        raise ImportError('Could not import PIL.Image. '
                          'The use of `array_to_img` requires PIL.')
    img = pil_image.open(path)
    if grayscale:
        if img.mode != 'L':
            img = img.convert('L')
    else:
        if img.mode != 'RGB':
            img = img.convert('RGB')

    # load resize
    width, height = img.size
    if isinstance(load_size, tuple):
        new_height, new_width = load_size
    elif height < width:
        ratio = float(load_size) / height
        new_width, new_height = int(floor(ratio * width)), load_size
    elif width < height:
        ratio = float(load_size) / width
        new_width, new_height = load_size, int(floor(ratio * height))
    else:
        new_height, new_width = load_size, load_size

    img = img.resize((new_width, new_height))

    # (random) crop resize
    if isinstance(crop_size, tuple):
        crop_size_h, crop_size_w = crop_size
    else:
        crop_size_h, crop_size_w = crop_size, crop_size
    width, height = img.size
    len_crop_h, len_crop_w = height - crop_size_h, width - crop_size_w
    if random:
        offset_h = random_state.randint(len_crop_h + 1)
        offset_w = random_state.randint(len_crop_w + 1)
    else:
        offset_h = int(len_crop_h / 2)
        offset_w = int(len_crop_w / 2)
    return img.crop((offset_w, offset_h, offset_w + crop_size_w, offset_h + crop_size_h))

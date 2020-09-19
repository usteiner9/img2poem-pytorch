# File: poetic.py
# Creation: Saturday September 19th 2020
# Author: Arthur Dujardin
# Contact: arthur.dujardin@ensg.eu
#          arthurd@ifi.uio.no
# --------
# Copyright (c) 2020 Arthur Dujardin


# Basic imports
import random

# img2poem package
from .poem import PoemMultiMDatasetMasks


class PoeticEmbeddedDataset(PoemMultiMDatasetMasks):
    """Dataset used to embed poectiness from paired images and poems.
    Usually, this dataset is used with ``PoeticEmbedder`` model.

    * :attr:`id` (int): Identifier of the image & poem pair.

    * :attr:`tokens` (torch.tensor): Tokenized ids of a poem.

    * :attr:`masks` (torch.tensor): Tokenized ids masked.

    * :attr:`image` (torch.tensor): Matrix of the image in RGB format.

    .. note::
        The default filename used to process the data is called ``multim_poem.json``.
        The ``image_dir`` argument is used the location of the downloaded images.

    .. note::
        Download the images from the csv file with the ``download`` method.

    """

    def __init__(self, filename, image_dir, tokenizer=None, max_seq_len=256, transform=None):
        super(PoeticEmbeddedDataset, self).__init__(filename, image_dir, tokenizer=tokenizer, max_seq_len=max_seq_len, transform=transform)

    def __len__(self):
        return len(self.tokens)

    def __getitem__(self, index):

        index2 = random.randrange(len(self.tokens))
        while index2 == index:
            index2 = random.randrange(len(self.tokens))

        id1 = self.ids[index]
        id2 = self.ids[index2]
        poem1 = self.tokens[index]
        poem2 = self.tokens[index2]
        mask1 = self.masks[index]
        mask2 = self.masks[index2]
        image1 = self.images[index]
        image2 = self.images[index2]
        return id1, poem1, mask1, image1, id2, poem2, mask2, image2

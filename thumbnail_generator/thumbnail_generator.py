#!/usr/bin/env python3

# futures module provides a couple of diff executors to run operations in parallel;
# one for using threads and another for using processes.
from concurrent import futures

import argparse
import logging
import os
import sys

import PIL
import PIL.Image

from tqdm import tqdm


def process_options():
    kwargs = {
        'format': '[%(levelname)s] %(message)s',
    }
    parser = argparse.ArgumentParser(
        description='Thumbnail generator',
        fromfile_prefix_chars='@'
    )
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-q', '--quiet', action='store_true')

    options = parser.parse_args()

    if options.debug:
        kwargs['level'] = logging.DEBUG
    elif options.verbose:
        kwargs['level'] = logging.INFO
    elif options.quiet:
        kwargs['level'] = logging.WARN

    logging.basicConfig(**kwargs)

    return options


def process_file(root, basename):
    filename = f'{root}/{basename}'
    image = PIL.Image.open(filename)

    size = (128, 128)
    image.thumbnail(size)

    new_name = f'thumbnails/{basename}'
    image.save(new_name, 'JPEG')
    return new_name


def progress_bar(files):
    return tqdm(files, desc='Processing', total=len(files), dynamic_ncols=True)


def main():
    process_options()

    # Create the thumbnails directory
    if not os.path.exists('thumbnails'):
        os.mkdir('thumbnails')
    # to be able to run things in parallel, we create an executor
    # (process that's in charge of distributing the work among the diff workers.)
    # example one
    # executor = futures.ThreadPoolExecutor()

    # example two
    # by changing to ProcessPoolExecutor() we tell the futures module that we want to use processes instead of threads.
    executor = futures.ProcessPoolExecutor()
    for root, _, files in os.walk('images'):
        for basename in progress_bar(files):
            if not basename.endswith('.jpg'):
                continue
            executor.submit(process_file, root, basename)
    print('Waiting for all threads to finish.')
    # this function waits until all the workers in the pool are done, and only then shuts down the executor.
    executor.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit((main()))

import os
# import cv2
# import time
import argparse
# import numpy as np

def path_check(path, name):
    assert os.path.exists(path), 'invalid {} path: {}'.format(name, path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--labels', type=str, default='',
                        help='Path to coco labels')
    parser.add_argument('--out', type=str, default='out',
                        help='Path to output dir')
    opt = parser.parse_args()

    # path_check(opt.coco, 'coco')
    
    # coco_images = os.path.join(opt.coco, 'images')
    # coco_labels = os.path.join(opt.coco, 'labels')
    
    # coco_images_val = os.path.join(coco_images,     'val2017')
    # coco_images_train = os.path.join(coco_images,   'train2017')
    # coco_labels_val = os.path.join(coco_labels,     'val2017')
    # coco_labels_train = os.path.join(coco_labels,   'train2017')
    
    # path_check(coco_images_val  , 'val2017')
    # path_check(coco_images_train, 'train2017')
    # path_check(coco_labels_val  , 'val2017')
    # path_check(coco_labels_train, 'train2017')
    
    path_check(opt.labels, 'labels')
    
    try:
        os.makedirs(opt.out)
    except:
        pass
    
    labels = [os.path.join(opt.labels, f) for f in next(os.walk(opt.labels))[2]]
    
    for label in labels:
        f = open(label, 'rt')
        filename = os.path.split(label)[1]
        out = open(os.path.join(opt.out, filename), 'wt')
        for line in f:
            if line.split(' ')[0] == '0':
                out.write(line)
        out.close()
        f.close()



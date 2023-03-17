# coco convert tools

## Category filter

Pick out some categories from coco dataset.

It runs through labels and picks out categories as command.  
(Maybe just *one* category, but you get the idea)

### Usage

```bash
python filter.py --labels /path/to/coco/labels/val2017  --out /path/to/coco-filtered/labels/val2017
```

## Dataset split

To use just part of the whole dataset.

It runs through image list and picks randomly.

### Usage

40% of coco2017 train

```bash
python split.py --txt /path/to/coco/train2017.txt --ratio=0.4 --out /path/to/coco/train2017-0.4.txt
```

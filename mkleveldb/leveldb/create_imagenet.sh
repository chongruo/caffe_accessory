#!/usr/bin/env sh
# Create the imagenet leveldb inputs
# N.B. set the path to the imagenet train + val data dirs

TOOLS=/home/chongruo/mywork/caffe/build/tools
DATA=/scratch/jiadeng_fluxg/chongruo/raw_render/render_z20000_256_first

TRAIN_DATA_ROOT=$DATA/train/
VAL_DATA_ROOT=$DATA/val/

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=false
if $RESIZE; then
  RESIZE_HEIGHT=256
  RESIZE_WIDTH=256
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet training data is stored."
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet validation data is stored."
  exit 1
fi

echo "Creating train leveldb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset.bin \
    $TRAIN_DATA_ROOT \
    $DATA/train.txt \
    ilsvrc12_train_leveldb 1 \
    # $RESIZE_HEIGHT $RESIZE_WIDTH

echo "Creating val leveldb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset.bin \
    $VAL_DATA_ROOT \
    $DATA/val.txt \
    ilsvrc12_val_leveldb 1 \
    # $RESIZE_HEIGHT $RESIZE_WIDTH

echo "Done."

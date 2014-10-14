# for create_imagenet.sh
data=/scratch/jiadeng_fluxg/chongruo/raw_render/render_z20000_128_first
train_image_root=$data/train_image/
val_image_root=$data/val_image/

name_root=render_z20000_128_first_1
train_image_output=${name_root}_train_image/
val_image_output=${name_root}_val_image/

# for calculating mean
mean_output=${name_root}_mean.binaryproto

# for create_imagenet_normal.sh
train_normal_root=$data/train_normal/
val_normal_root=$data/val_normal/
train_normal_output=${name_root}_train_normal/
val_normal_output=${name_root}_val_normal/


echo "create_imagenet.sh"
sh create_imagenet.sh $data $train_image_root $val_image_root $train_image_output $val_image_output

echo "make_iamgenet_mean.sh"
sh make_imagenet_mean.sh $train_image_output $mean_output

echo "create_imagenet_normal.sh"
sh create_imagenet_normal.sh $data $train_normal_root $val_normal_root $train_normal_output $val_normal_output  



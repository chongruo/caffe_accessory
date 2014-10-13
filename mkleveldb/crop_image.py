## crop the image from 256 to 128, crop image and normal using same boundary box
## Oct 11,2014

from PIL import Image as io
from random import randint
import os,shutil
import multiprocessing as mulpool

width,height = 128,128
root = '/scratch/jiadeng_fluxg/chongruo/raw_render/render_big'
ori_dir = 'image'
ori_normal_dir = 'normal'
dest_dir = 'image_128' 
dest_normal_dir = 'normal_128'

def crop_image(dir):
	print '--------',dir,'----------'
	ori_abs_path = os.path.join(root,dest_dir,dir)
	ori_normal_abs_path = os.path.join(root,dest_normal_dir,dir)
	
	if os.path.exists(ori_abs_path):
		shutil.rmtree(ori_abs_path)
		shutil.rmtree(ori_normal_abs_path)
	os.mkdir(ori_abs_path)
	os.mkdir(ori_normal_abs_path)
	
	ori_dir_path = os.path.join(root,ori_dir,dir)
	image_list = [dummy for dummy in os.listdir(ori_dir_path)]

	for index, ori_img in enumerate(image_list):
		if index%100==0:
			print 'process: ',dir,' ',str(index)+'/'+str(len(image_list))
		a,b = randint(0,127),randint(0,127)

		img = io.open(os.path.join(root,ori_dir,dir,ori_img))
		newimg = img.crop((a,b,a+128,b+128))
		dest_path = os.path.join(root,dest_dir,dir,ori_img)
		newimg.save(dest_path)

		temp = ori_img.split('_')
		temp = ['normal','z']+temp
		ori_normal_img = ('_').join(temp)
		normal_img = io.open(os.path.join(root,ori_normal_dir,dir,ori_normal_img))
		newnormal_img = normal_img.crop((a,b,a+128,b+128))
		dest_normal_path = os.path.join(root,dest_normal_dir,dir,ori_normal_img)
		newimg.save(dest_normal_path)

if __name__=="__main__":
	dir_list = os.listdir(os.path.join(root,ori_dir))
	print 'len(dir_list) ',len(dir_list)

	if os.path.exists(os.path.join(root,dest_dir)):
		shutil.rmtree(os.path.join(root,dest_dir))
		shutil.rmtree(os.path.join(root,dest_normal_dir))
	os.mkdir(os.path.join(root,dest_dir))
	os.mkdir(os.path.join(root,dest_normal_dir))
	print 'mkdir',dest_dir

	#crop_image('r0')
	pool = mulpool.Pool()
	pool.map(crop_image, dir_list)
	pool.close()
	pool.join()


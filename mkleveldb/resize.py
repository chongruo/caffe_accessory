# should modify: root, ori_dir, dest_dir

from PIL import Image as io
import traceback
import os,shutil
import multiprocessing as mulpool

width,height = 256,256
root = '/scratch/jiadeng_fluxg/chongruo/raw_render/render_big'
ori_dir = 'image'
dest_dir = 'new_render_256'

try:
	def Dirresize(dir):
		print '-----',dir,'---'
		os.mkdir(os.path.join(root,dest_dir,dir))
		
		ori_dir_path = os.path.join(root,ori_dir,dir)
		image_list = [dummy for dummy in os.listdir(ori_dir_path)]

		for index,ori_img in enumerate(image_list):
			if index%100==0:
				print 'process: ',dir,' ', str(index)+'/'+str(len(image_list))
		    
			try:
				img = io.open(os.path.join(root,ori_dir,dir,ori_img))
				w,h = img.size
				newing = img.resize((width,height),io.ANTIALIAS)
				dest_path = os.path.join(root,dest_dir,dir,ori_img)
				newing.save(dest_path)
			except IOError:
				print 'cant open: ',os.path.join(ori_dir,dir,ori_img)
				continue
			except IndexError:
				print 'cant open: ',os.path.join(ori_dir,dir,ori_img)
				continue
			except:
				print 'cant open: ',os.path.join(ori_dir,dir,ori_img)
				continue

except:
	traceback.print_exc()


if __name__=="__main__":
	dir_list = os.listdir(os.path.join(root,ori_dir))
	print 'len(dir_list) ',len(dir_list)
	
	if os.path.exists(os.path.join(root,dest_dir)):
		shutil.rmtree(os.path.join(root,dest_dir))
	os.mkdir(os.path.join(root,dest_dir))
	print 'mkdir ',dest_dir

	pool = mulpool.Pool()
	pool.map(Dirresize,dir_list)
	pool.close()
  	pool.join()

	#for dir in dir_list:
	#	Dirresize(dir)
 	

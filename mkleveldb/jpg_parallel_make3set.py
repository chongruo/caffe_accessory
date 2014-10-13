## split images into train/test/val as well as .txt
## the result will be in the dest_dir in the same path
## Oct 6,2014

import multiprocessing as mulpool
import os,shutil,random 

root = '/scratch/jiadeng_fluxg/chongruo/raw_render/render_z10000'
ori_dir = 'render_z10000_256'
dest_dir = 'render_z10000_256_first'

dir_dic = {}
dir_list =  os.listdir(os.path.join(root,ori_dir))
dir_list = sorted(dir_list)
print 'len(dir_list):',len(dir_list)
for index,dir in enumerate(dir_list):
	 dir_dic[dir] = index
	

def setDir(dir):
	print '-----',dir,'------'
	index = dir_dic[dir]
	for temp in ('train','test','val'):
		if os.path.exists(os.path.join(root,dest_dir,temp,dir)):
			shutil.rmtree(os.path.join(root,dest_dir,temp,dir))
		os.mkdir(os.path.join(root,dest_dir,temp,dir))

	ori_dir_abspath = os.path.join(root,ori_dir,dir)
	image_list = [dummy for dummy in os.listdir(ori_dir_abspath)]
	
	image_len = len(image_list)
	if image_len < 10:
		print dir,'---------Dir Pass, size is small-----'
		return
	image_len = (image_len/10)*10

	a = (image_len/10)*6
	b = (image_len/10)*1
	l = range(image_len)
	random.shuffle(l)
	ltrain = l[0:a]
	lval = l[a:a+b]
	ltest = l[a+b:image_len]

 	for i in range(image_len):
		img_oripath = os.path.join(ori_dir_abspath,image_list[i])
		if i in ltrain:
			img_destpath = os.path.join(root,dest_dir,'train',dir,image_list[i])
			shutil.copyfile(img_oripath,img_destpath)
			temp = os.path.join(dir,image_list[i])+' '+str(index)+'\n'
			with open(os.path.join(root,dest_dir,'train.txt'),'a') as train_txt:
				train_txt.write(temp)
		elif i in lval:
			img_destpath = os.path.join(root,dest_dir,'val',dir,image_list[i])
			shutil.copyfile(img_oripath,img_destpath)
			temp = os.path.join(dir,image_list[i])+' '+str(index)+'\n'
			with open(os.path.join(root,dest_dir,'val.txt'),'a') as val_txt:
				val_txt.write(temp)
		elif i in ltest:
			img_destpath = os.path.join(root,dest_dir,'test',dir,image_list[i])
			shutil.copyfile(img_oripath,img_destpath)
			temp = os.path.join(dir,image_list[i])+' '+str(0)+'\n'
			with open(os.path.join(root,dest_dir,'test.txt'),'a') as test_txt:
				test_txt.write(temp)
	print '---------',dir,'finish------'
			

if __name__=='__main__':
	if os.path.exists(os.path.join(root,dest_dir)):
		shutil.rmtree(os.path.join(root,dest_dir))
	os.mkdir(os.path.join(root,dest_dir))

	for file in ('train','test','val'):
		path = os.path.join(root,dest_dir,file)
		if os.path.exists(path):
			shutil.rmtree(path)
			print 'rm ',file
		os.mkdir(path)
		print 'mkdir  ',file

		path = os.path.join(root,dest_dir,file+'.txt')
		if os.path.exists(path):
			os.remove(path)
			print 'rmtxt ',file

	pool = mulpool.Pool()
	pool.map(setDir,dir_list)
	pool.close()
	pool.join()





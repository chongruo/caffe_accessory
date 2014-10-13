## create normal map for dir
## the dir includes 10 directories
## Oct 6,2014

from PIL import Image as io
import os
import multiprocessing as mulpool

origin_dir = '/afs/umich.edu/user/c/h/chongruo/Desktop/image_test'
dest_dir = ''

def normalmap(dir):
	images = os.listdir(dir)

	for index,img_name in enumerate(images):
		if index%100==0:
			print dir+':',index	

		img_abs = os.path.join(origin_dir,dir,img_name)  
		img = io.open(img_abs)
		img = img.split()[0]
		m,n = img.size
		pixelimg = img.load()
		for i in range(1,m):
			for j in range(1,n):
				pixelimg[i,j] = 256 - pixelimg[i,j]

		nimg = io.new('RGB',img.size,'white')
		pixelnew = nimg.load()

		for i in range(1,m-1):
			for j in range(1,n-1):
				temp1 = (img.getpixel((i-1,j)) - img.getpixel((i+1,j))) * (1.0)
				temp2 = (img.getpixel((i,j+1)) - img.getpixel((i,j-1))) * (1.0)
				temp = [temp1,temp2,2.0/256]
				summ = sum( map((lambda x:x**2), temp) )
				temp = [element/summ for element in temp]
				temp = [int((element+1)*128) for element in temp]	
				pixelnew[i,j] = tuple( temp )

		temp = file.split('_')
		temp[0] = 'normal'
		dest_img_name = '_'.join(temp)

		dest_img_path = os.path.join(dest_dir,dir,dest_img_name)
		nimg.save(dest_img_path)
				
if __name__=='__main__':
	dirs = os.listdir(origin_dir)
	
	pool = mulpool.Pool()
	pool.map(normalmap,dirs)
	pool.close()
	pool.join()





	

		

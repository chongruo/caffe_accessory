import caffe
import matplotlib.pyplot as plt
import numpy as np

def vis_square(data,padsize=1,padval=0):
	data -= data.min()
	data /= data.max()
	
	n = int(np.ceil(np.sqrt(data.shape[0])))
	padding = ((0,n**2 - data.shape[0]),(0,padsize),(0,padsize))+((0,0),)*(data.ndim -3 )
	data = np.pad(data,padding,mode='constant',constant_values=(padval,padval))

	data = data.reshape((n,n)+data.shape[1:]).transpose((0,2,1,3)+tuple(range(4,data.ndim+1)))
	data = data.reshape((n*data.shape[1], n*data.shape[3])+data.shape[4:])
	
	plt.imshow(data)
	plt.savefig('vis_conv[2].png')

root = '/home/chongruo/mywork/myexp/osf/exps/exp10/'
deploy_file = 'fmd_deploy.prototxt'
model = 'caffe_imagenet_train_iter_2500'

net = caffe.Classifier(root+deploy_file,root+model)
net.set_phase_test() 
net.set_mode_gpu()

filters = net.params['conv2'][0].data
vis_square(filters[:48].reshape(48**2,9,9))



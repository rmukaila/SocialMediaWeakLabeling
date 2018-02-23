caffe_root = '../../caffe-master/'  # this file should be run from {caffe_root}/examples (otherwise change this line)

import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
from create_solver import create_solver
from do_solve import do_solve
from pylab import *
import os


caffe.set_device(0)
caffe.set_mode_gpu()

weights = '../../../datasets/SocialMedia/models/pretrained/bvlc_googlenet.caffemodel'
assert os.path.exists(weights)

niter = 500000
base_lr = 0.001 #Starting from 0.01 (from quick solver) -- Working 0.001
display_interval = 400 #200

batch_size = 120 #Only used to print here

#number of validating images  is  test_iters * batchSize
test_interval = 1600 #1000
test_iters = 100 #100

#Name for training plot and snapshots
training_id = 'SocialMedia_contrastive_perWord_glove_m01'

#Set solver configuration
solver_filename = create_solver('prototxt/train_val_SM_peroWord_glove.prototxt', 'prototxt/train_val_SM_peroWord_glove.prototxt', training_id, base_lr=base_lr)
#Load solver
solver = caffe.get_solver(solver_filename)

#Copy init weights
solver.net.copy_from(weights)

#Restore solverstate
#solver.restore('../../../datasets/SocialMedia/models/CNNRegression/instagram_cities_1M_Inception_frozen_500_chunck_iter_280000.solverstate')


print 'Running solvers for %d iterations...' % niter
solvers = [('my_solver', solver)]
_, _, _ = do_solve(niter, solvers, display_interval, test_interval, test_iters, training_id, batch_size)
print 'Done.'


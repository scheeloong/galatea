jobdispatch --torque --env=THEANO_FLAGS=device=gpu,floatX=float32,force_device=True --duree=48:00:00 --whitespace --gpu train.py $G/dbm/inpaint/expdir/mnist_sup_inpaint_U5"{{A,B,C,D,E,F,G,H,I}}".yaml

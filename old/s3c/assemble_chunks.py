import numpy as np

chunks = [ 'chunk_%d.npy' % i for i in xrange(50) ]

print 'loading first chunk'
first_chunk = np.load(chunks[0])

final_shape = list(first_chunk.shape)

final_shape[0] = 50000

print 'making output'
X = np.zeros(final_shape,dtype='float32')

idx = first_chunk.shape[0]

X[0:idx,:] = first_chunk

for i in xrange(1, len(chunks)):

    print i, idx
    arg = chunks[i]

    chunk = np.load(arg)

    chunk_span = chunk.shape[0]

    X[idx:idx+chunk_span,...] = chunk

    idx += chunk_span
assert idx == 50000



np.save('out.npy',X)



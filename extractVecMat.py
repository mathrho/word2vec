#/datastore/zhenyang/bin/python

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#pretrained_model = './vectors.bin'
pretrained_model = '../freebase-vectors-skipgram1000-en.bin'
#pretrained_model = '../GoogleNews-vectors-negative300.bin'
model = gensim.models.Word2Vec.load_word2vec_format(pretrained_model, binary=True)
#model['animal']
print model.similarity('/en/dog', '/en/cat')
print model.similarity('/en/dog', '/en/mountain')




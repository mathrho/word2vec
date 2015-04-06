#/datastore/zhenyang/bin/python

import sys
import os
import gensim, logging
import numpy as np
import scipy.io as sio


def main():

    ##############
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    #pretrained_model = './vectors.bin'
    #pretrained_model = '../freebase-vectors-skipgram1000-en.bin'
    pretrained_model = '../GoogleNews-vectors-negative300.bin'
    model = gensim.models.Word2Vec.load_word2vec_format(pretrained_model, binary=True)

    ##############
    print model.syn0.shape
    print model.syn1.shape

    #np.savetxt('word2vec_GoogleNews.txt', word2vec_mat)
    #sio.savemat('word2vec_GoogleNews.mat', {'word2vec':word2vec_mat})

if __name__ == "__main__":
    main()
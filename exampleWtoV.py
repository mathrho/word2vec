#/datastore/zhenyang/bin/python

import gensim, logging
import sys
import os
from xml.etree import ElementTree

def get_parentmap(tree):
    parent_map = {}
    for p in tree.iter():
        for c in p:
            if c in parent_map:
                parent_map[c].append(p)
                # Or raise, if you don't want to allow this.
            else:
                parent_map[c] = [p]
                # Or parent_map[c] = p if you don't want to allow this
    return parent_map


def main():

    ##############
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    #pretrained_model = './vectors.bin'
    #pretrained_model = '../freebase-vectors-skipgram1000-en.bin'
    pretrained_model = '../GoogleNews-vectors-negative300.bin'
    model = gensim.models.Word2Vec.load_word2vec_format(pretrained_model, binary=True)
    #model['animal']
    #print model.similarity('/en/dog', '/en/cat')
    #print model.similarity('/en/man', '/en/woman')
    #print model.similarity('/en/man', '/en/male')
    print model.similarity('man', 'woman')
    print model.similarity('man', 'male')


if __name__ == "__main__":
    main()
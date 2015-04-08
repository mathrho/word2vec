#!/datastore/zhenyang/bin/ python

import sys
import os
import gensim, logging
import numpy as np
import scipy.io as sio
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
    imgnet_xml_file = 'structure_released.xml'
    tree = ElementTree.parse(imgnet_xml_file)

    root = tree.getroot()
    release_data = root[0].text
    synsets = root[1]


    ##############
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    #pretrained_model = './vectors.bin'
    #pretrained_model = '../freebase-vectors-skipgram1000-en.bin'
    pretrained_model = '../GoogleNews-vectors-negative300.bin'
    model = gensim.models.Word2Vec.load_word2vec_format(pretrained_model, binary=True)
    #model['animal']
    #print model.similarity('/en/dog', '/en/cat')
    #print model.similarity('/en/dog', '/en/mountain')


    ##############
    parent_map = get_parentmap(tree)
    classids = open('synsets.txt', 'r').read().splitlines()

    cc = 0
    clsid = 0
    vec_size = 300
    word2vec_classids = {}
    word2vec_map = {}
    word2vec_mat = np.zeros((len(classids), vec_size))
    for classid in classids:
        idc = 1
        for target in synsets.findall(".//synset[@wnid='" + classid + "']"):
            classnames = target.get('words').split(', ')
            for classname in classnames:
                #classname = '/en/' + classname.replace(' ', '_')
                classname = classname.replace(' ', '_')
                try:
                    wordvec = model[classname]
                    word2vec_mat[clsid, :] = wordvec
                    ##
                    c = target.get('wnid')
                    word2vec_classids[classid] = c
                    if c in word2vec_map:
                        word2vec_map[c].append(classid)
                    else:
                        word2vec_map[c] = [classid]

                    idc = 0
                    break

                except:
                    pass
            break

        #print dir(model)
        if idc>0:
            classnames = target.get('words').split(', ')
            for classname in classnames:
                namewords = classname.split(' ')
                wordvec = np.zeros(vec_size)
                for mameword in namewords:
                    try:
                        wordvec = np.add(wordvec, model[mameword])
                        idc = 0
                    except:
                        idc = 1
                        break

                if idc == 0:
                    word2vec_mat[clsid, :] = wordvec
                    ##
                    c = target.get('wnid')
                    word2vec_classids[classid] = c
                    if c in word2vec_map:
                        word2vec_map[c].append(classid)
                    else:
                        word2vec_map[c] = [classid]
                    break

        if idc>0:
            for parent in parent_map[target]:
                if True:
                #if parent.get('wnid') not in classids:

                    classnames = parent.get('words').split(', ')
                    for classname in classnames:
                        #classname = '/en/' + classname.replace(' ', '_')
                        classname = classname.replace(' ', '_')
                        try:
                            wordvec = model[classname]
                            word2vec_mat[clsid, :] = wordvec
                            ##
                            c = parent.get('wnid')
                            word2vec_classids[classid] = c
                            if c in word2vec_map:
                                word2vec_map[c].append(classid)
                            else:
                                word2vec_map[c] = [classid]

                            idc = 0
                            break
                        except:
                            pass
                    
                    if idc>0:
                        for classname in classnames:
                            namewords = classname.split(' ')
                            wordvec = np.zeros(300)
                            for mameword in namewords:
                                try:
                                    wordvec = np.add(wordvec, model[mameword])
                                    idc = 0
                                except:
                                    idc = 1
                                    break

                            if idc == 0:
                                word2vec_mat[clsid, :] = wordvec
                                ##
                                c = parent.get('wnid')
                                word2vec_classids[classid] = c
                                if c in word2vec_map:
                                    word2vec_map[c].append(classid)
                                else:
                                    word2vec_map[c] = [classid]

                                break

                else:
                    print classid + '\t' + target.get('wnid') + '\t' + parent.get('wnid') + '\n'

                if idc == 0:
                    break
 
        clsid = clsid + 1
        cc = cc + idc

    #np.savetxt('synset_word2vec_GoogleNews.txt', word2vec_mat)
    #sio.savemat('synset_word2vec_GoogleNews.mat', {'word2vec':word2vec_mat})
    print cc

    fp = open('./synset-filtered.txt', 'w')
    for classid in classids:
        fp.write(classid + '\t' + word2vec_classids[classid] + '\n')
    fp.close()

    fp = open('./synset-word2vec-map.txt', 'w')
    for classid in word2vec_map.keys():
        fp.write(classid + '\t' + ','.join(word2vec_map[classid]) + '\n')
    fp.close()

if __name__ == "__main__":
    main()
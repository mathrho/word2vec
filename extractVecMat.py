#/datastore/zhenyang/bin/python

import sys
import os
import gensim, logging
import numpy as np
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
    ##
    #for child in synsets.iter():
    #    if len(child) > 0:
    #        continue
            #wnid = child.attrib.get("wnid")
            #imagepath = get_imagepath(wnid)
            #if not os.path.exists(imagepath) or os.path.getsize(imagepath) == 0:
            #    params = {
            #    "wnid": wnid,
            #    "username": config.username,
            #    "accesskey": config.accesskey,
            #    "release": "latest",
            #    }
            #    download_file(config.synset_url, imagepath, params)


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
    #fp = open('./synset-missing-GoogleNews.txt', 'w')
    #fp = open('./synset-missing-freebase.txt', 'w')
    parent_map = get_parentmap(tree)
    cc = 0

    classids = open('synsets.txt', 'r').read().splitlines()

    vec_size = 300
    word2vec_mat = np.zeros((vec_size, len(classids)))
    clsid = 0
    for classid in classids:
        idc = 1
        for target in synsets.findall(".//synset[@wnid='" + classid + "']"):
            classnames = target.get('words').split(', ')
            for classname in classnames:
                #classname = '/en/' + classname.replace(' ', '_')
                classname = classname.replace(' ', '_')
                try:
                    wordvec = model[classname]
                    word2vec_mat[:, clsid] = wordvec
                    idc = 0
                    #break
                except:
                    pass
                    #continue
                    #print classname
                    
                #if classname not in model.keys():
                #   print classname
            break

        #print dir(model)
        if idc:
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
                    word2vec_mat[:, clsid] = wordvec
                    break


        if idc:
            for parent in parent_map[target]:
                if True:
                #if parent.get('wnid') not in classids:

                    classnames = parent.get('words').split(', ')
                    for classname in classnames:
                        #classname = '/en/' + classname.replace(' ', '_')
                        classname = classname.replace(' ', '_')
                        try:
                            wordvec = model[classname]
                            word2vec_mat[:, clsid] = wordvec
                            idc = 0
                            break
                        except:
                            pass
                    
                    if idc:
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
                                word2vec_mat[:, clsid] = wordvec
                                break

                else:
                    print classid + '\t' + target.get('wnid') + '\t' + parent.get('wnid') + '\n'

                if idc == 0:
                    break

        #if idc:
        #    fp.write(classid + '\n')
        clsid = clsid + 1
        cc = cc + idc

    np.savetxt('synset_word2vec_GoogleNews.txt', word2vec_mat)
    print cc
    #fp.close()

if __name__ == "__main__":
    main()
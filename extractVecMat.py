#/datastore/zhenyang/bin/python

import gensim, logging
import sys
import os
from xml.etree import ElementTree

##############
imgnet_xml_file = 'structure_released.xml'
tree = ElementTree.parse(imgnet_xml_file)

root = tree.getroot()
release_data = root[0].text
synsets = root[1]
##
for child in synsets.iter():
    if len(child) > 0:
        continue
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
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#pretrained_model = './vectors.bin'
#pretrained_model = '../freebase-vectors-skipgram1000-en.bin'
#pretrained_model = '../GoogleNews-vectors-negative300.bin'
#model = gensim.models.Word2Vec.load_word2vec_format(pretrained_model, binary=True)
#model['animal']
#print model.similarity('/en/dog', '/en/cat')
#print model.similarity('/en/dog', '/en/mountain')


##############
for classid in open('synsets.txt', 'r').readlines():
    classid = classid.strip()




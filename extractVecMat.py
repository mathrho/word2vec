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
    parent_map = get_parentmap(tree)
    cc = 0
    for classid in open('synsets.txt', 'r').readlines():
        classid = classid.strip()

        #classid = 'n01807828'
        #for target in synsets.findall(".//synset[@wnid='" + classid + "']"):
            #print target.get('words')
            #for parent in parent_map[target]:
                #print parent.get('words')

        idx = 1
        for target in synsets.findall(".//synset[@wnid='" + classid + "']"):
        #if target:
            classnames = target.get('words').split(', ')
            for classname in classnames:
                #classname = '/en/' + classname.replace(' ', '_')
                classname = classname.replace(' ', '_')
                try:
                    wordvec = model[classname]
                    idx = 0
                    #break
                except:
                    pass
                    #continue
                    #print classname
                    
                #if classname not in model.keys():
                #   print classname
            break
        #else:
        #    print classid
        #    cc = cc + 1

        if idx:
            for parent in parent_map[target]:
                classnames = parent.get('words').split(', ')
                for classname in classnames:
                    #classname = '/en/' + classname.replace(' ', '_')
                    classname = classname.replace(' ', '_')
                    try:
                        wordvec = model[classname]
                        idx = 0
                        #break
                    except:
                        pass
                break

        cc = cc + idx

    print cc

if __name__ == "__main__":
    main()
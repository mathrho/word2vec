load word2vec_GoogleNews.mat
word2vec = normalizeColsL2(double(word2vec));
nPCADims = 30;                                                                                                                                   
[X, pcamap] = netpca(double(word2vec'), nPCADims);
meanvec = mean(word2vec, 2);
save('word2vec_GoogleNews_PCAmap30.mat', 'pcamap', 'meanvec');

%load attr_word2vec_GoogleNews.mat
%load synset_word2vec_GoogleNews.mat

%word2vec = normalizeColsL2(double(word2vec));                                                                                                            

%nPCADims = 30;                                                                                                                                   
%[X, map] = netpca(double(word2vec'), nPCADims);

%meanvec = mean(word2vec, 2);
%word2vec = map' * (word2vec - repmat(meanvec, 1, size(word2vec, 2)));

%save('attr_word2vec_GoogleNews_PCAed.mat', 'word2vec');
%save('synset_word2vec_GoogleNews_PCAed.mat', 'word2vec');
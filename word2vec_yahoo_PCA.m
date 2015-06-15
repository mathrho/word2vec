function word2vec_yahoo_PCA()
%nPCADims
%pcamap
%meanvec

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
load('attr_word2vec_yahoo_500d.mat')
word2vec = word2vec';

nPCADims = 30;
word2vec = normalizeColsL2(double(word2vec));                                                                                                                                 
[X, pcamap] = netpca(double(word2vec'), nPCADims);
meanvec = mean(word2vec, 2);
save('attr_word2vec_yahoo_500PCA30_model.mat', 'pcamap', 'meanvec');

%word2vec = word2vec';
%word2vec = normalizeColsL2(double(word2vec));
word2vec = pcamap' * (word2vec - repmat(meanvec, 1, size(word2vec, 2)));
word2vec = word2vec';
save('attr_word2vec_yahooPCA_30d.mat', 'word2vec');

clear
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
load('synset_word2vec_yahoo_500d.mat')
word2vec = word2vec';

nPCADims = 30;
word2vec = normalizeColsL2(double(word2vec));                                                                                                                                 
[X, pcamap] = netpca(double(word2vec'), nPCADims);
meanvec = mean(word2vec, 2);
save('synset_word2vec_yahoo_500PCA30_model.mat', 'pcamap', 'meanvec');

%word2vec = word2vec';
%word2vec = normalizeColsL2(double(word2vec));
word2vec = pcamap' * (word2vec - repmat(meanvec, 1, size(word2vec, 2)));
word2vec = word2vec';
save('synset_word2vec_yahooPCA_30d.mat', 'word2vec');

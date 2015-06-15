function word2vec_yahoo_PCA()
%nPCADims
%pcamap
%meanvec

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
load('attr_word2vec_yahoo_500d.mat');
word2vec = word2vec';
idx = find(sum(word2vec, 1)==0)
w2v = word2vec(:, sum(word2vec, 1)~=0);

nPCADims = 30;
w2v = normalizeColsL2(double(w2v));                                                                                                                                 
[X, pcamap] = netpca(double(w2v'), nPCADims);
meanvec = mean(w2v, 2);
save('attr_word2vec_yahoo_500PCA30_model.mat', 'pcamap', 'meanvec');

%word2vec = word2vec';
word2vec = normalizeColsL2(double(word2vec));
word2vec = pcamap' * (word2vec - repmat(meanvec, 1, size(word2vec, 2)));
word2vec(:, idx) = 0;
word2vec = word2vec';
save('attr_word2vec_yahooPCA_30d.mat', 'word2vec');

clear
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
load('synset_word2vec_yahoo_500d.mat');
word2vec = word2vec';
idx = find(sum(word2vec, 1)==0)
w2v = word2vec(:, sum(word2vec, 1)~=0);

nPCADims = 30;
w2v = normalizeColsL2(double(w2v));                                                                                                                                 
[X, pcamap] = netpca(double(w2v'), nPCADims);
meanvec = mean(w2v, 2);
save('synset_word2vec_yahoo_500PCA30_model.mat', 'pcamap', 'meanvec');

%word2vec = word2vec';
word2vec = normalizeColsL2(double(word2vec));
word2vec = pcamap' * (word2vec - repmat(meanvec, 1, size(word2vec, 2)));
word2vec(:, idx) = 0;
word2vec = word2vec';
save('synset_word2vec_yahooPCA_30d.mat', 'word2vec');
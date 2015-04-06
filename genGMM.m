load D:/Data/PASCAL/VOC2007/matlab/siftPhow/voc2007_sampledTrainvalSiftVectors500K_phow_ss2.mat                                                  
                                                                                                                                                 
sift = normalizeColsL2(double(sift));                                                                                                            
                                                                                                                                                 
nPCADims = 64;                                                                                                                                   
[X, map] = netpca(double(sift'), nPCADims);                                                                                                      
                                                                                                                                                 
%if need                                                                                                                                         
pcamap = map;                                                                                                                                    
save -v7.3 D:/Data/PASCAL/VOC2007/matlab/siftPhow/voc2007_pcamap64.mat pcamap                                                                    
                                                                                                                                                 
sift = map' * sift;                                                                                                                              
                                                                                                                                                 
numWords = 256;                                                                                                                                  
%vocab = vl_kmeans(sift, numWords, 'verbose', 'algorithm', 'elkan');                                                                             
vocab = vl_kmeans(sift, numWords, 'verbose', 'algorithm', 'elkan', 'NumRepetitions', 10);                                                        
                                                                                                                                                 
[drop, binsa] = min(vl_alldist(single(vocab), single(sift)), [], 1);                                                                             
                                                                                                                                                 
%computeGmmForFisher('D:/Data/PASCAL/VOC2007/matlab/siftPhow/voc2007_gmm256.bin', sift, vocab, binsa, 1);                                        
computeGmmForFisher('D:/Data/PASCAL/VOC2007/matlab/siftPhow/voc2007_gmm256.bin', sift, vocab, binsa);  
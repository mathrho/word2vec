time ./word2vec -train ../yfcc100m_lower_nonumbers -output yahoo_100m_words_30d.output -cbow 0 -size 30 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 40 -binary 0 -iter 5
#./compute-accuracy yahoo_100m_words_30d.output 30000 < questions-words.txt
# to compute accuracy with the full vocabulary, use: ./compute-accuracy yahoo_100m_words_30d.output < questions-words.txt
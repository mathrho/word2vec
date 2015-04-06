function histograms = normalizeColsL2(histograms)

% Get sums
sumA = sum(histograms.^2, 1) ;
% Make sure there is no division by zero
sumA(sumA == 0) = 1;

histograms = bsxfun(@times, histograms, 1 ./ sqrt(sumA)) ;

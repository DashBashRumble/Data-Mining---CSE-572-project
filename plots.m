load('preprocessing.mat');
disp(length(cgmSeriesProcessed));

% featureMatrix = [];
% 
% cgmRow_1 = cgmSeries(1,:);
% cgmTime_1 = cgmTime(1, :);
% 
% cgmDiffValues_1 = [0 cgmRow_1(1:end-1) - cgmRow_1(2:end)];
%     
% [cgmDiffMax, indexMax] = max(cgmDiffValues_1);

% disp(length(cgmDiffValues_1))

% plot(cgmTime_1, cgmDiffValues_1);
% text(indexMax, cgmDiffMax, 'GLobal Maxima')

%Power spectral density

% fft_1 = abs(fft(cgmRow_1));
% N = length(fft_1);
% psdx = (1/(2*pi*N)) * abs(fft_1(1:N/2+1)).^2;
% psdx(2:end-1) = 2*psdx(2:end-1);
% freq = 0:(2*pi)/N:pi;
% 
% disp(length(freq));
% disp(length(psdx));
% 
% plot(freq/pi,10*log10(psdx))



% plot(fft_1)

% movRMS_1 = sqrt(movmean(cgmRow_1 .^ 2, 5));
% plot(movRMS_1);

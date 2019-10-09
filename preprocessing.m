cgmSeries = csvread("./DataFolder/CGMSeriesLunchPat1.csv", 1, 0);
cgmTime = csvread("./DataFolder/CGMDatenumLunchPat1.csv", 1, 0);

% plot(cgmTime(1, :), cgmSeries(1, :));

%Pre Processing of the data

cgmSeriesProcessed = cgmSeries(:, 1:31);
cgmDateNumProcessed = cgmTime(:, 1:31);

[cgmSeriesProcessed, index_to_remove] = rmmissing(cgmSeriesProcessed, 'MinNumMissing', round(31/4));

cgmDateNumProcessed = cgmTime(not(index_to_remove), :);


% If number of missing values less than 31/4, fill those

cgmSeriesProcessed = fillmissing(cgmSeriesProcessed, 'linear');


cgmDateNumProcessed = flip(flip(cgmDateNumProcessed,1),2);
cgmSeriesProcessed = flip(flip(cgmSeriesProcessed,1),2);


CGM_Timestamp_table_pat1 = readtable('./DataFolder/CGMDatenumLunchPat1.csv');
CGM_Series_Lunch_pat1 = readtable('./DataFolder/CGMSeriesLunchPat1.csv');

meal_time_1 = CGM_Timestamp_table_pat1{1, :};
% plot(meal_datetime_1, cgm_glu_1);

% ix = ismissing('StringTreatAsMissing',{'NaN'});
% CGM_Series_Lunch_pat1(any(ix,2),:);

meal_time_2 = CGM_Timestamp_table_pat1{2, :};
cgm_glu_2 = CGM_Series_Lunch_pat1{2, :};
meal_datetime_2 = arrayfun(@(time) datetime(time, 'ConvertFrom','datenum'),meal_time_2);
moving_mean_glucose_2 = movmean(cgm_glu_2, [length(cgm_glu_2) 0]);
cgm_glu_2 = fillmissing(cgm_glu_2, 'previous');
% plot(meal_datetime_1, moving_mean_glucose)
% plot(meal_datetime_2, moving_mean_glucose_2);
% time_series_2 = timeseries(moving_mean_glucose_2);

% fft_2 = fft(cgm_glu_2);
% mag_2 = abs(fft_2);
% freq_2 = (0:length(fft_2)-1)*100/length(fft_2);
% inverse_fft_2 = real(ifft(fft_2));
% phase_2 = unwrap(angle(fft_2));
% plot(meal_datetime_2, phase_2*180/pi);
% plot(meal_datetime_2, inverse_fft_2);

% plot(freq_2, mag_2)
% plot(meal_datetime_2, fft_2);
% fft_2 = fft(cgm_glu_2);
% plot(meal_datetime_1, abs(fft_2));

moving_mean_pt1 = cgm_glu_2;
for c1 = 1:33
    cgm_glu = CGM_Series_Lunch_pat1{c1, :};
    cgm_glu = fillmissing(cgm_glu, 'previous');
    moving_mean_pt1(c1,:) = movmean(cgm_glu, [length(cgm_glu) 0]);
end

csvwrite('Moving_Mean_pt1.csv',moving_mean_pt1)
entropy_pt1 = zeros(size(CGM_Series_Lunch_pat1));
disp(size(entropy_pt1))
for c1 = 1:33
    for c2 = 1:31
        cgm_glu_i = CGM_Series_Lunch_pat1{c1, 1:c2};
        cgm_glu_i = cgm_glu_i/max(abs(cgm_glu_i));
%         disp(cgm_glu_i)
        entropy_pt1(c1, c2) = entropy(cgm_glu_i);
    end
end

plot(fliplr(meal_datetime_2), entropy_pt1(2, :))

csvwrite('MovingEntropy.csv', entropy_pt1);



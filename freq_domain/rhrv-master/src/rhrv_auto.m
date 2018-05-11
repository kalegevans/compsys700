function[] = rhrv_auto(nameOfDb)
for i = 1:36
    fileNo = pad(int2str(i),2,'left','0');
    rhrv(nameOfDb + '/cu' + fileNo, 'window_minutes', 4, 'plot', false)
end
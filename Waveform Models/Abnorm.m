%y = .5*sin(t);
%yo = 4.76;
%for k = 5
   
%y = yo + y + sin(k*t)/k;
%end
%plot(t, y)

t = 0:0.1:pi; %Frequency
yo = 0; %Starting point
y = yo + 17*sin(t) + (3*sin(3*t)/3) + (17*sin(5*t)/5); %Harmonics equation
y = floor(y) %makes values to integers
plot(t, y)
%save(Abnorm.mat)
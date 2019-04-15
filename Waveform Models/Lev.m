t = 0:0.1:pi; %Xscale
yo = 0; %starting point
y = yo + 22*sin(t) + (20*sin(3*t)/3) + (22*sin(5*t)/5); %Harmonics eq
y = floor(y) %values to integers
plot(t, y)

%insert to write
%escape
%:wq to save and quit
%:q! to quit without saving

t = 0:0.1:pi; %Xscale
w = 1;%Frequency 
A = 15; 
a = A; %Amplitude,could also div by pi
y = 0; %starting point
n = 6; %how many iterations
for  i = 1:n
   y =(y+a*((1)^(i-1))*(1/i)*sin(i*w*t)); %Fourier Transform Eq
   
   
i = i+1;  
end
%y = sgolayfilt(y, 3, 7)
y = floor(y) %values to integers
plot(t,(y));
%save('Normal.mat', 'y')

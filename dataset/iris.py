function [yt, akurasi] = knn (xr,yr, ys, K)
% implementasi the Nearest neighbor algorithm
% Inputs:
% xr - Train patterns (obs x dim)
% yr - Train targets (obs x 1)
% xs - Test patterns (obs x dim)
% K - Number of Nearest neighbors
% Outputs
% yt- Predicted targets
L=length(yr);
Uc=uniques(yr);

if (L < K),
  error(;tetangga lebih banyak dari jumlah titik training')
end
N   = size(xs, 1);
yt  = zeros(N, 1);
for i = 1:N,
    jar=(xr-repmat(xs(i,:),L,1)).^2;
    jarak = sum(jar, 2);%jarak tiap titik dataset terhadap data training
    [m, idk]= sort(jarak);%urutkan jarak dr yang terkecil
    lab=yr (idk(1:K));%ambil K jarak terkecil dan periksa labelnya
     n = hist(lab, Uc);%menempatkan data testing ke kelas mana
(tergantung Uc)
    [m, best]= max(n);%mencari frekuensi maksimum kelas mana paling
banyak dari K tetangga terdekat
    yt(i) = Uc(best);
end
beda=find(ys~=yt);
akurasi=1-length(beda)/length(yt);



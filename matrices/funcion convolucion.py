from scipy import signal as sg
print(sg.convolve([[255, 7, 3],
                   [212, 240, 4],
                   [218, 216, 230]],
                   [[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], "valid"))
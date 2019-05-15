#------------------
# Author luzhongshan
# Time2019/5/15 21:38
#------------------
import torch


def de_subpix(y):
    (b, c, h, w) = y.shape
    # print(b, c, h, w)
    h1 = int(h / 2)
    w1 = int(w / 2)
    d1 = torch.zeros((b, c, h1, w1))
    d2 = torch.zeros((b, c, h1, w1))
    d3 = torch.zeros((b, c, h1, w1))
    d4 = torch.zeros((b, c, h1, w1))
    # print(y.shape)
    for i in range(0, h1, 2):
        for j in range(0, w1, 2):
            d1[:, :, i, j] = y[:, :, 2 * i, 2 * j]
            d2[:, :, i, j] = y[:, :, 2 * i + 1, 2 * j]
            d3[:, :, i, j] = y[:, :, 2 * i, 2 * j + 1]
            d4[:, :, i, j] = y[:, :, 2 * i + 1, 2 * j + 1]
            # print()
            # print(i,j)
    out = torch.cat([d1, d2, d3, d4], 1)
    # print(out.shape)
    return out
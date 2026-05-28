import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update(frame):
    global board
    global fig
    # global frameNum
    board = nextGenCalc(board)
    # plt.savefig('screenshots/frame_{}.png'.format(frameNum))
    img.set_data(board)
    # frameNum += 1
    return [img]

def shift(board, dr, dc):
    shifted = np.roll(board, dr, 0)
    shifted = np.roll(shifted, dc, 1)

    if dr == 1:
        shifted[0, :] = 0
    elif dr == -1:
        shifted[-1, :] = 0
    if dc == 1:
        shifted[:, 0] = 0
    elif dc == -1:
        shifted[:, -1] = 0

    return shifted

def nextGenCalc(board):
    neighbor = sum(shift(board, i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if(i !=0 or j!=0))
    newBorad = (neighbor == 3) | (((neighbor == 2) | (neighbor == 3)) & board == 1)

    return newBorad

if __name__ == "__main__":
    # frameNum = 0
    with open(file='./patterns/gosper-glider-gun.txt', mode='r') as f:
        
        imGoL = []
        r = 0
        allLines = f.readlines()
        for line in allLines:
            line = line.strip()
            lineChar = []
            for col in line:
                if col == '.':
                    lineChar.append(0)
                else:
                    lineChar.append(1)
            imGoL.append(lineChar)

    fig = plt.figure()
    ax = plt.subplot()

    imGoLnp = np.array(imGoL)
    img = ax.imshow(imGoLnp)
    board = imGoLnp

    ani = FuncAnimation(fig, update, frames=10, interval = 30, blit = True)
    plt.show()

    

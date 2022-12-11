import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

btc_df = pd.read_csv("BTC-USD.csv")
btc_df = btc_df[["Date", "Close"]]
btc_df = btc_df.dropna()

fig, ax = plt.subplots()
xx = btc_df.index
yy = btc_df["Close"]


def animate(i):
    # clear the previous image
    ax.cla()
    plt.xlabel(
        "Day from 10/12/21 to 10/12/22"
    )
    plt.ylabel("BTC USD Daily Price")
    plt.title(
        "BTC USD Daily Price 10/12/21 - 10/12/22"
    )
    # plot the line
    ax.plot(xx[:i], yy[:i])
    # fix the x axis limits
    ax.set_xlim([xx[0], xx[-1]])
    # fix the y axis limits
    ax.set_ylim(
        [
            0.9 * np.min(yy),
            1.1 * np.max(yy),
        ]
    )


anim = animation.FuncAnimation(
    fig,
    animate,
    frames=len(btc_df) + 1,
    interval=100,
    blit=False,
)
# plt.show()
anim.save(
    "btc_daily.mp4", writer="ffmpeg"
)

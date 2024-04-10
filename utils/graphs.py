import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime, timedelta

def balance_graph():
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import numpy as np
    from datetime import datetime, timedelta


    num_points = 24
    dates = [datetime.now() - timedelta(days=30) * x for x in range(num_points)]
    balance = np.cumsum(np.random.randn(num_points) * 1000)  # Cumulative sum to simulate balance changes


    fig, ax = plt.subplots(figsize=(10, 5))


    fig.patch.set_facecolor('#0F102B')
    ax.set_facecolor('#0F102B')

    ax.plot(dates, balance, color='skyblue', label='Balance', linewidth=2)

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    fig.autofmt_xdate()


    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.tick_params(axis='both', which='both', bottom=False, labelbottom=False, left=False, labelleft=False)


    for spine in ['top', 'right', 'left']:
        ax.spines[spine].set_visible(False)


    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)


    plt.tight_layout()

    return fig


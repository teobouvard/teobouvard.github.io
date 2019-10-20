import numpy as np
from matplotlib import pyplot as plt

def optplot(result, x, y, r, verbose=True):
    plt.rcParams["figure.figsize"] = (16,8)
    
    t = result.x
    angles = [f'{np.degrees(theta):.2f}' for theta in t]
    print(f'Objective function has been evaluated {result.nfev} times')
    print(f'Optimizer performed {result.nit} iterations')
    print(f'Angles minimizing the objective function : {angles}')

    # Compute optimized points from angles
    x_p = x + r*np.sin(t)
    y_p = y + r*np.cos(t)
    dists = np.sqrt(np.power(np.diff(x_p), 2) + np.power(np.diff(y_p), 2))
    
    _, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(min(x)-2, max(x)+2)
    ax.set_ylim(min(y)-2, max(y)+2)
    text_opt = dict(textcoords='offset pixels', ha='center')
    
    plt.scatter(x, y, marker='+')
    plt.plot(x_p, y_p, ls='--')
    
    for i, (cx, cy, cr) in enumerate(zip(x, y, r)):
        circle = plt.Circle((cx, cy), cr, color='black', fill=False)
        ax.add_artist(circle)
        if verbose:
            if i == 0:
                ax.annotate('Position', (cx, cy), xytext=(0, -20), **text_opt)
            elif i < len(x) - 1:
                ax.annotate(f'TP{i}', (cx, cy), xytext=(0, 10), **text_opt)
            else:
                ax.annotate(f'Goal', (cx, cy), xytext=(0, 10), **text_opt)
                
    ax.annotate(f'Total distance : {dists.sum():.2f}', xy=(0.05, 0.9), xycoords='axes fraction')
    
    plt.tight_layout()
        
def taskplot(x, y, r, verbose=True):
    plt.rcParams["figure.figsize"] = (16,8)
    
    _, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(min(x)-2, max(x)+2)
    ax.set_ylim(min(y)-2, max(y)+2)

    plt.scatter(x, y, marker='+')
    text_opt = dict(textcoords='offset pixels', ha='center')

    for i, (cx, cy, cr) in enumerate(zip(x, y, r)):
        circle = plt.Circle((cx, cy), cr, color='black', fill=False)
        ax.add_artist(circle)
        if verbose:
            if i == 0:
                ax.annotate('Position', (cx, cy), xytext=(0, -20), **text_opt)
            elif i < len(x) - 1:
                ax.annotate(f'TP{i}', (cx, cy), xytext=(0, 10), **text_opt)
            else:
                ax.annotate(f'Goal', (cx, cy), xytext=(0, 10), **text_opt)
    
    plt.tight_layout()
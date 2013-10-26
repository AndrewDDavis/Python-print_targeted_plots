# print_targeted_plots.py
"""Make plots suitable for printed publication.

This module contains functions to improve the appearance of 
matplotlib plots that will appear in print.  The recommended usage is
to first decide on a font size that suits the figure; for example, 8
point font for a single-column figure.  Next, run set_ink_weight()
before creating the figure.  After plotting, use the other convenience
functions to adjust the figure parameters before calling show() or
savefig().

Example:
    import numpy as np
    import matplotlib.pyplot as plt
    import print_targeted_plots as ptp
    font_size = 8
    ptp.set_ink_weight(font_size)
    fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.42, 3.), dpi=150)
    abc = np.array([1,2,3,4])
    ax1.plot(abc, 'go--', label='abc')
    (_, caps, _) = ax1.errorbar(abc-1, abc, yerr=abc/10., fmt=None)
    ax1.yaxis.grid(True)
    ax1.set_axisbelow(True)
    ax1.legend()
    ptp.adjust_label_padding(font_size)
    ptp.adjust_eb_caps(font_size, caps)
    ptp.adjust_grid_dashes(font_size)
    ptp.adjust_legends()
    ptp.turn_frame_off(ax2)

"""

# v0.1 (Oct 2013) by Andrew Davis (addavis@gmail.com)
#
# History:
#     v0.1 (Oct 2013): initial release
#
# License:
#     The MIT License (MIT)
#     See LICENSE file, or:
#     http://opensource.org/licenses/MIT

__version__ = "0.1"

def set_ink_weight(font_size, line_size=None, set_fonts=True, set_lines=True):
    """Change the rc settings for widths of figure lines and fonts.
    Call this before the figure is created;  font_size is in points.

    Example: set_ink_weight(12)
    """
    
    import matplotlib.pyplot as plt

    plt.rc('figure', autolayout=True)   # prevent labels from being cut off -- similar results to plt.tight_layout()

    # Determine line width
    if line_size is None:
        line_size = font_size/12.

    if set_fonts:
        plt.rc('font', size=font_size)  # default font size for all text
        plt.rc('xtick', labelsize='small')
        plt.rc('ytick', labelsize='small')
        plt.rc('legend', fontsize='small')

    # Change marker, tick and line width values to default * factor
    if set_lines:
        plt.rc('lines', linewidth=line_size, markeredgewidth=0.5*line_size, markersize=6*line_size)
        plt.rc('patch', linewidth=line_size)
        plt.rc('axes', linewidth=line_size)
        plt.rc('grid', linewidth=0.5*line_size)
        plt.rc('xtick.minor', width=0.5*line_size, size=2*line_size, pad=4*line_size)
        plt.rc('xtick.major', width=0.5*line_size, size=4*line_size, pad=4*line_size)
        plt.rc('ytick.minor', width=0.5*line_size, size=2*line_size, pad=4*line_size)
        plt.rc('ytick.major', width=0.5*line_size, size=4*line_size, pad=4*line_size)

    #print("known values not set here [default]:\n" 
    #      "    none right now... [?]")

def adjust_label_padding(font_size):
    """Change axes label padding to match font size for all axes.
    Call this after the figure is made.

    Example:
        adjust_label_padding(12)
    """

    import matplotlib.pyplot as plt

    adj_factor = font_size/12.

    fig = plt.gcf()
    for ax in fig.axes:
        xlp = ax.xaxis.labelpad
        ylp = ax.yaxis.labelpad
        ax.xaxis.labelpad = xlp*adj_factor
        ax.yaxis.labelpad = ylp*adj_factor

def adjust_eb_caps(font_size, caps):
    """Change errorbar cap width according to font size.
    Call this after making error bars.

    Example:
        (_, caps, _) = ax1.errorbar(...)
        adjust_eb_caps(font_size, caps)
    """

    import matplotlib.pyplot as plt

    adj_factor = font_size/12.

    for cap in caps:
        cap.set_markersize(6*adj_factor)

def adjust_grid_dashes(font_size):
    """Change dash spacing of grid lines to match font size for all axes.
    Call this after the figure is made.

    Example:
        adjust_grid_dashes(12)
    """

    import matplotlib.pyplot as plt

    adj_factor = font_size/12.
    dash_ink = [1*adj_factor, 3*adj_factor]

    fig = plt.gcf()
    for ax in fig.axes:
        plt.setp(ax.xaxis.get_gridlines(), dashes=dash_ink)     # change grid dash width -- haven't found a get_dashes method to check defaults 
        plt.setp(ax.yaxis.get_gridlines(), dashes=dash_ink)

def adjust_legends():
    """Change legends to be borderless, but with a background.
    Call this after the figure is made.

    Example:
        adjust_legends()
    """

    import matplotlib.pyplot as plt

    fig = plt.gcf()
    for ax in fig.axes:
        leg = ax.get_legend()   # legend for axes
        if leg is not None:
            leg.get_frame().set_linewidth(0)


def turn_frame_off(ax=None):
    """Turn off axes frame box and ticks, but leaving background.
    Call this after the figure is made.

    Example:
        turn_frame_off(ax)
    """

    import matplotlib.pyplot as plt

    if ax is None:
        ax = plt.gca()

    for spine in ax.spines.itervalues():
        spine.set_visible(False)            # turn off box lines
    ax.xaxis.set_visible(False)             # take care of ticks and ticklabels
    ax.yaxis.set_visible(False)


def adjust_boxplot(bp, font_size):
    """Change colors of boxplot to be more subtle.  Uses blue and black.
    Also changes some weights and dashes according to font_size.

    Example:
        bp = ax1.boxplot(...)
        adjust_boxplot(bp, 8)
    """

    import matplotlib.pyplot as plt

    adj_factor = font_size/12.

    for bpFeature in ['boxes', 'whiskers', 'caps', 'fliers']:   # bp has entries: boxes, whiskers, caps, fliers, medians
       plt.setp(bp[bpFeature], color='#778899')
    plt.setp(bp['medians'], lw=1.1*adj_factor, color='black')
    plt.setp(bp['whiskers'], linestyle=':', dashes=[1*adj_factor, 3*adj_factor])     # set dash length


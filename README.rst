Print Targeted Plots
====================

Make plots suitable for printed publication.

This module contains functions to improve the appearance of  ``matplotlib``
plots that will appear in print.  The recommended usage is to first decide on
a font size that suits the figure; for example, 8 point font may be used for a
single-column figure.  The font size will be passed to the relevant
convenience functions, which adjust plot features in accordance with it.

Next, run ``set_ink_weight()`` before creating the figure.  After plotting,
use the other convenience functions to adjust the figure parameters before
calling ``show()`` or ``savefig()``.

Current capabilities of the module
----------------------------------

**set_ink_weight**
    Change the rc settings for widths of figure lines, markers, and fonts.
**adjust_label_padding**
    Change axes label padding of all axes.
**adjust_eb_caps**
    Change errorbar cap widths.
**adjust_grid_dashes**
    Change dash spacing of grid lines of all axes.
**adjust_legends**
    Change legends to be borderless, but with a background.
**turn_frame_off**
    Turn off axes frame box and ticks, but leave background.
**adjust_boxplot**
    Change colors of boxplot to be more subtle.  Uses blue and black.
    Also changes some line weights and dash spacing.


Example
-------

::

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

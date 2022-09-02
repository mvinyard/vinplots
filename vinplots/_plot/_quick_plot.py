
from ._PlotModule import _Plot

def _quick_plot(nplots=1, ncols=1, spines_to_delete=['top', 'right'], rm_ticks=False, **construct_kwargs):
    
    if spines_to_delete == "all":
        spines_to_delete = ['top', 'bottom', 'left', 'right']
    
    fig = _Plot()
    fig.construct(nplots=nplots, ncols=ncols, **construct_kwargs)
    fig.modify_spines(ax="all", spines_to_delete=spines_to_delete)
    axes = fig.linearize()
    
    if rm_ticks:
        for ax in axes:
            ax.set_xticks([])
            ax.set_yticks([])

    return fig, axes
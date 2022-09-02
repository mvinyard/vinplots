
def _linearize_axes(AxesDict):

    axes = []

    for i, row in AxesDict.items():
        for j, col in row.items():
            axes.append(AxesDict[i][j])
    return axes
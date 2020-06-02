import pygmt

# Built-in data
grid = pygmt.datasets.load_earth_relief(resolution="30m")

fig = pygmt.Figure()
# Layout a basemap
fig.basemap(region=[-150, -30, -60, 60], frame=True, projection="I-90/6i")
# Pseudo-color plot
fig.grdimage(grid=grid, cmap="viridis")
# Mask coastlines
fig.coast(land="#333333")
fig.savefig("img/pygmt-example.png", transparent=True)
fig.show()

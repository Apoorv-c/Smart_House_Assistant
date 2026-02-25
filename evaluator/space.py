def space_efficiency(layout, plot):
    total_room_area = sum(r.width * r.height for r in layout)
    plot_area = plot.length * plot.width
    return int((total_room_area / plot_area) * 100)
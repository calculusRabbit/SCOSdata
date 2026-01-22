import dearpygui.dearpygui as dpg


class Layout:
    MAIN_WIDTH = 1200
    MAIN_HEIGHT = 800
    
    LEFT_WIDTH = 550
    RIGHT_WIDTH = 600
    
    # Left panel
    ROW1_HEIGHT = 250
    ROW2_HEIGHT = 480
    ROW2_COL1_WIDTH = 335  
    ROW2_COL2_WIDTH = LEFT_WIDTH - ROW2_COL1_WIDTH - 8
    
class Colors:
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    GREEN = (0, 255, 0)


# Creating app
dpg.create_context()
dpg.create_viewport(
    title='SCOS',
    width=Layout.MAIN_WIDTH,
    height=Layout.MAIN_HEIGHT
)

# creating UI

# Main window
main_window = dpg.add_window(label="Main")

# Main layout: LEFT | RIGHT
main_group = dpg.add_group(horizontal=True, parent=main_window)

## LEFT MAIN
left_panel = dpg.add_child_window(
    width=Layout.LEFT_WIDTH,
    parent=main_group,
    border=False
)

left_row1 = dpg.add_child_window(
    height=Layout.ROW1_HEIGHT,
    border=True,
    parent=left_panel
)
dpg.add_text("Camera Image", parent=left_row1)

plots_group = dpg.add_group(horizontal=True, parent=left_row1)


for i in range(6):
    plot = dpg.add_plot(width=80, height=180, parent=plots_group)

    dpg.add_plot_axis(dpg.mvXAxis, parent=plot)

    dpg.add_plot_axis(dpg.mvYAxis, parent=plot)

left_row2_group = dpg.add_group(horizontal=True, parent=left_panel)

left_row2_col1 = dpg.add_child_window(
    width=Layout.ROW2_COL1_WIDTH,
    height=Layout.ROW2_HEIGHT,
    border=True,
    parent=left_row2_group
)

left_row2_col2 = dpg.add_child_window(
    width=Layout.ROW2_COL2_WIDTH,
    height=Layout.ROW2_HEIGHT,
    border=True,
    parent=left_row2_group
)


## RIGHT MAIN
right_panel = dpg.add_child_window(width=Layout.RIGHT_WIDTH, border=True, parent=main_group)
# add plots
for i in range(3):
    dpg.add_text("plot " + str(i+1) + ": ", parent=right_panel)
    plot = dpg.add_plot(height=150, width=-1, parent=right_panel)
    dpg.add_plot_axis(dpg.mvXAxis, label='x', parent=plot)
    dpg.add_plot_axis(dpg.mvYAxis, label='y', parent=plot)
    
    


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(main_window, True)
dpg.start_dearpygui()
dpg.destroy_context()
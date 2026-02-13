# import dearpygui.dearpygui as dpg
# import numpy as np
# import time


# class SCOS_UI:    
#     def __init__(self):
#         # chatgpt told me to use this tag for future
#         self.tags = {
#             'main_window': 'main_window',
#             'device_combo': 'device_combo',
#             'connect_device_btn': 'connect_device_btn',
#             'device_status_indicator': 'device_status_indicator',
#             'study_name_input': 'study_name_input',
#             'create_study_btn': 'create_study_btn',
#             'current_study_combo': 'current_study_combo',
#             'subject_input': 'subject_input',
#             'run_input': 'run_input',
#             'sampling_rate_slider': 'sampling_rate_slider',
#             'roi_preview_btn': 'roi_preview_btn',
#             'preview_btn': 'preview_btn',
#             'start_btn': 'start_btn',
#             'pause_btn': 'pause_btn',
#             'stop_btn': 'stop_btn',
#             'trigger_source_combo': 'trigger_source_combo',
#             'connect_trigger_btn': 'connect_trigger_btn',
#             'trigger_status_indicator': 'trigger_status_indicator',
#             'time_scale_input': 'time_scale_input',
#             'autoscale_checkbox': 'autoscale_checkbox',
#             'status_text': 'status_text',
#             'y_axis_k2': 'y_axis_k2',
#             'y_axis_bfi': 'y_axis_bfi',
#             'y_axis_cc': 'y_axis_cc',
#             'y_axis_od': 'y_axis_od',
#             'k2_series': 'k2_series',
#             'bfi_series': 'bfi_series',
#             'cc_series': 'cc_series',
#             'od_series': 'od_series',
#         }
        
#         # Generate sample data for plots
#         self.x_data = np.linspace(10, 20, 100)
#         self.k2_data = 2000 + 500 * np.sin(self.x_data * 3)
#         self.bfi_data = 400 + 200 * np.sin(self.x_data * 3)
#         self.cc_data = 195 + 5 * np.sin(self.x_data * 3)
#         self.od_data = -0.10 + 0.02 * np.sin(self.x_data * 3)
    
#     def create_ui(self):
#         with dpg.window(label="SCOS Data Acquisition App", 
#                        tag=self.tags['main_window'], 
#                        width=1260, 
#                        height=700):
            
#             with dpg.group(horizontal=True):
#                 self._create_left_column()
#                 self._create_right_column()
    
#     def _create_left_column(self):
#         """Create left column with camera image and controls"""
#         with dpg.child_window(width=550, height=750):
#             self._create_camera_image_panel()
#             dpg.add_spacer(height=20)
            
#             with dpg.group(horizontal=True):
#                 self._create_device_study_controls()
#                 self._create_roi_selection_panel()
    
#     def _create_camera_image_panel(self):
#         with dpg.group(horizontal=True):
#             # Create 6 vertical color bars
#             for i, label in enumerate(["K^2_raw", "K^2_1", "K^2_2", "K^2_3", "K^2_4", "K^2_5"]):
#                 with dpg.group():
#                     dpg.add_text(label)
#                     dpg.add_color_button(
#                         default_value=(0, 100+i*30, 200-i*20, 255), 
#                         width=80, 
#                         height=200
#                     )
    
#     def _create_device_study_controls(self):
#         with dpg.child_window(width=280, height=400):
#             dpg.add_text("Device")

#             with dpg.group(horizontal=True):
#                 dpg.add_combo(width=100, tag=self.tags['device_combo'])
#                 dpg.add_button(label="connect device", width=100, tag=self.tags['connect_device_btn'])
            
#             dpg.add_spacer(height=10)
            
#             dpg.add_text("Study name")
#             with dpg.group(horizontal=True):
#                 dpg.add_input_text(width=160, tag=self.tags['study_name_input'])
#                 dpg.add_button(
#                     label="Create", 
#                     width=100,
#                     tag=self.tags['create_study_btn']
#                 )
            
#             dpg.add_text("sampling rate")
#             dpg.add_slider_float()
    
#     def _create_roi_selection_panel(self):
#         """Create ROI selection panel with preview and control buttons"""
#         with dpg.child_window(width=250, height=400):
#             dpg.add_text("ROI selection")
            
#             # Image preview placeholder
#             with dpg.texture_registry(show=False):
#                 # 1x1 transparent pixel as placeholder
#                 empty_texture = dpg.add_static_texture(1, 1, [0.0, 0.0, 0.0, 0.0])

#             # Display the placeholder image
#             dpg.add_image(empty_texture, width=200, height=200)

            
#             dpg.add_button(
#                 label="Preview",
#                 width=200,
#                 height=30
#             )

#             dpg.add_button(
#                 label="Start", 
#                 width=200,
#                 height=30
#             )
#             dpg.add_button(
#                 label="Pause", 
#                 width=200,
#                 height=30
#             )
#             dpg.add_button(
#                 label="Stop", 
#                 width=200,
#                 height=30
#             )
    
#     def _create_right_column(self):
#         """Create right column with plots and controls"""
#         with dpg.child_window(width=900, height=750):
#             self._create_trigger_controls()
#             self._create_plots()
    
#     def _create_trigger_controls(self):
#         """Create trigger source controls"""
#         with dpg.group(horizontal=True):
#             dpg.add_text("Trigger source:")
#             dpg.add_combo(
#                 ["LSL", "Manual", "External"], 
#                 width=100,
#             )
#             dpg.add_button(
#                 label="connect trigger",
#             )
#             dpg.add_text("Time scale:")
#             dpg.add_input_int(
#                 default_value=0, 
#                 width=100,
#             )
#             dpg.add_checkbox(label="Autoscale")
    
#     def _create_plots(self):
#         x_data = np.linspace(0, 4*np.pi, 200)
#         y_data = np.sin(x_data)   
#         for i in range(5):
#                 with dpg.plot(label=f"Sin(x)", height=150, width=-1):
#                     dpg.add_plot_legend()
#                     dpg.add_plot_axis(dpg.mvXAxis, label="x")
#                     with dpg.plot_axis(dpg.mvYAxis, label="sin(x)"):
#                         dpg.add_line_series(x_data.tolist(), y_data.tolist())




import dearpygui.dearpygui as dpg
import numpy as np


class SCOS_UI:
    def __init__(self):
        self.main_window_tag = "main_window"
        self.camera_image_bar_tag = ["K^2_raw", "K^2_1", "K^2_2", "K^2_3", "K^2_4", "K^2_5"]
        self.device_dropDown_tag = "drop_down_device"
        self.connect_device_button_tag = "btn_connect_device"
        self.study_name_editField_tag = "edit_field_study_name"
        self.btn_create_study_tag = "btn_create_study"
        self.current_study_dropDown_tag = "drop_down_current_study"
        self.subject_editField_tag = "edit_field_subject"
        self.run_editField_tag = "edit_field_run"
        self.rate_slider_tag = "slider_rate"
        self.live_image_tag = "live_image"

        
    
    def create_ui(self):
        with dpg.window(label="SCOS Data Acquisition App",
                        tag=self.main_window_tag,
                        width=1260, height=700):
            with dpg.group(horizontal=True):
                self._create_left_column()
                self._create_right_column()

    
    def _create_left_column(self):
        # 1260/2 = 630
        with dpg.child_window(width=620, height=-1):
            self._create_camera_image_panel()

            with dpg.group(horizontal=True):
                self._create_device_study_controls_panel()
                self._create_roi_selection_panel()
        

    def _create_camera_image_panel(self):
        with dpg.group(horizontal=True):
            # create 6 vertical bars
            for i in range(len(self.camera_image_bar_tag)):
                with dpg.plot(label=self.camera_image_bar_tag[i],
                              width=90, height=200):
                    # adding the X-axis
                    dpg.add_plot_axis(dpg.mvXAxis, label="", no_tick_labels=True)
                    # adding the Y-axis
                    dpg.add_plot_axis(dpg.mvYAxis, label="", no_tick_labels=True,
                                      tag=self.camera_image_bar_tag[i])
                    

    def _create_device_study_controls_panel(self):
        with dpg.child_window(width=350, height=-1, border=True):
            
            with dpg.group(horizontal=True):
                dpg.add_text("Device")
                dpg.add_combo(width=80, tag=self.device_dropDown_tag)
                dpg.add_button(width=80, label="connect", tag=self.connect_device_button_tag)
            
            dpg.add_spacer(height=10)
            
            with dpg.group(horizontal=True):
                dpg.add_text("Study") 
                dpg.add_input_text(width=120, tag=self.study_name_editField_tag)
                dpg.add_button(label="Create", width=80, tag=self.btn_create_study_tag)
            
            dpg.add_spacer(height=10)

            with dpg.group(horizontal=True):
                dpg.add_text("Sampling rate")
                dpg.add_slider_float(width=260, tag=self.rate_slider_tag)  


    def _create_roi_selection_panel(self):
        with dpg.child_window(width=260, height=-1, border=True):
            dpg.add_text("ROI Selection")

            with dpg.texture_registry(show=False):
                empty_texture = dpg.add_static_texture(1, 1, [0, 0, 0, 0])
            
            dpg.add_image(empty_texture, width=230, height=200, tag=self.live_image_tag)
            dpg.add_spacer(height=10)
            
            dpg.add_button(label="Preview", width=230, height=30, tag="btn_preview")
            dpg.add_spacer(height=10)

            dpg.add_button(label="Start", width=230, height=30)
            dpg.add_spacer(height=10)

            dpg.add_button(label="Pause", width=230, height=30)
            dpg.add_spacer(height=10)

            dpg.add_button(label="Stop", width=230, height=30)
            dpg.add_spacer(height=10)



    def _create_right_column(self):
        """Create right column with plots and controls"""
        with dpg.child_window(width=-1, height=-1):
            self._create_trigger_controls_panel()
            self._create_plots_panel()


    def _create_trigger_controls_panel(self):
        with dpg.group(horizontal=True):
            dpg.add_text("Trigger source:")
            dpg.add_combo(width=80)
            dpg.add_button(label="connect trigger")
            dpg.add_text("Time scale:")
            dpg.add_input_int(default_value=0, width=80)
            dpg.add_checkbox(label="Autoscale")
    
## below for testing for now!!!
    def _create_plots_panel(self):
        import numpy as np
        
        # Store data for animation
        self.plot_series_tags = []
        self.x_offset = 0
        
        # Create 5 animated plots
        for i in range(5):
            with dpg.plot(label=f"Plot {i+1}", height=130, width=-1):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="x")
                y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="sin(x)")

                series_tag = f"sin_series_{i}"

                # Create empty series (data will be set later)
                dpg.add_line_series([], [], parent=y_axis, tag=series_tag)

                self.plot_series_tags.append(series_tag)

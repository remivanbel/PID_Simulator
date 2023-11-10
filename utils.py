from bokeh.plotting import figure

def make_chart(controller, system_simulator):
    # Establish command list for test run of controller
    command_list = [[0,0], [10,50]]

    # Simulate the controllers response to the command_list
    time_list, signal_list, x, target_list = controller.run_simulation(system_simulator, 50, command_list)

    p = figure(
        title='Stapantwoord',
        x_axis_label='Tijd (s)',
        y_axis_label='Hoogte (m)')

    p.line(time_list, target_list, legend_label="Referentiewaarde", color="red", line_width=2)
    p.line(time_list, x, legend_label="Meetsignaal", color="blue", line_width=2)
    p.legend.location = "bottom_right"

    return p
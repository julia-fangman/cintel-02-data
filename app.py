import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins # This package provides the Palmer Penguins dataset


# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

penguins_df.describe()

column_names = penguins_df.columns.tolist()
print(column_names)

color_mapping = {'Male': 'green', 'Female': 'purple'} 

ui.page_opts(title="Julia's Penguin Data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(penguins_df, x="flipper_length_mm", color="sex", title = "Flipper Length",
                             color_discrete_map=color_mapping)
    
    @render_plotly
    def plot2():
        return px.histogram(penguins_df, x="body_mass_g", color="sex", title="Body Mass",
                             color_discrete_map=color_mapping)

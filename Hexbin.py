# nbi:hide_in

from ipywidgets import interact, interactive, fixed, interact_manual, Layout, SelectMultiple
import ipywidgets as widgets
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
from datetime import datetime as dt
import ipydatetime
import time
import matplotlib.ticker as mticker
import matplotlib
import plotly.express as px
import sys 
import importlib
import os
import subprocess
from multiprocessing import Process
import matplotlib as mpl
import plotly.figure_factory as ff


def hexbin():
    # nbi:hide_in
    start_date_widget = widgets.DatePicker(
        description='Start Date',
        disabled=False) 


    end_date_widget = widgets.DatePicker(
        description='End Date',
        disabled=False
    )

    opts = ['Speed', 'Altitude', 'ir', 'luminosity', 'pm1s', 'pm25s', 'pm10s', 'pm1e', 'pm25e', 'pm10e', 'a03um01Lair', 'a05um01Lair', 'a1um01Lair', 'a25um01Lair', 'a5um01Lair', 'a10um01Lair', 'Co2', 'Temp', 'Hum', 'uv', 'ROH', 'NH4']
    sensor_data_widget = widgets.Select(
        options=opts,
        description='Sensor Data:',
        disabled=False,
        rows=3
        )

    opts1 = ['open-street-map', 'carto-positron','carto-darkmatter','stamen-terrain']
    mapbox_style_widget = widgets.Select(
        options=opts1,
        description='Map Style:',
        disabled=False,
        rows=4
        )

    # nbi:hide_in
    df = pd.read_csv("Lipo.Master.Data.csv")
    #df = pd.read_csv("Lipo.Master.Data.csv")
    #df = pd.read_csv("/home/frakesmart/Desktop/LIPO/june_15_16_17_JULY_17.csv")

    df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y %H:%M:%S.%f')



    start_date_widget = widgets.DatePicker(
        description='Start Date',
        disabled=False
    )


    end_date_widget = widgets.DatePicker(
        description='End Date',
        disabled=False
    )

    opts = ['Speed', 'Altitude', 'ir', 'luminosity', 'pm1s', 'pm25s', 'pm10s', 'pm1e', 'pm25e', 'pm10e', 'a03um01Lair', 'a05um01Lair', 'a1um01Lair', 'a25um01Lair', 'a5um01Lair', 'a10um01Lair', 'Co2', 'Temp', 'Hum', 'uv', 'ROH', 'NH4']
    sensor_data_widget = widgets.Select(
        options=opts,
        description='Sensor Data:',
        disabled=False,
        rows=3
    )
    Speed_widget = widgets.FloatRangeSlider(
        value=[-1.0, 3.0],
        min=-1.0,
        max=3.0,
        step=0.1,
        description='Speed:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.3f',
    )

    Altitude_widget = widgets.FloatRangeSlider(
        value=[-250, 150],
        min=-250,
        max=150.0,
        step=0.1,
        description='Altitude:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    ir_widget = widgets.FloatRangeSlider(
        value=[-1.0, 10000.0],
        min=-1.0,
        max=10000.0,
        step=1.0,
        description='IR:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    luminosity_widget = widgets.FloatRangeSlider(
        value=[-1.0, 50000],
        min=-1.0,
        max=50000,
        step=0.01,
        description='Luminosity:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.5f',
    )

    pm1s_widget = widgets.FloatRangeSlider(
        value=[-1.0, 400.0],
        min=-1.0,
        max=400.0,
        step=1.0,
        description='PM1s:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    pm25s_widget = widgets.FloatRangeSlider(
        value=[-1.0, 600.0],
        min=-1.0,
        max=600.0,
        step=1.0,
        description='PM2.5s:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    pm10s_widget = widgets.FloatRangeSlider(
        value=[-1.0, 600.0],
        min=-1.0,
        max=600.0,
        step=1.0,
        description='PM10s:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    pm1e_widget = widgets.FloatRangeSlider(
        value=[-1.0, 300.0],
        min=-1.0,
        max=300.0,
        step=1.0,
        description='PM1e:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    pm25e_widget = widgets.FloatRangeSlider(
        value=[-1.0, 350.0],
        min=-1.0,
        max=350.0,
        step=1.0,
        description='PM2.5e:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    pm10e_widget = widgets.FloatRangeSlider(
        value=[-1.0, 400.0],
        min=-1.0,
        max=400.0,
        step=1.0,
        description='PM10e:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    a03um01Lair_widget = widgets.FloatRangeSlider(
        value=[-1.0, 53000.0],
        min=-1.0,
        max=53000.0,
        step=1.0,
        description='03um01Lair:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    a05um01Lair_widget = widgets.FloatRangeSlider(
        value=[-1.0, 60000.0],
        min=-1.0,
        max=60000.0,
        step=1.0,
        description='05um01Lair:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    a1um01Lair_widget = widgets.FloatRangeSlider(
        value=[-1.0, 61000.0],
        min=-1.0,
        max=61000.0,
        step=1.0,
        description='1um01Lair:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    a25um01Lair_widget = widgets.FloatRangeSlider(
        value=[-1.0, 42000.0],
        min=-1.0,
        max=42000.0,
        step=0.01,
        description='25um01Lair:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    a5um01Lair_widget = widgets.FloatRangeSlider(
        value=[-1.0, 20000.0],
        min=-1.0,
        max=20000.0,
        step=1.0,
        description='5um01Lair:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    a10um01Lair_widget = widgets.FloatRangeSlider(
        value=[-1.0, 10000.0],
        min=-1.0,
        max=10000.0,
        step=1.0,
        description='10um01Lair:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    Co2_widget = widgets.FloatRangeSlider(
        value=[-1.0, 10000.0],
        min=-1.0,
        max=10000.0,
        step=1.0,
        description='CO2:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    Temp_widget = widgets.FloatRangeSlider(
        value=[-1.0, 70.0],
        min=-1.0,
        max=70.0,
        step=1.0,
        description='Temperature:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    Hum_widget = widgets.FloatRangeSlider(
        value=[-1.0, 100.0],
        min=-1.0,
        max=100.0,
        step=1.0,
        description='Humidity:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    uv_widget = widgets.FloatRangeSlider(
        value=[-0.1, 1.0],
        min=-0.1,
        max=1.0,
        step=0.01,
        description='UV:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.2f',
    )

    ROH_widget = widgets.FloatRangeSlider(
        value=[-1.0, 100.0],
        min=-1.0,
        max=100.0,
        step=1.0,
        description='Alcohol:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )

    NH4_widget = widgets.FloatRangeSlider(
        value=[-1.0, 100.0],
        min=-1.0,
        max=100.0,
        step=1.0,
        description='Nitrate:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )


    # nbi:hide_in
    def sensor_data_parameters(sensordata):
        display(sensor_data_widget)

    def date_parameters(start, end):

        #start = pd.to_datetime('2021/07/13')
        #end = pd.to_datetime('2021/07/31')

        df_date_update = df.loc[(start <= df['Date'].dt.date) & (end >= df['Date'].dt.date)]
        df_date_update.to_csv('date.csv')

    #    df_speed = pd.read_csv('/home/frakesmart/Desktop/LIPO/speed.csv')
    #    fig = px.scatter_mapbox(df_speed, lat="Latitude", lon="Longitude", color="Speed",size="Speed", hover_name="Speed", hover_data=["Speed"],
    #                size_max=15, zoom=12, height=600)
    #    fig.update_layout(mapbox_style="open-street-map")
    #    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


    #    fig.show()
    #    print(df_speed_updated)


    # nbi:hide_in
    def Speed_parameters(speed):

        speedlow = speed[0]
        speedhigh = speed[1]    

        data = pd.read_csv("date.csv")
        df_speed_updated = data[data.Speed.between(speedlow,speedhigh)]
        df_speed_updated.to_csv('speed.csv')
        
        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_speed = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_speed, lat="Latitude", lon="Longitude", nx_hexagon=25,
                    opacity=0.5, labels={"color": "Speed"},show_original_data=True,
                    color="Speed", color_continuous_scale="Icefire", range_color=[0,3], mapbox_style='open-street-map', height=600)
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_speed = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_speed, lat="Latitude", lon="Longitude", nx_hexagon=50,
                    opacity=0.5, labels={"color": "Speed"},show_original_data=True,
                    color="Speed", color_continuous_scale="Icefire", range_color=[0,3], mapbox_style='open-street-map', height=600)
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_speed = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_speed, lat="Latitude", lon="Longitude", nx_hexagon=100,
                    opacity=0.5, labels={"color": "Speed"},show_original_data=True,
                    color="Speed", color_continuous_scale="Icefire", range_color=[0,3], mapbox_style='open-street-map', height=600)
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_speed = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_speed, lat="Latitude", lon="Longitude", nx_hexagon=200,
                    opacity=0.5, labels={"color": "Speed"},show_original_data=True,
                    color="Speed", color_continuous_scale="Icefire", range_color=[0,3], mapbox_style='open-street-map', height=600)
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_speed = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_speed, lat="Latitude", lon="Longitude", nx_hexagon=300,
                    opacity=0.5, labels={"color": "Speed"},show_original_data=True,
                    color="Speed", color_continuous_scale="Icefire", range_color=[0,3], mapbox_style='open-street-map', height=600)
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_speed = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_speed, lat="Latitude", lon="Longitude", nx_hexagon=400,
                    opacity=0.5, labels={"color": "Speed"},show_original_data=True,
                    color="Speed", color_continuous_scale="Icefire", range_color=[0,3], mapbox_style='open-street-map', height=600)
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_speed = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_speed, lat="Latitude", lon="Longitude", nx_hexagon=500,
                    opacity=0.5, labels={"color": "Speed"},show_original_data=True,
                    color="Speed", color_continuous_scale="Icefire", range_color=[0,3], mapbox_style='open-street-map', height=600)
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_speed = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_speed, lat="Latitude", lon="Longitude", nx_hexagon=600,
                    opacity=0.5, labels={"color": "Speed"},show_original_data=True,
                    color="Speed", color_continuous_scale="Icefire", range_color=[0,3], mapbox_style='open-street-map', height=600)
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)


    def Altitude_parameters(altitude):

        altitudelow = altitude[0]
        altitudehigh = altitude[1]    

        data = pd.read_csv("date.csv")
        df_altitude_updated = data[data.Altitude.between(altitudelow,altitudehigh)]
        df_altitude_updated.to_csv('altitude.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_altitude = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_altitude, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "Altitude"},show_original_data=True,
                    color="Altitude", color_continuous_scale="Icefire", range_color=[0,150], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_altitude = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_altitude, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "Altitude"},show_original_data=True,
                    color="Altitude", color_continuous_scale="Icefire", range_color=[0,150], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_altitude = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_altitude, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "Altitude"},show_original_data=True,
                    color="Altitude", color_continuous_scale="Icefire", range_color=[0,150], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_altitude = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_altitude, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "Altitude"},show_original_data=True,
                    color="Altitude", color_continuous_scale="Icefire", range_color=[0,150], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_altitude = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_altitude, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "Altitude"},show_original_data=True,
                    color="Altitude", color_continuous_scale="Icefire", range_color=[0,150], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_altitude = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_altitude, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "Altitude"},show_original_data=True,
                    color="Altitude", color_continuous_scale="Icefire", range_color=[0,150], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_altitude = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_altitude, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "Altitude"},show_original_data=True,
                    color="Altitude", color_continuous_scale="Icefire", range_color=[0,150], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_altitude = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_altitude, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "Altitude"},show_original_data=True,
                    color="Altitude", color_continuous_scale="Icefire", range_color=[0,150], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)


    def ir_parameters(ir):

        irlow = ir[0]
        irhigh = ir[1]    

        data = pd.read_csv("date.csv")
        df_ir_updated = data[data.ir.between(irlow,irhigh)]
        df_ir_updated.to_csv('ir.csv')
        
        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_ir = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ir, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "ir"},show_original_data=True,
                    color="ir", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_ir = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ir, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "ir"},show_original_data=True,
                    color="ir", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_ir = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ir, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "ir"},show_original_data=True,
                    color="ir", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_ir = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ir, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "ir"},show_original_data=True,
                    color="ir", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_ir = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ir, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "ir"},show_original_data=True,
                    color="ir", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_ir = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ir, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "ir"},show_original_data=True,
                    color="ir", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_ir = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ir, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "ir"},show_original_data=True,
                    color="ir", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_ir = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ir, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "ir"},show_original_data=True,
                    color="ir", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)


    def luminosity_parameters(luminosity):

        luminositylow = luminosity[0]
        luminosityhigh = luminosity[1]    

        data = pd.read_csv("date.csv")
        df_luminosity_updated = data[data.luminosity.between(luminositylow,luminosityhigh)]
        df_luminosity_updated.to_csv('luminosity.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_luminosity = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_luminosity, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "luminosity"},show_original_data=True,
                    color="luminosity", color_continuous_scale="Icefire", range_color=[0,50000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_luminosity = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_luminosity, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "luminosity"},show_original_data=True,
                    color="luminosity", color_continuous_scale="Icefire", range_color=[0,50000], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_luminosity = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_luminosity, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "luminosity"},show_original_data=True,
                    color="luminosity", color_continuous_scale="Icefire", range_color=[0,50000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_luminosity = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_luminosity, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "luminosity"},show_original_data=True,
                    color="luminosity", color_continuous_scale="Icefire", range_color=[0,50000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_luminosity = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_luminosity, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "luminosity"},show_original_data=True,
                    color="luminosity", color_continuous_scale="Icefire", range_color=[0,50000], mapbox_style='open-street-map', height=600
                )
                fig.show()
            elif hexagon_widget.value == '400' :
                df_luminosity = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_luminosity, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "luminosity"},show_original_data=True,
                    color="luminosity", color_continuous_scale="Icefire", range_color=[0,50000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_luminosity = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_luminosity, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "luminosity"},show_original_data=True,
                    color="luminosity", color_continuous_scale="Icefire", range_color=[0,50000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_luminosity = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_luminosity, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "luminosity"},show_original_data=True,
                    color="luminosity", color_continuous_scale="Icefire", range_color=[0,50000], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)        


    def pm1s_parameters(pm1s):

        pm1slow = pm1s[0]
        pm1shigh = pm1s[1]    

        data = pd.read_csv("date.csv")
        df_pm1s_updated = data[data.pm1s.between(pm1slow,pm1shigh)]
        df_pm1s_updated.to_csv('pm1s.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_pm1s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1s, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "pm1s"},show_original_data=True,
                    color="pm1s", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_pm1s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1s, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "pm1s"},show_original_data=True,
                    color="pm1s", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_pm1s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1s, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "pm1s"},show_original_data=True,
                    color="pm1s", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_pm1s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1s, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "pm1s"},show_original_data=True,
                    color="pm1s", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_pm1s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1s, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "pm1s"},show_original_data=True,
                    color="pm1s", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_pm1s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1s, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "pm1s"},show_original_data=True,
                    color="pm1s", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_pm1s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1s, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "pm1s"},show_original_data=True,
                    color="pm1s", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_pm1s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1s, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "pm1s"},show_original_data=True,
                    color="pm1s", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)         


    def pm25s_parameters(pm25s):

        pm25slow = pm25s[0]
        pm25shigh = pm25s[1]    

        data = pd.read_csv("date.csv")
        df_pm25s_updated = data[data.pm25s.between(pm25slow,pm25shigh)]
        df_pm25s_updated.to_csv('pm25s.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_pm25s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25s, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "pm25s"},show_original_data=True,
                    color="pm25s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_pm25s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25s, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "pm25s"},show_original_data=True,
                    color="pm25s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_pm25s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25s, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "pm25s"},show_original_data=True,
                    color="pm25s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_pm25s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25s, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "pm25s"},show_original_data=True,
                    color="pm25s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_pm25s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25s, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "pm25s"},show_original_data=True,
                    color="pm25s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_pm25s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25s, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "pm25s"},show_original_data=True,
                    color="pm25s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_pm25s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25s, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "pm25s"},show_original_data=True,
                    color="pm25s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_pm25s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25s, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "pm25s"},show_original_data=True,
                    color="pm25s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)           


    def pm10s_parameters(pm10s):

        pm10slow = pm10s[0]
        pm10shigh = pm10s[1]    

        data = pd.read_csv("date.csv")
        df_pm10s_updated = data[data.pm10s.between(pm10slow,pm10shigh)]
        df_pm10s_updated.to_csv('pm10s.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_pm10s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10s, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "pm10s"},show_original_data=True,
                    color="pm10s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_pm10s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10s, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "pm10s"},show_original_data=True,
                    color="pm10s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_pm10s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10s, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "pm10s"},show_original_data=True,
                    color="pm10s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_pm10s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10s, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "pm10s"},show_original_data=True,
                    color="pm10s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_pm10s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10s, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "pm10s"},show_original_data=True,
                    color="pm10s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_pm10s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10s, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "pm10s"},show_original_data=True,
                    color="pm10s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_pm10s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10s, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "pm10s"},show_original_data=True,
                    color="pm10s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_pm10s = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10s, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "pm10s"},show_original_data=True,
                    color="pm10s", color_continuous_scale="Icefire", range_color=[0,600], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)            


    def pm1e_parameters(pm1e):

        pm1elow = pm1e[0]
        pm1ehigh = pm1e[1]    

        data = pd.read_csv("date.csv")
        df_pm1e_updated = data[data.pm1e.between(pm1elow,pm1ehigh)]
        df_pm1e_updated.to_csv('pm1e.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_pm1e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1e, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "pm1e"},show_original_data=True,
                    color="pm1e", color_continuous_scale="Icefire", range_color=[0,300], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_pm1e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1e, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "pm1e"},show_original_data=True,
                    color="pm1e", color_continuous_scale="Icefire", range_color=[0,300], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_pm1e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1e, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "pm1e"},show_original_data=True,
                    color="pm1e", color_continuous_scale="Icefire", range_color=[0,300], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_pm1e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1e, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "pm1e"},show_original_data=True,
                    color="pm1e", color_continuous_scale="Icefire", range_color=[0,300], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_pm1e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1e, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "pm1e"},show_original_data=True,
                    color="pm1e", color_continuous_scale="Icefire", range_color=[0,300], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_pm1e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1e, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "pm1e"},show_original_data=True,
                    color="pm1e", color_continuous_scale="Icefire", range_color=[0,300], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_pm1e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1e, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "pm1e"},show_original_data=True,
                    color="pm1e", color_continuous_scale="Icefire", range_color=[0,300], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_pm1e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm1e, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "pm1e"},show_original_data=True,
                    color="pm1e", color_continuous_scale="Icefire", range_color=[0,300], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)         


    def pm25e_parameters(pm25e):

        pm25elow = pm25e[0]
        pm25ehigh = pm25e[1]    

        data = pd.read_csv("date.csv")
        df_pm25e_updated = data[data.pm25e.between(pm25elow,pm25ehigh)]
        df_pm25e_updated.to_csv('pm25e.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_pm25e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25e, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "pm25e"},show_original_data=True,
                    color="pm25e", color_continuous_scale="Icefire", range_color=[0,350], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_pm25e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25e, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "pm25e"},show_original_data=True,
                    color="pm25e", color_continuous_scale="Icefire", range_color=[0,350], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_pm25e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25e, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "pm25e"},show_original_data=True,
                    color="pm25e", color_continuous_scale="Icefire", range_color=[0,350], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_pm25e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25e, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "pm25e"},show_original_data=True,
                    color="pm25e", color_continuous_scale="Icefire", range_color=[0,350], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_pm25e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25e, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "pm25e"},show_original_data=True,
                    color="pm25e", color_continuous_scale="Icefire", range_color=[0,350], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_pm25e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25e, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "pm25e"},show_original_data=True,
                    color="pm25e", color_continuous_scale="Icefire", range_color=[0,350], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_pm25e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25e, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "pm25e"},show_original_data=True,
                    color="pm25e", color_continuous_scale="Icefire", range_color=[0,350], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_pm25e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm25e, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "pm25e"},show_original_data=True,
                    color="pm25e", color_continuous_scale="Icefire", range_color=[0,350], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)        


    def pm10e_parameters(pm10e):

        pm10elow = pm10e[0]
        pm10ehigh = pm10e[1]    

        data = pd.read_csv("date.csv")
        df_pm10e_updated = data[data.pm10e.between(pm10elow,pm10ehigh)]
        df_pm10e_updated.to_csv('pm10e.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_pm10e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10e, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "pm10e"},show_original_data=True,
                    color="pm10e", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_pm10e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10e, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "pm10e"},show_original_data=True,
                    color="pm10e", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_pm10e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10e, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "pm10e"},show_original_data=True,
                    color="pm10e", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_pm10e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10e, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "pm10e"},show_original_data=True,
                    color="pm10e", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_pm10e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10e, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "pm10e"},show_original_data=True,
                    color="pm10e", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_pm10e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10e, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "pm10e"},show_original_data=True,
                    color="pm10e", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_pm10e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10e, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "pm10e"},show_original_data=True,
                    color="pm10e", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_pm10e = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_pm10e, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "pm10e"},show_original_data=True,
                    color="pm10e", color_continuous_scale="Icefire", range_color=[0,400], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)         


    def a03um01Lair_parameters(a03um01Lair):

        a03um01Lairlow = a03um01Lair[0]
        a03um01Lairhigh = a03um01Lair[1]    

        data = pd.read_csv("date.csv")
        df_a03um01Lair_updated = data[data.a03um01Lair.between(a03um01Lairlow,a03um01Lairhigh)]
        df_a03um01Lair_updated.to_csv('a03um01Lair.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_a03um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a03um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "a03um01Lair"},show_original_data=True,
                    color="a03um01Lair", color_continuous_scale="Icefire", range_color=[0,53000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_a03um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a03um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "a03um01Lair"},show_original_data=True,
                    color="a03um01Lair", color_continuous_scale="Icefire", range_color=[0,53000], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_a03um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a03um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "a03um01Lair"},show_original_data=True,
                    color="a03um01Lair", color_continuous_scale="Icefire", range_color=[0,53000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_a03um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a03um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "a03um01Lair"},show_original_data=True,
                    color="a03um01Lair", color_continuous_scale="Icefire", range_color=[0,53000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_a03um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a03um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "a03um01Lair"},show_original_data=True,
                    color="a03um01Lair", color_continuous_scale="Icefire", range_color=[0,53000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_a03um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a03um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "a03um01Lair"},show_original_data=True,
                    color="a03um01Lair", color_continuous_scale="Icefire", range_color=[0,53000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_a03um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a03um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "a03um01Lair"},show_original_data=True,
                    color="a03um01Lair", color_continuous_scale="Icefire", range_color=[0,53000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_a03um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a03um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "a03um01Lair"},show_original_data=True,
                    color="a03um01Lair", color_continuous_scale="Icefire", range_color=[0,53000], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)         


    def a05um01Lair_parameters(a05um01Lair):

        a05um01Lairlow = a05um01Lair[0]
        a05um01Lairhigh = a05um01Lair[1]    

        data = pd.read_csv("date.csv")
        df_a05um01Lair_updated = data[data.a05um01Lair.between(a05um01Lairlow,a05um01Lairhigh)]
        df_a05um01Lair_updated.to_csv('a05um01Lair.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_a05um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a05um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "a05um01Lair"},show_original_data=True,
                    color="a05um01Lair", color_continuous_scale="Icefire", range_color=[0,60000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_a05um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a05um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "a05um01Lair"},show_original_data=True,
                    color="a05um01Lair", color_continuous_scale="Icefire", range_color=[0,60000], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_a05um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a05um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "a05um01Lair"},show_original_data=True,
                    color="a05um01Lair", color_continuous_scale="Icefire", range_color=[0,60000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_a05um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a05um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "a05um01Lair"},show_original_data=True,
                    color="a05um01Lair", color_continuous_scale="Icefire", range_color=[0,60000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_a05um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a05um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "a05um01Lair"},show_original_data=True,
                    color="a05um01Lair", color_continuous_scale="Icefire", range_color=[0,60000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_a05um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a05um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "a05um01Lair"},show_original_data=True,
                    color="a05um01Lair", color_continuous_scale="Icefire", range_color=[0,60000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_a05um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a05um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "a05um01Lair"},show_original_data=True,
                    color="a05um01Lair", color_continuous_scale="Icefire", range_color=[0,60000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_a05um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a05um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "a05um01Lair"},show_original_data=True,
                    color="a05um01Lair", color_continuous_scale="Icefire", range_color=[0,60000], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)        


    def a1um01Lair_parameters(a1um01Lair):

        a1um01Lairlow = a1um01Lair[0]
        a1um01Lairhigh = a1um01Lair[1]    

        data = pd.read_csv("date.csv")
        df_a1um01Lair_updated = data[data.a1um01Lair.between(a1um01Lairlow,a1um01Lairhigh)]
        df_a1um01Lair_updated.to_csv('a1um01Lair.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_a1um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a1um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "a1um01Lair"},show_original_data=True,
                    color="a1um01Lair", color_continuous_scale="Icefire", range_color=[0,61000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_a1um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a1um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "a1um01Lair"},show_original_data=True,
                    color="a1um01Lair", color_continuous_scale="Icefire", range_color=[0,61000], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_a1um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a1um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "a1um01Lair"},show_original_data=True,
                    color="a1um01Lair", color_continuous_scale="Icefire", range_color=[0,61000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_a1um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a1um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "a1um01Lair"},show_original_data=True,
                    color="a1um01Lair", color_continuous_scale="Icefire", range_color=[0,61000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_a1um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a1um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "a1um01Lair"},show_original_data=True,
                    color="a1um01Lair", color_continuous_scale="Icefire", range_color=[0,61000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_a1um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a1um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "a1um01Lair"},show_original_data=True,
                    color="a1um01Lair", color_continuous_scale="Icefire", range_color=[0,61000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_a1um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a1um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "a1um01Lair"},show_original_data=True,
                    color="a1um01Lair", color_continuous_scale="Icefire", range_color=[0,61000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_a1um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a1um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "a1um01Lair"},show_original_data=True,
                    color="a1um01Lair", color_continuous_scale="Icefire", range_color=[0,61000], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)        


    def a25um01Lair_parameters(a25um01Lair):

        a25um01Lairlow = a25um01Lair[0]
        a25um01Lairhigh = a25um01Lair[1]    

        data = pd.read_csv("date.csv")
        df_a25um01Lair_updated = data[data.a25um01Lair.between(a25um01Lairlow,a25um01Lairhigh)]
        df_a25um01Lair_updated.to_csv('a25um01Lair.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_a25um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a25um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "a25um01Lair"},show_original_data=True,
                    color="a25um01Lair", color_continuous_scale="Icefire", range_color=[0,42000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_a25um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a25um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "a25um01Lair"},show_original_data=True,
                    color="a25um01Lair", color_continuous_scale="Icefire", range_color=[0,42000], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_a25um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a25um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "a25um01Lair"},show_original_data=True,
                    color="a25um01Lair", color_continuous_scale="Icefire", range_color=[0,42000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_a25um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a25um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "a25um01Lair"},show_original_data=True,
                    color="a25um01Lair", color_continuous_scale="Icefire", range_color=[0,42000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_a25um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a25um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "a25um01Lair"},show_original_data=True,
                    color="a25um01Lair", color_continuous_scale="Icefire", range_color=[0,42000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_a25um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a25um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "a25um01Lair"},show_original_data=True,
                    color="a25um01Lair", color_continuous_scale="Icefire", range_color=[0,42000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_a25um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a25um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "a25um01Lair"},show_original_data=True,
                    color="a25um01Lair", color_continuous_scale="Icefire", range_color=[0,42000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_a25um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a25um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "a25um01Lair"},show_original_data=True,
                    color="a25um01Lair", color_continuous_scale="Icefire", range_color=[0,42000], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)         


    def a5um01Lair_parameters(a5um01Lair):

        a5um01Lairlow = a5um01Lair[0]
        a5um01Lairhigh = a5um01Lair[1]    

        data = pd.read_csv("date.csv")
        df_a5um01Lair_updated = data[data.a5um01Lair.between(a5um01Lairlow,a5um01Lairhigh)]
        df_a5um01Lair_updated.to_csv('a5um01Lair.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_a5um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a5um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "a5um01Lair"},show_original_data=True,
                    color="a5um01Lair", color_continuous_scale="Icefire", range_color=[0,20000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_a5um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a5um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "a5um01Lair"},show_original_data=True,
                    color="a5um01Lair", color_continuous_scale="Icefire", range_color=[0,20000], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_a5um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a5um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "a5um01Lair"},show_original_data=True,
                    color="a5um01Lair", color_continuous_scale="Icefire", range_color=[0,20000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_a5um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a5um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "a5um01Lair"},show_original_data=True,
                    color="a5um01Lair", color_continuous_scale="Icefire", range_color=[0,20000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_a5um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a5um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "a5um01Lair"},show_original_data=True,
                    color="a5um01Lair", color_continuous_scale="Icefire", range_color=[0,20000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_a5um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a5um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "a5um01Lair"},show_original_data=True,
                    color="a5um01Lair", color_continuous_scale="Icefire", range_color=[0,20000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_a5um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a5um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "a5um01Lair"},show_original_data=True,
                    color="a5um01Lair", color_continuous_scale="Icefire", range_color=[0,20000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_a5um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a5um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "a5um01Lair"},show_original_data=True,
                    color="a5um01Lair", color_continuous_scale="Icefire", range_color=[0,20000], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)        


    def a10um01Lair_parameters(a10um01Lair):

        a10um01Lairlow = a10um01Lair[0]
        a10um01Lairhigh = a10um01Lair[1]    

        data = pd.read_csv("date.csv")
        df_a10um01Lair_updated = data[data.a10um01Lair.between(a10um01Lairlow,a10um01Lairhigh)]
        df_a10um01Lair_updated.to_csv('a10um01Lair.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_a10um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a10um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "a10um01Lair"},show_original_data=True,
                    color="a10um01Lair", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_a10um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a10um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "a10um01Lair"},show_original_data=True,
                    color="a10um01Lair", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_a10um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a10um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "a10um01Lair"},show_original_data=True,
                    color="a10um01Lair", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_a10um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a10um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "a10um01Lair"},show_original_data=True,
                    color="a10um01Lair", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_a10um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a10um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "a10um01Lair"},show_original_data=True,
                    color="a10um01Lair", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_a10um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a10um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "a10um01Lair"},show_original_data=True,
                    color="a10um01Lair", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_a10um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a10um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "a10um01Lair"},show_original_data=True,
                    color="a10um01Lair", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_a10um01Lair = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_a10um01Lair, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "a10um01Lair"},show_original_data=True,
                    color="a10um01Lair", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)         


    def Co2_parameters(Co2):

        Co2low = Co2[0]
        Co2high = Co2[1]    

        data = pd.read_csv("date.csv")
        df_Co2_updated = data[data.Co2.between(Co2low,Co2high)]
        df_Co2_updated.to_csv('Co2.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_Co2 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Co2, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "Co2"},show_original_data=True,
                    color="Co2", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_Co2 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Co2, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "Co2"},show_original_data=True,
                    color="Co2", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_Co2 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Co2, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "Co2"},show_original_data=True,
                    color="Co2", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_Co2 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Co2, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "Co2"},show_original_data=True,
                    color="Co2", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_Co2 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Co2, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "Co2"},show_original_data=True,
                    color="Co2", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_Co2 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Co2, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "Co2"},show_original_data=True,
                    color="Co2", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_Co2 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Co2, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "Co2"},show_original_data=True,
                    color="Co2", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_Co2 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Co2, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "Co2"},show_original_data=True,
                    color="Co2", color_continuous_scale="Icefire", range_color=[0,10000], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)         


    def Temp_parameters(Temp):

        Templow = Temp[0]
        Temphigh = Temp[1]    

        data = pd.read_csv("date.csv")
        df_Temp_updated = data[data.Temp.between(Templow,Temphigh)]
        df_Temp_updated.to_csv('Temp.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_Temp = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Temp, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "Temp"},show_original_data=True,
                    color="Temp", color_continuous_scale="Icefire", range_color=[0,70], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_Temp = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Temp, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "Temp"},show_original_data=True,
                    color="Temp", color_continuous_scale="Icefire", range_color=[0,70], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_Temp = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Temp, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "Temp"},show_original_data=True,
                    color="Temp", color_continuous_scale="Icefire", range_color=[0,70], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_Temp = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Temp, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "Temp"},show_original_data=True,
                    color="Temp", color_continuous_scale="Icefire", range_color=[0,70], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_Temp = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Temp, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "Temp"},show_original_data=True,
                    color="Temp", color_continuous_scale="Icefire", range_color=[0,70], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_Temp = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Temp, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "Temp"},show_original_data=True,
                    color="Temp", color_continuous_scale="Icefire", range_color=[0,70], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_Temp = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Temp, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "Temp"},show_original_data=True,
                    color="Temp", color_continuous_scale="Icefire", range_color=[0,70], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_Temp = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Temp, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "Temp"},show_original_data=True,
                    color="Temp", color_continuous_scale="Icefire", range_color=[0,70], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)        


    def Hum_parameters(Hum):

        Humlow = Hum[0]
        Humhigh = Hum[1]    

        data = pd.read_csv("date.csv")
        df_Hum_updated = data[data.Hum.between(Humlow,Humhigh)]
        df_Hum_updated.to_csv('Hum.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_Hum = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Hum, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "Hum"},show_original_data=True,
                    color="Hum", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_Hum = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Hum, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "Hum"},show_original_data=True,
                    color="Hum", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_Hum = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Hum, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "Hum"},show_original_data=True,
                    color="Hum", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_Hum = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Hum, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "Hum"},show_original_data=True,
                    color="Hum", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_Hum = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Hum, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "Hum"},show_original_data=True,
                    color="Hum", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_Hum = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Hum, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "Hum"},show_original_data=True,
                    color="Hum", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_Hum = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Hum, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "Hum"},show_original_data=True,
                    color="Hum", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_Hum = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_Hum, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "Hum"},show_original_data=True,
                    color="Hum", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)        


    def uv_parameters(uv):

        uvlow = uv[0]
        uvhigh = uv[1]    

        data = pd.read_csv("date.csv")
        df_uv_updated = data[data.uv.between(uvlow,uvhigh)]
        df_uv_updated.to_csv('uv.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_uv = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_uv, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "uv"},show_original_data=True,
                    color="uv", color_continuous_scale="Icefire", range_color=[0,1], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_uv = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_uv, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "uv"},show_original_data=True,
                    color="uv", color_continuous_scale="Icefire", range_color=[0,1], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_uv = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_uv, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "uv"},show_original_data=True,
                    color="uv", color_continuous_scale="Icefire", range_color=[0,1], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_uv = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_uv, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "uv"},show_original_data=True,
                    color="uv", color_continuous_scale="Icefire", range_color=[0,1], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_uv = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_uv, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "uv"},show_original_data=True,
                    color="uv", color_continuous_scale="Icefire", range_color=[0,1], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_uv = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_uv, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "uv"},show_original_data=True,
                    color="uv", color_continuous_scale="Icefire", range_color=[0,1], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_uv = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_uv, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "uv"},show_original_data=True,
                    color="uv", color_continuous_scale="Icefire", range_color=[0,1], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_uv = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_uv, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "uv"},show_original_data=True,
                    color="uv", color_continuous_scale="Icefire", range_color=[0,1], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)         


    def ROH_parameters(ROH):

        ROHlow = ROH[0]
        ROHhigh = ROH[1]    

        data = pd.read_csv("date.csv")
        df_ROH_updated = data[data.ROH.between(ROHlow,ROHhigh)]
        df_ROH_updated.to_csv('ROH.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_ROH = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ROH, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "ROH"},show_original_data=True,
                    color="ROH", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_ROH = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ROH, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "ROH"},show_original_data=True,
                    color="ROH", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_ROH = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ROH, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "ROH"},show_original_data=True,
                    color="ROH", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_ROH = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ROH, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "ROH"},show_original_data=True,
                    color="ROH", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_ROH = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ROH, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "ROH"},show_original_data=True,
                    color="ROH", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_ROH = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ROH, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "ROH"},show_original_data=True,
                    color="ROH", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_ROH = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ROH, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "ROH"},show_original_data=True,
                    color="ROH", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_ROH = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_ROH, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "ROH"},show_original_data=True,
                    color="ROH", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)        


    def NH4_parameters(NH4):

        NH4low = NH4[0]
        NH4high = NH4[1]    

        data = pd.read_csv("date.csv")
        df_NH4_updated = data[data.NH4.between(NH4low,NH4high)]
        df_NH4_updated.to_csv('NH4.csv')

        opts1 =  ['25','50','100','200','300','400','500','600']
        hexagon_widget = widgets.Select(
        options=opts1,
        description='Hexagon Size:',
        disabled=False,
        rows=4,
        )

        def hexagon_parameters(hex):
            display(hexagon_widget)
        
        hex = widgets.interactive_output(hexagon_parameters, 
          {'hex': hexagon_widget
          })
        
        def hex_size(hex):
            if hexagon_widget.value == '25' :
                df_NH4 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_NH4, lat="Latitude", lon="Longitude",
                    nx_hexagon=25, opacity=0.5, labels={"color": "NH4"},show_original_data=True,
                    color="NH4", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '50' :
                df_NH4 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_NH4, lat="Latitude", lon="Longitude",
                    nx_hexagon=50, opacity=0.5, labels={"color": "NH4"},show_original_data=True,
                    color="NH4", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
            
            elif hexagon_widget.value == '100' :
                df_NH4 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_NH4, lat="Latitude", lon="Longitude",
                    nx_hexagon=100, opacity=0.5, labels={"color": "NH4"},show_original_data=True,
                    color="NH4", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '200' :
                df_NH4 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_NH4, lat="Latitude", lon="Longitude",
                    nx_hexagon=200, opacity=0.5, labels={"color": "NH4"},show_original_data=True,
                    color="NH4", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '300' :
                df_NH4 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_NH4, lat="Latitude", lon="Longitude",
                    nx_hexagon=300, opacity=0.5, labels={"color": "NH4"},show_original_data=True,
                    color="NH4", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '400' :
                df_NH4 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_NH4, lat="Latitude", lon="Longitude",
                    nx_hexagon=400, opacity=0.5, labels={"color": "NH4"},show_original_data=True,
                    color="NH4", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '500' :
                df_NH4 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_NH4, lat="Latitude", lon="Longitude",
                    nx_hexagon=500, opacity=0.5, labels={"color": "NH4"},show_original_data=True,
                    color="NH4", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
                
            elif hexagon_widget.value == '600' :
                df_NH4 = df
                fig = ff.create_hexbin_mapbox(
                    data_frame=df_NH4, lat="Latitude", lon="Longitude",
                    nx_hexagon=600, opacity=0.5, labels={"color": "NH4"},show_original_data=True,
                    color="NH4", color_continuous_scale="Icefire", range_color=[0,100], mapbox_style='open-street-map', height=600
                )
                fig.show()
        
        
        plotui = widgets.HBox(
                [widgets.VBox(
                    [widgets.Label("Select Hexagon size"), hexagon_widget])], 
                layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between'))
        
        plotout = widgets.interactive_output(
            hex_size, 
          {'hex':hexagon_widget})
            
            
        display(plotout,plotui)         


    # nbi:hide_in
    sensordata_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("Select your preferred Data:"), sensor_data_widget]),
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    speed_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             Speed_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    altitude_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             Altitude_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    ir_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             ir_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    luminosity_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             luminosity_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    pm1s_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             pm1s_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    pm25s_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             pm25s_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    pm10s_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             pm10s_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    pm1e_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             pm1e_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    pm25e_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             pm25e_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    pm10e_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             pm10e_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    a03um01Lair_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             a03um01Lair_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    a05um01Lair_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             a05um01Lair_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    a1um01Lair_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             a1um01Lair_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    a25um01Lair_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             a25um01Lair_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    a5um01Lair_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             a5um01Lair_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    a10um01Lair_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             a10um01Lair_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    Co2_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             Co2_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    Temp_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             Temp_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    Hum_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             Hum_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    uv_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             uv_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    ROH_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             ROH_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    NH4_ui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("2021-07-01 <= YOUR DATE <= 2021-12-31"), start_date_widget, end_date_widget]),
             NH4_widget,
            ], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )


    # nbi:hide_in
    sensordata = widgets.interactive_output(sensor_data_parameters, 
              {'sensordata': sensor_data_widget
              })


    date = widgets.interactive_output(date_parameters, 
              {'start': start_date_widget, 
               'end': end_date_widget
              })

    Speed = widgets.interactive_output(Speed_parameters, 
              {'speed': Speed_widget
              })

    Altitude = widgets.interactive_output(Altitude_parameters, 
              {'altitude': Altitude_widget
              })

    ir = widgets.interactive_output(ir_parameters, 
              {'ir': ir_widget
              })

    luminosity = widgets.interactive_output(luminosity_parameters, 
              {'luminosity': luminosity_widget
              })

    pm1s = widgets.interactive_output(pm1s_parameters, 
              {'pm1s': pm1s_widget
              })

    pm25s = widgets.interactive_output(pm25s_parameters, 
              {'pm25s': pm25s_widget
              })

    pm10s = widgets.interactive_output(pm10s_parameters, 
              {'pm10s': pm10s_widget
              })

    pm1e = widgets.interactive_output(pm1e_parameters, 
              {'pm1e': pm1e_widget
              })

    pm25e = widgets.interactive_output(pm25e_parameters, 
              {'pm25e': pm25e_widget
              })

    pm10e = widgets.interactive_output(pm10e_parameters, 
              {'pm10e': pm10e_widget
              })

    a03um01Lair = widgets.interactive_output(a03um01Lair_parameters, 
              {'a03um01Lair': a03um01Lair_widget
              })

    a05um01Lair = widgets.interactive_output(a05um01Lair_parameters, 
              {'a05um01Lair': a05um01Lair_widget
              })

    a1um01Lair = widgets.interactive_output(a1um01Lair_parameters, 
              {'a1um01Lair': a1um01Lair_widget
              })

    a25um01Lair = widgets.interactive_output(a25um01Lair_parameters, 
              {'a25um01Lair': a25um01Lair_widget
              })

    a5um01Lair = widgets.interactive_output(a5um01Lair_parameters, 
              {'a5um01Lair': a5um01Lair_widget
              })

    a10um01Lair = widgets.interactive_output(a10um01Lair_parameters, 
              {'a10um01Lair': a10um01Lair_widget
              })

    Co2 = widgets.interactive_output(Co2_parameters, 
              {'Co2': Co2_widget
              })

    Temp = widgets.interactive_output(Temp_parameters, 
              {'Temp': Temp_widget
              })

    Hum = widgets.interactive_output(Hum_parameters, 
              {'Hum': Hum_widget
              })

    uv = widgets.interactive_output(uv_parameters, 
              {'uv': uv_widget
              })

    ROH = widgets.interactive_output(ROH_parameters, 
              {'ROH': ROH_widget
              })

    NH4 = widgets.interactive_output(NH4_parameters, 
              {'NH4': NH4_widget
              })


    # nbi:hide_in

    def plot(sensordata):

        if sensor_data_widget.value == "Speed" :
            display(speed_ui,Speed)

        elif sensor_data_widget.value == "Altitude" :
            display(altitude_ui,Altitude)

        elif sensor_data_widget.value == "ir" :
            display(ir_ui,ir)

        elif sensor_data_widget.value == "luminosity" :
            display(luminosity_ui,luminosity)

        elif sensor_data_widget.value == "pm1s" :
            display(pm1s_ui,pm1s)

        elif sensor_data_widget.value == "pm25s" :
            display(pm25s_ui,pm25s)

        elif sensor_data_widget.value == "pm10s" :
            display(pm10s_ui,pm10s)

        elif sensor_data_widget.value == "pm1e" :
            display(pm1e_ui,pm1e)   

        elif sensor_data_widget.value == "pm25e" :
            display(pm25e_ui,pm25e)

        elif sensor_data_widget.value == "pm10e" :
            display(pm10e_ui,pm10e)

        elif sensor_data_widget.value == "a03um01Lair" :
            display(a03um01Lair_ui,a03um01Lair)

        elif sensor_data_widget.value == "a05um01Lair" :
            display(a05um01Lair_ui,a05um01Lair)

        elif sensor_data_widget.value == "a1um01Lair" :
            display(a1um01Lair_ui,a1um01Lair)

        elif sensor_data_widget.value == "a25um01Lair" :
            display(a25um01Lair_ui,a25um01Lair)

        elif sensor_data_widget.value == "a5um01Lair" :
            display(a5um01Lair_ui,a5um01Lair)

        elif sensor_data_widget.value == "a10um01Lair" :
            display(a10um01Lair_ui,a10um01Lair)

        elif sensor_data_widget.value == "Co2" :
            display(Co2_ui,Co2)

        elif sensor_data_widget.value == "Temp" :
            display(Temp_ui,Temp)

        elif sensor_data_widget.value == "Hum" :
            display(Hum_ui,Hum)

        elif sensor_data_widget.value == "uv" :
            display(uv_ui,uv)

        elif sensor_data_widget.value == "ROH" :
            display(ROH_ui,ROH)

        elif sensor_data_widget.value == "NH4" :
            display(NH4_ui,NH4)


    # nbi:hide_in

    plotui = widgets.HBox(
            [widgets.VBox(
              [widgets.Label("Select Sensor Data to Plot"), sensor_data_widget])], 
            layout=Layout(display='flex', flex_flow='row wrap', justify_content='space-between')
        )

    def mapstyle(mapboxstyle):

        if mapbox_style_widget.value == 'carto-positron':
            plotout.close()
            plotui.close()
            carto_positron_style.cartop_mapbox()

        elif mapbox_style_widget.value == 'carto-darkmatter':
            plotout.close()
            plotui.close()
            carto_darkmatter_style.cartod_mapbox()

        elif mapbox_style_widget.value == 'stamen-terrain':
            plotout.close()
            plotui.close()
            stamen_terrain_style.stament_mapbox()

        elif mapbox_style_widget.value == 'open-street-map':
            plotout.close()
            plotui.close()
            open_street_map_style.osm_mapbox()

    plotout = widgets.interactive_output(
            plot, 
              {'sensordata':sensor_data_widget})


    display(plotout, plotui)

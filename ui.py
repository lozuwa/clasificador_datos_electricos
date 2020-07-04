import ipywidgets as widgets
from IPython.display import display

class UI(object):

  DEFAULT_DISABLED = False
  DEFAULT_CONTINUOUS_UPDATE = False
  DEFAULT_ORIENTATION = "horizontal"
  DEFAULT_READOUT = True
  DEFAULT_READOUT_FORMAT = 'd' 
  DEFAULT_READOUT_FORMAT_FLOAT = '.4f'

  @staticmethod
  def create_int_slider(value=None, min=None, max=None, step=None, name=None):
    widget = None
    try:
      widget = widgets.IntSlider(value=value,
                            min=min,
                            max=max,
                            step=step,
                            description="".join([name, ": "]),
                            disabled=UI.DEFAULT_DISABLED,
                            continuous_update=UI.DEFAULT_CONTINUOUS_UPDATE,
                            orientation=UI.DEFAULT_ORIENTATION,
                            readout=UI.DEFAULT_READOUT,
                            readout_format=UI.DEFAULT_READOUT_FORMAT)
    except:
      raise Exception("None value in widget!")
    return widget

  @staticmethod
  def create_float_slider(value=None, min=None, max=None, step=None, name=None):
    widget = None
    try:
      widget = widgets.FloatSlider(value=value,
                        min=min,
                        max=max,
                        step=step,
                        description="".join([name, ": "]),
                        disabled=UI.DEFAULT_DISABLED,
                        continuous_update=UI.DEFAULT_CONTINUOUS_UPDATE,
                        orientation=UI.DEFAULT_ORIENTATION,
                        readout=UI.DEFAULT_READOUT,
                        readout_format=UI.DEFAULT_READOUT_FORMAT_FLOAT)
    except:
      raise Exception("None value in widget!")
    return widget
  

  @staticmethod
  def create_float_text(value=None, name=None):
    widget = None
    try:
      widget = widgets.FloatText(value=value,
                        description="".join([name, ": "]),
                        disabled=UI.DEFAULT_DISABLED)
    except:
      raise Exception("None value in widget!")
    return widget



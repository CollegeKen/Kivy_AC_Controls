from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ListProperty

import slider2


# The widget looks for the kv file of the same name, so if you call your app PlotterApp, make sure the kv file is named
# plotter


class MainView(Widget):
    scale = ListProperty([100, 100])

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.slider.bind(value1=self.on_slider_changed, value2=self.on_slider_changed)

    def on_slider_changed(self, obj, value):
        self.scale[0] = self.slider.value1
        self.scale[1] = self.slider.value2


class SliderApp(App):

    def build(self):
        self.view = MainView()
        return self.view


if __name__ == '__main__':
    SliderApp().run()

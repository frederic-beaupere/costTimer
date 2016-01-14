from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string("""
<Timer>:
        Button:
                text: "addP1"
                on_press: root.addWage("addP1")
        Button:
                text: "addP2"
                on_press: root.addWage("addP2")
        Button:
                text: "addP3"
                on_press: root.addWage("addP3")
        Button:
                text: "addP4"
                on_press: root.addWage("addP4")
        Button:
                text: "addP5"
                on_press: root.addWage("addP5")
        Button:
                text: "addP7"
                on_press: root.addWage("addP7")
        Button:
                text: "addP8"
                on_press: root.addWage("addP8")

        Label:
                id: P1_label
                text: "P1: " + str(root.P1count)
        Label:
                id: P2_label
                text: "P2: " + str(root.P2count)
        Label:
                id: P3_label
                text: "P3: " +  str(root.P3count)
        Label:
                id: P4_label
                text: "P4: " +  str(root.P4count)
        Label:
                id: P5_label
                text: "P5: " +  str(root.P5count)
        Label:
                id: P7_label
                text: "P7: " + str(root.P7count)
        Label:
                id: P8_label
                text: "P8: " + str(root.P8count)

        Button:
                text: "removeP1"
                on_press: root.remWage("remP1")
        Button:
                text: "removeP2"
                on_press: root.remWage("remP2")
        Button:
                text: "removeP3"
                on_press: root.remWage("remP3")
        Button:
                text: "removeP4"
                on_press: root.remWage("remP4")
        Button:
                text: "removeP5"
                on_press: root.remWage("remP5")
        Button:
                text: "removeP7"
                on_press: root.remWage("remP7")
        Button:
                text: "removeP8"
                on_press: root.remWage("remP8")
        Button:
                text: "Timer start"
                on_press: root.timerStart()
        Button:
                text: "Timer stop"
                on_press: root.timerStop()

        Label:
                id: blank00
        Label:
                id: time_label
                text: "elapsed time: " + str(root.seconds)
        Label:
                id: blank01
        Label:
                id: cost_label
                text: "timed cost: " + str(root.accuCost)

""")

wageP1 = 10.0
wageP2 = 20.0
wageP3 = 30.0
wageP4 = 40.0
wageP5 = 50.0
wageP7 = 70.0
wageP8 = 80.0


class Timer(GridLayout):
    running = BooleanProperty(False)
    seconds = NumericProperty(0)
    accuCost = NumericProperty(0)
    P1count = NumericProperty(0)
    P2count = NumericProperty(0)
    P3count = NumericProperty(0)
    P4count = NumericProperty(0)
    P5count = NumericProperty(0)
    P7count = NumericProperty(0)
    P8count = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Timer, self).__init__()
        self.cols = 7

        self.totalHourlyWages = 0
        self.seconds = 0
        self.accuCost = 0.0
        self.P1count = 0
        self.P2count = 0
        self.P3count = 0
        self.P4count = 0
        self.P5count = 0
        self.P7count = 0
        self.P8count = 0

    def timerStart(self, *args):
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update, 1)

    def timerStop(self, *args):
        if self.running:
            self.running = False
            Clock.unschedule(self.update)

    def addWage(self, *args):
        if args[0] == "addP1":
            self.totalHourlyWages += wageP1
            self.P1count += 1
        elif args[0] == "addP2":
            self.totalHourlyWages += wageP2
            self.P2count += 1
        elif args[0] == "addP3":
            self.totalHourlyWages += wageP3
            self.P3count += 1
        elif args[0] == "addP4":
            self.totalHourlyWages += wageP4
            self.P4count += 1
        elif args[0] == "addP5":
            self.totalHourlyWages += wageP5
            self.P5count += 1
        elif args[0] == "addP7":
            self.totalHourlyWages += wageP7
            self.P7count += 1
        elif args[0] == "addP8":
            self.totalHourlyWages += wageP8
            self.P8count += 1
        print(self.totalHourlyWages)

    def remWage(self, *args):
        if args[0] == "remP1" and self.P1count > 0:
            self.totalHourlyWages -= wageP1
            self.P1count -= 1
        elif args[0] == "remP2" and self.P2count > 0:
            self.totalHourlyWages -= wageP2
            self.P2count -= 1
        elif args[0] == "remP3" and self.P3count > 0:
            self.P3count -= 1
            self.totalHourlyWages -= wageP3
        elif args[0] == "remP4" and self.P4count > 0:
            self.P4count -= 1
            self.totalHourlyWages -= wageP4
        elif args[0] == "remP5" and self.P5count > 0:
            self.P5count -= 1
            self.totalHourlyWages -= wageP5
        elif args[0] == "remP7" and self.P7count > 0:
            self.P7count -= 1
            self.totalHourlyWages -= wageP7
        elif args[0] == "remP8" and self.P8count > 0:
            self.P8count -= 1
            self.totalHourlyWages -= wageP8
        print(self.totalHourlyWages)


    def update(self, *args):
        self.seconds += 1
        print(self.seconds)
        print(self.accuCost)
        self.accuCost += int((self.totalHourlyWages / 3600.0) * 100) / 100.0


class CostTimer(App):

    def build(self):
        timer = Timer()
        return timer

if __name__ == "__main__":
    CostTimer().run()
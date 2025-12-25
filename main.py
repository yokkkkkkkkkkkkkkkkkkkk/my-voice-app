from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

KV = '''
MDScreen:
    md_bg_color: [1, 1, 1, 1]
    MDLabel:
        text: "محول الصوت أوفلاين"
        halign: "center"
        pos_hint: {"center_y": .8}
        font_style: "H4"
    
    MDRaisedButton:
        text: "بدء التسجيل والتحويل"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.start_conversion()

    MDLabel:
        id: result_text
        text: "النص سيظهر هنا"
        halign: "center"
        pos_hint: {"center_y": .3}
'''

class OfflineApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def start_conversion(self):
        # هنا سنضع كود استدعاء محرك الأندرويد الداخلي لاحقاً
        self.root.ids.result_text.text = "جاري الاستماع..."

if __name__ == '__main__':
    OfflineApp().run()

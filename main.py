import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from PIL import Image

class FloatingPDFWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 15

        self.add_widget(Label(text="SOLARIS PDF POCKET", font_size='20sp', bold=True, size_hint=(1, 0.1)))

        # Блок камеры
        self.camera = Camera(play=True, resolution=(640, 480), size_hint=(1, 0.6))
        self.add_widget(self.camera)

        # Кнопка Сделать PDF
        btn_snap = Button(
            text="📸 СНЯТЬ И СОХРАНИТЬ В PDF", 
            size_hint=(1, 0.15), 
            background_color=(0.2, 0.7, 0.3, 1),
            font_size='16sp'
        )
        btn_snap.bind(on_press=self.capture_to_pdf)
        self.add_widget(btn_snap)

        self.status_label = Label(text="Готов к съемке", size_hint=(1, 0.1))
        self.add_widget(self.status_label)

    def capture_to_pdf(self, instance):
        try:
            # 1. Сохраняем временно кадр с камеры
            img_path = "/sdcard/Download/temp_scan.png"
            pdf_path = "/sdcard/Download/Scan_Tonya.pdf"
            
            self.camera.export_to_png(img_path)

            # 2. Переводим картинку в PDF через Pillow
            image = Image.open(img_path)
            image_rgb = image.convert('RGB')
            image_rgb.save(pdf_path)

            # Удаляем временный файл
            if os.path.exists(img_path):
                os.remove(img_path)

            self.status_label.text = "✅ Сохранено в Download/Scan_Tonya.pdf!"
        except Exception as e:
            self.status_label.text = f"Ошибка: {str(e)}"

class FloatingPDFApp(App):
    def build(self):
        return FloatingPDFWidget()

if __name__ == "__main__":
    FloatingPDFApp().run()

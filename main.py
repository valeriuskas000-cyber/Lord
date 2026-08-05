
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Тёмный фон интерфейса
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class LordApp(App):
    def build(self):
        self.pin_approved = False
        self.safe = 0.0
        self.nz = 0.0
        self.index = 154

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Заголовок
        self.title_label = Label(
            text="🔒 СИСТЕМА ЛОРДА: ВХОД ЗАБЛОКИРОВАН", 
            font_size='20sp', 
            bold=True,
            color=(1, 0.8, 0, 1)
        )
        self.layout.add_widget(self.title_label)

        # Информационный блок
        self.info_label = Label(
            text="Введите секретный PIN-код:", 
            font_size='16sp'
        )
        self.layout.add_widget(self.info_label)

        # Поле ввода PIN
        self.pin_input = TextInput(
            hint_text="ПИН-код...", 
            password=True, 
            multiline=False, 
            size_hint=(1, 0.4),
            font_size='22sp'
        )
        self.layout.add_widget(self.pin_input)

        # Кнопка подтверждения
        self.btn_action = Button(
            text="Войти", 
            background_color=(0, 0.7, 1, 1),
            size_hint=(1, 0.5),
            font_size='18sp',
            bold=True
        )
        self.btn_action.bind(on_press=self.check_pin)
        self.layout.add_widget(self.btn_action)

        # Статус
        self.status_label = Label(
            text="", 
            font_size='14sp', 
            color=(0.8, 0.8, 0.8, 1)
        )
        self.layout.add_widget(self.status_label)

        return self.layout

    def check_pin(self, instance):
        if not self.pin_approved:
            if self.pin_input.text == "7777":
                self.pin_approved = True
                self.title_label.text = "👑 СИСТЕМА ЛОРДА: ЯДРО АКТИВИРОВАНО"
                self.title_label.color = (0, 1, 0.4, 1)
                self.info_label.text = f"📈 Тек. Индекс: {self.index}  |  Сейф: {self.safe}$"
                
                self.layout.remove_widget(self.pin_input)
                self.layout.remove_widget(self.btn_action)

                self.btn_depo = Button(text="➕ Пополнение (+50$)", background_color=(0, 0.8, 0.2, 1), size_hint=(1, 0.5), font_size='18sp')
                self.btn_depo.bind(on_press=self.add_depo)
                self.layout.add_widget(self.btn_depo)

                self.btn_out = Button(text="💳 Вывод на карту", background_color=(0.9, 0.3, 0.2, 1), size_hint=(1, 0.5), font_size='18sp')
                self.btn_out.bind(on_press=self.make_withdraw)
                self.layout.add_widget(self.btn_out)

                self.status_label.text = "✅ ДОСТУП РАЗРЕШЁН! Добро пожаловать."
            else:
                self.status_label.text = "❌ НЕВЕРНЫЙ ПИН-КОД!"

    def add_depo(self, instance):
        self.safe += 50.0
        self.index -= 7
        self.info_label.text = f"📈 Тек. Индекс: {self.index}  |  Сейф: {self.safe}$"
        self.status_label.text = "⚡ [ВВОД]: +50$ зашло в Сейф!"

    def make_withdraw(self, instance):
        if self.safe > 0:
            self.safe = 0.0
            self.info_label.text = f"📈 Тек. Индекс: {self.index}  |  Сейф: {self.safe}$"
            self.status_label.text = "💸 Средства успешно выведены!"
        else:
            self.status_label.text = "⚠️ Сейф пуст!"

if __name__ == '__main__':
    LordApp().run()

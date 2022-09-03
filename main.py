from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class Money(App):
    def build(self):
        return GUI

    def get_money_value(self, money_name):
        api = requests.get(f"https://economia.awesomeapi.com.br/last/{money_name}-BRL").json()
        return float(api[f"{money_name}BRL"]["bid"])

    def on_start(self):
        self.root.ids["usd"].text = "Dólar: ${:.2f}".format(self.get_money_value("USD"))
        self.root.ids["eur"].text = "Euro: €{:.2f}".format(self.get_money_value("EUR"))
        self.root.ids["eth"].text = "Ethereum: Ξ{:.2f}".format(self.get_money_value("ETH"))
        self.root.ids["btc"].text = "Bitcoin: ₿{:.2f}".format(self.get_money_value("BTC"))

Money().run()
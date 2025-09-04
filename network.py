class Packet:
    def __init__(self, src, dst, data):
        self.src = src  # MAC-адрес отправителя
        self.dst = dst  # MAC-адрес получателя или широковещательный адрес
        self.data = data


class Router:
    def __init__(self):
        self.devices = {}  # mac -> Computer

    def connect(self, device):
        self.devices[device.mac] = device
        print(f"Устройство с MAC {device.mac} подключено к роутеру.")

    def route(self, packet):
        if packet.dst == "FF:FF:FF:FF:FF:FF":
            # Широковещательная рассылка всем, кроме отправителя
            print(f"Широковещательная рассылка от {packet.src}")
            for mac, device in self.devices.items():
                if mac != packet.src:
                    device.receive(packet)
        else:
            recipient = self.devices.get(packet.dst)
            if recipient:
                print(f"Пересылаю пакет от {packet.src} к {packet.dst}")
                recipient.receive(packet)
            else:
                print(f"Ошибка: устройство с MAC {packet.dst} не найдено.")


class Computer:
    def __init__(self, name, mac, router):
        self.name = name
        self.mac = mac
        self.router = router
        self.router.connect(self)

    def send(self, dst_mac, data):
        packet = Packet(src=self.mac, dst=dst_mac, data=data)
        self.router.route(packet)

    def receive(self, packet):
        print(f"{self.name} ({self.mac}) получил сообщение от {packet.src}: {packet.data}")


# Создаём роутер
router = Router()

# Создаём компьютеры с MAC-адресами
PC1 = Computer("PC1", "00:11:22:33:44:55", router)
PC2 = Computer("PC2", "66:77:88:99:AA:BB", router)
PC3 = Computer("PC3", "CC:DD:EE:FF:00:11", router)
PC4 = Computer("PC4", "22:33:44:55:66:77", router)

# Отправка обычных пакетов
PC1.send("CC:DD:EE:FF:00:11", "Привет от PC1!")  # PC1 -> PC3
PC3.send("00:11:22:33:44:55", "Ответ от PC3!")  # PC3 -> PC1
PC2.send("22:33:44:55:66:77", "PC2 здесь.")     # PC2 -> PC4
PC4.send("66:77:88:99:AA:BB", "Принято!")       # PC4 -> PC2

print("\n--- Широковещательная рассылка ---")
# Отправка широковещательного пакета
PC1.send("FF:FF:FF:FF:FF:FF", "Всем привет от PC1!")

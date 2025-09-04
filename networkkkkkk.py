class Packet:
    def __init__(self, src, dst, data):
        self.src = src
        self.dst = dst
        self.data = data


class Computer:
    def __init__(self, name, router):
        self.name = name
        self.router = router
        self.router.connect(self)

    def send(self, dst, data):
        packet = Packet(self.name, dst, data)
        self.router.route(packet)

    def receive(self, packet):
        print(f"Сообщение для {self.name} от {packet.src}: {packet.data}")


class Router:
    def __init__(self):
        self.devices = {}  # словарь: имя -> объект Computer

    def connect(self, device):
        self.devices[device.name] = device

    def route(self, packet):
        recipient = self.devices.get(packet.dst)
        if recipient:
            recipient.receive(packet)
        else:
            print(f"Маршрутизатор: устройство {packet.dst} не найдено.")

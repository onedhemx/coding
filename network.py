class Packet:
    """docstring for Packet"""
    def __init__(self,src , dst, data ):
        self.src = src 
        self.dst = dst
        self.data = data

class Router:
    def __init__(self):
        self.devices = {}
    def connect(device):
        self.devices = True
        print(f"{device} добавлен в словарь")
    def route(packet):
        dst = packet.dst 
        if dst in self.devices:
            print(f"пересылаю пакет {packet.src} в {packet.dst}")
        else:
            print("ошибка, пакет не доставлен")
            
class Computer:
    def __init__(self, name, router):
        self.name = name
        self.router = router
    def send(self, dst, data):
        packet = Packet(src=self.name, dst=dst, data=data)
        self.router.route(packet)

    def receive(self, packet):
        print(f"{self.name} получил сообщение от {packet.src}: {packet.data}")
        

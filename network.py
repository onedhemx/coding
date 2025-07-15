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




router = Router()

PC1 = Computer("PC1", router)
PC2 = Computer("PC2", router)
PC3 = Computer("PC3", router)
PC4 = Computer("PC4", router)

router.connect("PC1", PC1)
router.connect("PC2", PC2)
router.connect("PC3", PC3)
router.connect("PC4", PC4)

class TV:

    def __init__(self):
        self.volume = 0
        self.setCanal(0)

    def setCanal(self, canal):
        if (canal >= 0) and (canal <= 100):
            self.canal = canal

    def aumentaVolume(self):
        if (self.volume < 100):
            self.volume += 1

    def diminuiVolume(self):
        if (self.volume > 0):
            self.volume -= 1

# TESTE DA CLASSE
tv = TV()
print("Canal: %d - Volume: %d" % (tv.canal, tv.volume))
tv.setCanal(10)
print("Canal: %d - Volume: %d" % (tv.canal, tv.volume))
tv.aumentaVolume()
print("Canal: %d - Volume: %d" % (tv.canal, tv.volume))
tv.aumentaVolume()
print("Canal: %d - Volume: %d" % (tv.canal, tv.volume))
tv.aumentaVolume()
print("Canal: %d - Volume: %d" % (tv.canal, tv.volume))
tv.aumentaVolume()
print("Canal: %d - Volume: %d" % (tv.canal, tv.volume))
tv.diminuiVolume()
print("Canal: %d - Volume: %d" % (tv.canal, tv.volume))

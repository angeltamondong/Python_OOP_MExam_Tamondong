class Device:
    room = "Lab 1"

    def __init__(self, asset_tag):
        self.asset_tag = asset_tag


first = Device("D-01")
second = Device("D-02")

Device.room = "Repair bench"
first.room = "Lab 2"
second.room = "Lab 2"

print(Device.room)
print(first.room)
print(second.room)

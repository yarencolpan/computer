class Computer:

    def __init__(self,
                 comp_status="off",
                 ram=16,
                 ssd=512,
                 volume=20,
                 screen_bright=25,
                 wifi="off",
                 connected_network="-",
                 bluetooth="on",
                 desktop_apps=None, ):
        if desktop_apps is None:
            desktop_apps = ["Excel",
                            "Word",
                            "Powerpoint",
                            "Adobe photoshop",
                            "google chrome",
                            "Steam",
                            "Microsoft Outlook",
                            "Adobe Acrobat Reade"]
            self.comp_status = comp_status
            self.ram = ram
            self.ssd = ssd
            self.volume = volume
            self.screen_bright = screen_bright
            self.wifi = wifi
            self.connected_network = connected_network
            self.bluetooth = bluetooth
            self.desktop_apps = desktop_apps

    def __str__(self):
        return "comp_status: {}\n" \
               "ram: {}\n" \
               "ssd: {}\n" \
               "connected_network: {}\n" \
               "volume: {}\n" \
               "screen_bright: {}\n" \
               "wifi: {}\n" \
               "bluetooth: {}\n" \
               "desktop_apps: {}".format(self.comp_status, self.ram, self.ssd, self.volume, self.connected_network,
                                         self.screen_bright, self.wifi, self.bluetooth, self.desktop_apps)

    def __len__(self):
        return len(self.desktop_apps)

    def comp_on(self):
        if self.comp_status == "on":
            print("computer is on")

        elif self.comp_status == "off":
            self.comp_status = "on"
            print("computer is on")

    def comp_off(self):
        if self.comp_status == "off":
            print("computer is off")

        elif self.comp_status == "on":
            self.comp_status = "off"
            print("computer is off")

    def raise_vol(self):
        if self.volume == 100:
            print("volume is max.")

        else:
            self.volume += 1

    def lower_vol(self):
        if self.volume == 0:
            print("volume is min.")

        else:
            self.volume -= 1

    def raise_bright(self):
        if self.screen_bright == 100:
            print("screen bright is max")

        else:
            self.screen_bright += 1

    def lower_bright(self):
        if self.screen_bright == 0:
            print("screen bright is min")

        else:
            self.screen_bright -= 1

    def wifi_connection(self):
        if self.wifi == "on":
            print("wifi is on.")

        else:
            self.wifi = "on"
            print("wifi is on.")

    def disconnect_wifi(self):
        if self.wifi == "off":
            print("Wifi is off.")

        else:
            self.wifi = "off"
            print("Wifi is off.")

    def choose_network(self):
        print("1-SUPERONLINE_WiFi_2389\n2-SUPERONLINE_WiFi_6547\n3-SUPERONLINE_WIFI_6723")

        networks = ["SUPERONLINE_WiFi_2389", "SUPERONLINE_WiFi_6547", "SUPERONLINE_WIFI_6723"]

        choice = int(input("Enter network of number:"))

        self.connected_network = networks[choice-1]
        print("connected")

    def on_bluetooth(self):
        if self.bluetooth == "on":
            print("bluetooth is on.")

        else:
            self.bluetooth = "on"
            print("bluetooth is on.")

    def off_bluetooth(self):
        if self.bluetooth == "off":
            print("bluetooth is off.")

        else:
            self.bluetooth = "off"
            print("bluetooth is off.")

    def open_app(self):
        app_is = int(input("""
        1-"Excel"
        2-"Word"
        3-"Powerpoint"
        4-"Adobe photoshop"
        5-"google chrome"
        6-"Steam"
        7-"Microsoft Outlook"
        8-"Adobe Acrobat Reade"
        
        Enter the number:"""))

        print(self.desktop_apps[app_is-1], "is open")


computer1 = Computer()

print("""
Command prompt

1-To give information press '1'
2-To learn Desktop applications count press'2'
3-To turn on computer press '3'
4-To turn off computer press '4'
5-To raise the volume press '5'
6-To lower the volume press '6'
7-To raise the bright press '7'
8-To lower the bright press '8'
9-To turn on bluetooth press '9'
10-To turn off bluetooth press '10'
11-To open an desktop application press '11'
""")

while True:
    transaction = int(input("Enter the number:"))

    if transaction == 1:
        print(computer1)

    elif transaction == 2:
        print("Desktop applications count", len(computer1))

    elif transaction == 3:
        computer1.comp_on()

    elif transaction == 4:
        computer1.comp_off()

    elif transaction == 5:
        computer1.raise_vol()

    elif transaction == 6:
        computer1.lower_vol()

    elif transaction == 7:
        computer1.raise_bright()

    elif transaction == 8:
        computer1.lower_bright()

    elif transaction == 9:
        computer1.on_bluetooth()

    elif transaction == 10:
        computer1.off_bluetooth()

    elif transaction == 11:
        computer1.open_app()







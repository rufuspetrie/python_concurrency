import threading
import time

class Spouse(threading.Thread):
    def __init__(self, name, partner):
        threading.Thread.__init__(self)
        self.name = name
        self.partner = partner
        self.hungry = True

    def run(self):
        while self.hungry:
            print(f"{self.name} is hungry and wants to eat.")
        if self.partner.hungry:
            print(f"{self.name} is waiting for its partner to eat first")
        else:
            with fork:
                print(f"{self.name} has started eating.")
                time.sleep(5)
                self.hungry = False


fork = threading.Lock()
partner_1 = Spouse("Wife", None)
partner_2 = Spouse("Husband", partner_1)
partner_1.partner = partner_2

partner_1.start()
partner_2.start()
partner_1.join()
partner_2.join()
print("Done.")
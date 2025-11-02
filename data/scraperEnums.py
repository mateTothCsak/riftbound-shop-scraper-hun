from enum import Enum, auto


class Products(Enum):
    SPIRITFORGED_BOOSTER_DISPLAY = "Spiritforged Booster Display"


# (name, website, riftbound path)
class Shops(Enum): 
    META = ("metagames", "https://www.metagames.hu", "/gyujtogetos-kartyajatekok/riftbound-league-of-legends-tcg/")

    def __init__(self, shop_name, website, riftbound_path):
        self.shop_name = shop_name
        self.website = website
        self.riftbound_path = riftbound_path


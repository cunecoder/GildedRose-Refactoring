# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """ Update the quality of each item based on one day by using quality system. """

        # List of items with different quality updating attributes
        diff_quality_items = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Conjured Mana Cake"]
        
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # Decreases quality of normal items by one but never negative
            if item.name not in diff_quality_items and item.quality >0:
                item.quality -= 1
            
            # For brie, conjured items, and passes, increase quality based on guidelines
            else:
                if item.name == "Conjured Mana Cake":
                    item.quality -= 2
                elif item.quality < 50:
                    item.quality += 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        # Increase stage (total=2) pass if 10<days but not over 50 
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        # Incrase stage (total=3) pass if 5<days but not over 50
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            
            

            item.sell_in -= 1

            # Update quality for items passed sell_in date
            if item.sell_in <0:
                if item.name =="Aged Brie" and item.quality < 50:
                        item.quality = item.quality + 1
                elif item.name == "Conjured Mana Cake":
                        item.quality -= 2
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                elif item.quality > 0:
                    item.quality -= 1

    



    # def update_quality(self):
    #     for item in self.items:
    #         # If item isn't brie, backstage pass, or sulfuras AND item quality > 0, subtract 1 quality
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     # Take first quality off this day
    #                     item.quality = item.quality - 1
    #         # Otherwise, if pass, 
    #         else:
    #             if item.quality < 50:
    #                 # Increase bri and stage pass
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     # Increase stage (total=2) pass if 10<days but not over 50 
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     # Incrase stage (total=3) pass if 5<days but not over 50
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         # All items have one less day to sell by, not sulfuras
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1

    #         # If past sell time
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     # NORMAL ITEM If sell_in < 0, take an extra (total=2) quality off
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     # If backstage pass, item quality = 0
    #                     item.quality = item.quality - item.quality
    #             else:
    #                 # If brie and quality !>50, increase quality again (total=2)
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

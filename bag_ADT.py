class Bag(object):
    def __init__(self):
        self.items = list()
        
    def length(self):
        return len(self.items)
    
    def contains(self, item):
        return item in self.items
    
    def add(self, item):
        self.items.append(item)
        print("added:", item)
        
    def remove(self, item):
        
        if item in self.items:
            self.items.remove(item)
            print("removed:",item)
        else: 
            print("there is no item as", item, "in the bag")
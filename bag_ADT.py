class Bag(object):
    def __init__(self):
        self.items = list()
        
    def __iter__(self):
        return _BagIterator(self.items)
        
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

# iterator for the bag_ADT
class _BagIterator(object):
    def __init__(self, ls) -> None:
        self._bag_items = ls
        self._cur_item = 0
        
    # returning reference to the object itself
    def __iter__(self):
        """Return the reference to the object itself"""
        return self
    
    
    def __next__(self):
        """Return the next item in container"""
        if self._cur_item < len( self._bag_items ):
            item = self._bag_items[self._cur_item]
            self._cur_item += 1
            return item
        else:
            raise StopIteration
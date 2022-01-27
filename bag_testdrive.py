from bag_ADT import Bag

myBag = Bag()
myBag.add("sugar")
myBag.add( 1 )
myBag.add( 2 )
myBag.add( 3 )
myBag.add( 4 )
myBag.add( 5 )
myBag.add( 5 )

print(myBag.items)
print("length: ", myBag.length())

myBag.remove(5)
print("length: ", myBag.length())

myBag.remove(5)
myBag.remove(5)
print("length: ", myBag.length())

if myBag.contains(1):
    print("Yes, 1 is in the bag")
else: 
    print("Nope")
    
    
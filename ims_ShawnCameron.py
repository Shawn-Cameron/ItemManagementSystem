rev_names = {}

names = {"WIs" : "small widget",
          "WIm" : "medium widget",
          "Ts" : "small thingamajig",
          "Tl" : "large thingamajig",
          "WAs" : "small watchamacallit"}


descriptions = {"WIs" : "small widget for those basic tasks",
          "WIm" : "medium widget, helps you get things done",
          "Ts" : "small thingamajig, almost like a small widget",
          "Tl" : "large thingamajig for those complicated jobs",
          "WAs" : "small watchamacallit, useful for many tasks"}


prices = {"WIs" : 9.25,
          "WIm" : 12.75,
          "Ts" : 8.50,
          "Tl" : 15.00,
          "WAs" : 8.75}


inventory = {"WIs" : 11,
          "WIm" : 5,
          "Ts" : 21,
          "Tl" : 10,
          "WAs" : 1}


current_purchase = {"WIs" : 0,
          "WIm" : 0,
          "Ts" : 0,
          "Tl" : 0,
          "WAs" : 0}

def space():
  print(" - "*15)

def help(): # runs when called at certian parts of the program
  help_sys = input("Would you like to see the existing items with their codes in the system")
  if help_sys == "y":
    space()
    print(names)
    space()

def key_exists(key):
    if (key in names):
        return 1
    else:
        return 0

def status_message(msg):
    print("")
    print("===> " + msg)
    print("")
    
def generate_rev_names():
  for keyval in names:
    val = names[keyval]
    rev_names[val] = keyval
    return
  
def list_information():
  key = {}
  for a in names:
    b = names[a]
    key[b] = a
  status_message("Displaying information of all items in the system")
  
  for a in names: #prints all the information of each item in the list individually
    b = names[a] # b must equal to the name of the item to allow the key to 
    print("The item code is:",key[b]) # be printed from the temperary dictionary
    print("Name:", names[a])
    print("Discription:",descriptions[a])
    print("The price per item:",prices[a])
    print("There is", inventory[a],"in stock")
    print(current_purchase[a],"of these units have been sold")
    space()  
    
def remove_item():

    id_item = input("Enter the ID value for the item you want to remove: ")
    
    if (key_exists(id_item) == 0):
        status_message("THAT ID DOES NOT EXIST IN THE SYSTEM.  YOU MUST USE AN EXISTING ID!")
        return
    
    else:
        status_message("Good, that ID value is in the system.")

        thename = names[id_item]
        
        del names[id_item]
        del descriptions[id_item]
        del prices[id_item]
        del inventory[id_item]
        del current_purchase[id_item]

        del rev_names[thename]
        
        status_message("Item removed from the system!")
        return

def add_new_item():

    id_new_item = input("Enter the ID value for the new item: ")
    
    if (key_exists(id_new_item) == 1):
        status_message("THAT ID IS ALREADY IN USE IN THE SYSTEM.  YOU MUST USE A NEW ID!")
        return
    
    else:
        status_message("Good, that ID value is not yet in use.")
        name_new_item = input("Enter the name for the new item: ")
        desc_new_item = input("Enter a description for the new item: ")
        price_new_item = float(input("Enter the price (without $ sign) for the new item: "))
        inv_new_item = int(input("Enter the quantity of the new item for the inventory: "))

        names[id_new_item] = name_new_item
        descriptions[id_new_item] = desc_new_item
        prices[id_new_item] = price_new_item
        inventory[id_new_item] = inv_new_item
        current_purchase[id_new_item] = 0

        rev_names[name_new_item] = id_new_item

        status_message("New item added to the system!")
        return

def item_information():
  name = {}
  for a in names:
    b = names[a]
    name[b] = a # switches and stores the dictionary's values and keys in another dictionary

  id_name_item = input("Enter the ID value or name of your item")
  if id_name_item in names:
    space()
    print(names[id_name_item])
    print(descriptions[id_name_item])
    print("The cost of the item is $", prices[id_name_item],". There is",inventory[id_name_item],"in stock")
    
  elif id_name_item in name:#if an existing name is entered this will run
    space()
    print("The id of your item is",name[id_name_item])
    id_new_item = name[id_name_item]
    print(descriptions[id_new_item])
    print("The cost of the item is", prices[id_new_item],"$. There is",inventory[id_new_item],"in stock")
  else:
    print("That item does not exist")

def purchase():
  price = 0
  run = "y"
  items_cart={}
  while run == "y":
    id_bought_item = input("Enter the ID value of the purchasing item")
    if inventory[id_bought_item] == 0:
      print("That item is out of stock")
      continue
    elif key_exists(id_bought_item) == 0:
      print("That item does not exist in the system")
      help()
    else:
      selling = int(input("How many of that item is being bought?"))
      if selling == 0:
        print("Invalid Amount")
      elif selling <= inventory[id_bought_item]:
        amount_items = inventory[id_bought_item]
        amount_items -= selling
        inventory[id_bought_item] = amount_items    #changes value in inventory
        price += prices[id_bought_item] * selling #multiplies the amount of items you are buying by the given price
        current_purchase[id_bought_item] += selling #adds the amount of units being sold to the dictionary
        existing = names[id_bought_item]
        if existing in items_cart:#checks the cart if the item they entered was the same as before 
          del items_cart[existing]# and deletes it to be redefind after
        items_cart[names[id_bought_item]] = current_purchase[id_bought_item]
        print(items_cart)
        run = input("would you like to add another item to your shopping cart")
        if run != "y":
          break
      elif selling > inventory[id_bought_item]:
        print("We only have", inventory[id_bought_item],"in stock at this moment!")
  print ("You have purchased",items_cart)
  print ("Your total is $",price)
        
def increase_stock_of_item():
  x = 0
  while x == 0:#used to create the while loop
    id_item = input("What is the item code of the item")
    if key_exists(id_item) == 1:
      add = int(input("How many of that item are you adding (negative number for removing items)"))
      if add == 0:
        print("Invalid Value")
      else:
        add_items = inventory[id_item] 
        add_items += add 
        inventory[id_item]= add_items #changes the inventory stock of the item
        space()
        print(add,names[id_item]+"s","have been added to the system")
        print("There are currently", add_items ,names[id_item]+"s","in the system")
        break
    else:
      print("Invalid code")
      help()

def edit_item():
  edit = input("Enter the item code. Enter h for help")#asks for the item code for the item you wish edit
  if key_exists(edit) == 1:
    start = input("What are you editing? An items price, discription, item code, or name(P,D,I,N)")
    start = start.upper()
    
    if start == "D":
      descript = input("Enter the new discription")
      descriptions[edit] = descript
      print("The description of",names[edit], "has been changed to", descriptions[edit],)
      
    elif start == "P":
      priceofitem = float(input("Enter the new price of the item"))
      prices[edit] = priceofitem
      print("The price of",names[edit], "has been changed to $", prices[edit],"per item.")
      
    elif start == "N":
      name = {}
      for a in names:
        b = names[a]
        name[b] = a
      nameofitem = input("Enter the new name of your item")
      if nameofitem in name:
        print("That name corresponds to another item name in the system")
      else:
        names[edit] = nameofitem
        print("The name of that item has been changed to",names[edit],)
    
    elif start == "I":
      new_id = input("Enter the new id of the item")
      if key_exists(new_id) == 1:  
        print("That id is already in use")
      else:  
        space()
        
        n = names[edit]     # stores all the original values   
        d = descriptions[edit]
        p = prices[edit]
        i = inventory[edit]
        cp = current_purchase[edit]
        
        names[new_id] = n           # places all the original values in the same
        descriptions[new_id] = d    # dictionary but with the new key
        prices[new_id] = p          
        inventory[new_id] = i
        current_purchase[new_id] = cp
        
        del names[edit]             #deletes the original to get rid of the old key
        del descriptions[edit]
        del prices[edit]
        del inventory[edit]
        del current_purchase[edit]
        
        print("The item code for",n,"has been changed to",new_id)
      
      
  elif edit == "h":
    help()
  else:
    print("That key does not exist in the system")

  
##### MAIN PROGRAM

status_message("Welcome to our inventory system!")
status_message("This is our current inventory")

keep_running = "y"

generate_rev_names() # Generate the reverse names table to allow lookup of item ID by name.

while (keep_running == "y"):
    space()
    print("a or A --> ADD a new item to the system")
    print("cs or CS-->CHANGING STOCK of an item in the system")
    print("r or R --> REMOVE an item from the system")
    print("e or E --> EDIT the info for an item in the system")
    print("i or I --> INFORMATION about an item in the system")
    print("all or ALL --> INFORMATION on ALL items in the system")
    print("p or P --> PURCHASING an item that is in the system")
    print("")
    print("q or Q --> QUIT the system")
    print("")
    
    action = input("Enter one of the above commands: ")
    action = action.upper()

    # Check whether the user wants to exit the system.
    if (action == "Q"):
        break
    
    if ((action != "A") and (action != "R") and (action != "E") and (action != "I")) and action != "P" and action != "CS" and action != "ALL":
        status_message("INVALID COMMAND!")
        continue

    if (action == "A"):
        # Add a new item.
        space()
        add_new_item()

    if (action == "R"):
        # Remove the item from the system.
        space()
        remove_item()
        
    if action == "I":
      space()
      item_information() # checks information of a certian item
      
    if action == "ALL":
      list_information() # shows all the information for all the items in the system
      
    if action == "P":
      space()
      purchase()# purchasing items and lowers stock
      
    if action == "CS":
      space()
      increase_stock_of_item() #increases stock of the item
    
    if action == "E":
      space()
      edit_item()

status_message("Thank you for using the system!  Goodbye!")


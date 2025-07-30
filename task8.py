Menu = ["1. Add Contact", "2. View All Contacts", "3. Search For A Contact", "4. Delete A Contact"]
li_of_contacts = []
def add_contact(): 
  contact = input("Enter the name you want to add/n")
  li_of_contacts.append(contact)
def view_contact():
  print(li_of_contacts)  
def search_contact():
  search = input("Enter the name your are searching for/n")
  if search in li_of_contacts:
    print(f"{search} is available")
  else:
    print(f"{search} doesn't exist")       
def delete_contact():
  del_contact = input("Enter the name of the contact you want to delete/n")
  li_of_contacts.remove(del_contact)
while True:
  print(Menu)
  option = int(input("Choose number of one of the options"))
  if option == 1:
    add_contact()
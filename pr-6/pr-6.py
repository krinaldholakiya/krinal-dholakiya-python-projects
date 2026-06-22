import time

class Entry:
        def __init__(self,entry_text):
            self.entry_text= entry_text
            self.timestamp=time.ctime()
            
        def display(self):
            print(f"[{self.timestamp}]")
            print(self.entry_text)

class JournalManager:
    def __init__(self):
        self.filename="journal.txt"
        self.entries = []  

    def add_entry(self):
        text = input("Enter Your Journal Entry: ")
        new_entry = Entry(text)
        self.entries.append(new_entry)
        print("\n--- Entry Added Successfully! ---\n")

    def view_entries(self):
        if not self.entries:
            print("No Journal Entries Found!\n")
            return
        print("\n--- Your Journal Entries ---")
        for entry in self.entries:
            entry.display()
        print()

    def search_entry(self):
        keyword = input("Enter Keyword To Search: ")
        found = False
        for entry in self.entries:
            if keyword.lower() in entry.entry_text.lower():  # Case-insensitive search
                entry.display()
                found = True
        if not found:
            print(f"No entries found for: {keyword}\n")


manager=JournalManager()

print("\n--------Welcome To Personal Journal Manager!---------\n")
while True:
    print("Please Select an Option:\n")
    print("1.Add a New Entry")
    print("2.View All Entries")
    print("3.Search For an Entry")
    print("4.Delete All Entries")
    print("5.Exit\n")
    
    try:
        choice=int(input("Choose Any Option:"))
    except ValueError:
        print("-------Invalid Input! Please Enter a Number Between 1 and 5.-------")
        continue

    match choice:
        case 1:
            manager.add_entry()
    
        case 2:
            manager.view_entries()
            
        case 3:
            manager.search_entry()
          
        case 4:
            if not manager.entries:
                print("-----NO Journal Entries To Delete-----")
                continue

            delete=input("Are You Sure,You Want To Delete All Entries (Yes/No) :")

            match delete.lower():

                case "yes":
                    manager.entries.clear()
                    print("-----All Journal Entries Have Been Deleted Successfully!-----")

                case "no":
                    print("Ok, I Didn't Delete Any Entries.\n")
           
        case 5:
            print("-----Thank You For Using Personal Journal Manager-----")
            break           
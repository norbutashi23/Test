from queue import LifoQueue


backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

#visit function
NoOfVisits = int(input("enter the number of url history: "))
print("enter URLs to visit: ")
for i in range(NoOfVisits):
    url = input("URL: ")
    print(f"Visiting {url}")
    backward_history.put(current_page)
current_page = url

#display current page
print(f"current page: {current_page}")

#go back
while input("do you want to go back? (yes/no): ").lower() == 'yes' :
    if not backward_history.empty():
        forward_history.put(current_page)
        print(f"going back to {current_page}")
    else:
        print("N0 previous page available")    

#go forward                
while input("do you want to go forward? (yes/no): ").lower() == 'yes' :
    if not forward_history.empty():
        forward_history.put(current_page)
        print(f"going forward to {current_page}")
    else:
        print("N0 forward page available")
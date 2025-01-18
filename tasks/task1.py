from queue import Queue

requests = Queue()
order_id = 1

def generate_request():
    request = f"Order: id={order_id}"
    requests.put(request)
    print(f"Order with id={order_id} added")

def process_request():
    if requests.empty():
        print("There are no orders")
        return
    
    order = requests.get()
    print(f"Request for [{order}] was closed")

for i in range(5):
    generate_request()
    order_id += 1
    process_request()

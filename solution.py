"""
Kogan Coding Challenge
	This program prints average cubic weight for all products in the "Air Conditioners" category taken from API endpoint.
Args:
	q: Queue data structure storing URLs for processing
	threadsNum: Number of threads that are running, specified by the user/programmer
	tLock: Primitive threading lock object
	weightSum: Total weight of products falling into "Air Conditioners" category
	cnt: Total number of products falling into "Air Conditioners" category
	convRate: Industry standard cubic weight conversion factor given
	baseUrl: Given base Url before pagination
	worker: A running thread
	pag: A page url that is to be appended to baseUrl and parsed from API json. First page url is initially given.
	req: Response content got from API to be encoded

Returns:
	Average cubic weight
"""
import requests, threading
from queue import Queue

def getAirCons(q):
	global weightSum, cnt
	while True:
		pag = q.get(block=True) #block = True. Otherwise, we get exception for processing None value. That means blocking untill we get an item from queue.
		req = requests.get(baseUrl + pag).json() 
		if req["next"]: # If next url is not None, it is put in queue for processing immediately by other available threads.
			q.put(req["next"]) 
		for obj in req["objects"]:
			if obj["category"] == "Air Conditioners":
				tLock.acquire() # Getting up-to-date weightSum and cnt values
				weightSum += obj["size"]["width"] * obj["size"]["length"] * obj["size"]["height"] * convRate * 10 ** -6 # Multiplied by 10 ** -6 due to centimeter to meter conversion of cubic block
				cnt += 1
				tLock.release() 
		q.task_done() 
			
if __name__ == "__main__":
	q = Queue()
	q.put("/api/products/1") # initial url to be processed put into queue
	threadsNum = 10 # can be specified related to machine's memory and thread's stack size
	tLock = threading.Lock()
	weightSum = cnt = 0
	convRate = 250
	baseUrl = "http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com"

	#initializing threads
	for i in range(threadsNum):
		worker = threading.Thread(target=getAirCons, args=(q,), daemon=True) # setting daemon to True for script keeps running after no alive non-daemon threads are left.
		worker.start()

	# Waiting for the queue to be empty, indicating all URLs are processed.
	q.join()
	print("Average cubic weight for all products in the Air Conditioners category is {:.2f} kg.".format(cnt and weightSum / cnt))

import requests, threading
from queue import Queue

def getAirCons(q):
	global weightSum, cnt
	while True:
		pag = q.get(block=True)
		req = requests.get(baseUrl + pag).json()
		if req["next"]:
			q.put(req["next"])
		for obj in req["objects"]:
			if obj["category"] == "Air Conditioners":
				tLock.acquire()
				weightSum += obj["size"]["width"] * obj["size"]["length"] * obj["size"]["height"] * convRate * 10 ** -6
				cnt += 1
				tLock.release()
		q.task_done()
			
if __name__ == "__main__":
	q = Queue()
	q.put("/api/products/1")
	threadsNum = 10
	tLock = threading.Lock()
	weightSum = cnt = 0
	convRate = 250
	baseUrl = "http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com"

	for i in range(threadsNum):
		worker = threading.Thread(target=getAirCons, args=(q,), daemon=True)
		worker.start()

	q.join()
	print("Average cubic weight for all products in the Air Conditioners category is {:.2f} kg.".format(cnt and weightSum / cnt))

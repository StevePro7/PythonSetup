Comparing requests, aiohttp, and httpx: Which HTTP client should you use?
06-Jun-2025

https://leapcell.medium.com/comparing-requests-aiohttp-and-httpx-which-http-client-should-you-use-6e3d9ff47b0e

Ex01    Sending Requests with requests  sync
Ex02    Sending Requests with httpx     sync
Ex03    Sending Requests with httpx     async
Ex04    Sending Requests with aiohttp   async

Performance Test: Time Consumption of Sending 100 Requests
Ex05    Without Keeping the Connection  sent 3 requests, cost: 2.1332383155822754
Ex06    Keeping the Connection          sent 3 requests, cost: 1.62925124168396 
Ex07    httpx Synchronous Mode  sync    sent 3 requests, cost: 3.556018114089966
Ex08    httpx Synchronous Mode  async   sent 3 requests, cost: 1.030292272567749        only once
Ex09    httpx Synchronous Mode  async   sent 3 requests, cost: 2.0491294860839844       everytime
Ex10    aiohttp create ClientSession()  sent 3 requests, cost: 0.9784464836120605       only once
Ex11    aiohttp create ClientSession()  sent 3 requests, cost: 0.9784464836120605       
everytime
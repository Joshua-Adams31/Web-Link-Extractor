# Web-Link-Extractor
Notes


I assumed that we couldn't use any external libraries since we wnated it frictionless. So I used Python's built in libraries which I've only done a handful of times. Another way I could've solved this would have been to use Beautiful Soup and/or Selenium. I wasn't clear on how we should seperate Producer and Consumer so I just wrote it on one file. I have some print statements commented out at the bottom of the code that will print the links extracted, otherwise they are just saved in their respected lists.

Design Thoughts


I created the HTMLParser class to handle the extractions with the links I fed it. I then recieved the links(Assumed they came in a comma sperated list) from user input and added them into a queue. I then popped from the queue until it was empty, taking each url and running it through my parser. The code should be able to handle a bad url fetch as I've put the action of fetching in a try/catch. In the case of a bad url, I've also created a seperate list to keep track of the urls that didn't work. 

Requirements 


1) I didn't separate producer and consumer so the whole file runs concurrently
2) I can handle a bad fetch, but not too sure about going about handling a bad parse?
3) I have only ever written test cases in Java and I'm unsure on how to do that in Python. I did my own tests inputing different websites such as (https://www.google.com, https://example.com/, google sheets). 
4) Link sent to Joe

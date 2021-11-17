# kafka-consumer-debugger
A Python script for debugging Kafka consumers to get the offset of affected messages.

<b>Helps with finding errors related to: Unexpected error code 2 while fetching data </b>

The error seems to come up when you have saturated your server's I/O.


##How to run:

`python3 debugger.py`

##Other

Helpful to debug Kafka issues from Java as well since the error output is slightly different (helps with subsequent Google searches)

Loosely based on:

https://gist.github.com/bepcyc/545e261603b7364f76b5155eb99243bf


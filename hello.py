def hello_world():
	return "Hello World!"
def hello_world_n(N):
	Hello_W = ''
	if N != 0:
		Hello_W = 'Hello World!'
		while N != 1:
			N -= 1
			Hello_W = Hello_W + ' Hello World!'
	return Hello_W
print(hello_world_n(3))
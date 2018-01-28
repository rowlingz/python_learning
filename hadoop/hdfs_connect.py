import hdfs

client = hdfs.Client("http://120.0.01:50070")

print(client.list("/", status=False))

client.makedirs("/test/local")
print("end")



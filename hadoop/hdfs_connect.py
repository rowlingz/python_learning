import hdfs


# 返回指定目录下的目录列表
def file_list(client, hdfs_path):
    print(client.list(hdfs_path, status=False))
# print(client.list("/", status=False))


# 读取hdfs 文件内容，按行读取返回
def read_hdfs_file(client, filename):
    lines = []
    with client.read(filename, encoding='utf-8') as reader:
        for line in reader:
            lines.append(line.strip())
    return lines


# 创建目录
def make_dirs(client, hdfs_path):
    client.makedirs(hdfs_path)


# 删除hdfs文件
def delete_hdfs_file(client, hdfs_path):
    client.delete(hdfs_path)


# 上传文件
def upload_to_hdfs(client, local_path, hdfs_path):
    client.upload(hdfs_path, local_path)


# 获取hdfs文件到本地
def get_from_hdfs(client, loca_path, hdfs_path):
    client.download(hdfs_path, loca_path)


# 追加数据到hdfs文件
def write_to_hdfs(client, hdfs_path, data):
    client.write(hdfs_path, data, )


if __name__ == '__main__':
    client = hdfs.Client("localhost:50070")
    file_list(client, '/test')
    # print(read_hdfs_file(client, '/test/file_a'))
    # make_dirs(client, '/test/localtest')
    # delete_hdfs_file(client, '/test/local')
    # upload_to_hdfs(client, "/home/mk.txt", "/test")
    get_from_hdfs(client, "C:\python_project\\test", "/test/file_a")
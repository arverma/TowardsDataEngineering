URI = sc._gateway.jvm.java.net.URI
Path = sc._gateway.jvm.org.apache.hadoop.fs.Path
FileSystem  = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
Configuration = sc._gateway.jvm.org.apache.hadoop.conf.Configuration
fs = FileSystem.get(URI("hdfs://<name_node>"), Configuration())

file_metadata = []
status = fs.listStatus(Path('.'))
for fileStatus in status:
    file_metadata.append((fileStatus.getPath().toString(), fileStatus.getModificationTime()))
file_metadata.sort(key=lambda x: x[1])
srcPath = file_metadata[-1][0]

destPath= Path("aman.csv")

if(fs.exists(srcPath) and fs.isFile(srcPath)):
  fs.rename(srcPath,destPath)
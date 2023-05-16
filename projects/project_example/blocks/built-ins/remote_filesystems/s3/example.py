from prefect.filesystems import RemoteFileSystem

block = RemoteFileSystem(basepath="s3://my-bucket/folder/")
block.save("dev")

from prefect.filesystems import GitHub

block = GitHub(
    repository="https://github.com/my-repo/",
    access_token=<my_access_token> # only required for private repos
)
block.get_directory("folder-in-repo") # specify a subfolder of repo
block.save("dev")


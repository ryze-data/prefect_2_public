from prefect.filesystems import GitHub

# register filesystem

block = GitHub(
    repository="https://github.com/ryze-data/prefect_2_public/"
     # only required for private repos
)
block.get_directory("projects/dev") # specify a subfolder of repo
block.save("development")


# register infrastructure

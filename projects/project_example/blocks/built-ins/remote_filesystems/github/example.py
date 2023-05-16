from prefect.filesystems import GitHub

block = GitHub(
    repository="https://github.com/ryze-data/prefect_2_public/"",
    # access_token=<my_access_token> # only required for private repos
)
block.get_directory("projects/project_example"") # specify a subfolder of repo
block.save("project_example")


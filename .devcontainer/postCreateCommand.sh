echo '# Add /home/ubuntu/.local/bin to PATH. Note this is where pipp3 for py3.11 install packages'
echo '# Add local bin to PATH' >> ~/.bashrc && echo 'export PATH="$PATH:/home/ubuntu/.local/bin"' >> ~/.bashrc && \
source ~/.bashrc && \
echo '# Install Python 3.11 ' && \
sudo apt update -y && \
sudo apt upgrade -y && \
sudo apt install software-properties-common && \
sudo add-apt-repository -y ppa:deadsnakes/ppa && \
sudo apt update -y && \
sudo apt install python3.11 -y && \
sudo apt update -y && \
sudo apt install python3.11-distutils -y && \
echo '# Install pip for python3.11 ' && \
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 && \
echo '# Install prefect and dependency packages ' && \
python3.11 -m pip install prefect==2.16.9 --upgrade && \
python3.11 -m pip install prefect-shell==0.2.4 prefect-github==0.2.4 prefect-dbt[snowflake]==0.4.3 prefect-dask==0.2.8 prefect-snowflake==0.27.5 --upgrade && \
python3.11 -m pip install pydantic==1.10.6 --upgrade && \
python3.11 -m pip install pyopenssl==24.1.0 --upgrade && \
python3.11 -m pip install boto3==1.34.98 --upgrade && \
python3.11 -m pip install azure-core==1.30.1 azure-cosmos==4.6.0 azure-identity==1.16.0 azure-storage-blob==12.19.1 --upgrade && \
python3.11 -m pip install dbt-snowflake==1.7.3 --upgrade && \
python3.11 -m pip install pyodbc==5.1.0 pymongo==4.7.1  pycurl==7.45.3 --upgrade && \
python3.11 -m pip install "snowflake-connector-python[pandas]==3.10.0" --upgrade && \
echo '# install dev linter/formatters and unit testing frameworks' && \
python3.11 -m pip install ruff sqlfluff isort pylint pre-commit pytest && \
source ~/.bashrc && \
echo 'BUG: Installing AWS cli : asks me for a password when installing ' && \
sudo apt update -y && \
sudo apt install unzip && \
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
unzip awscliv2.zip && \
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli && \
rm -rf ./awscliv2.zip && \
rm -rf ./aws && \
echo 'Manuall Install form dev container (issue:E: Unable to locate package msodbcsql17 ): Installing mssql tools ODBC and bcp  ' && \
sudo apt update -y && \
curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc && \
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list && \
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools && \
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc && \
echo 'export PATH="$PATH:/opt/mssql-tools/bin/bcp"' >> ~/.bashrc && \
source ~/.bashrc && \
echo 'Installing mongo database tools  ' && \
curl -O https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2204-x86_64-100.9.0.deb && \
sudo apt install ./mongodb-database-tools-*-100.9.0.deb && \
sudo rm mongodb-database-tools-ubuntu2204-x86_64-*.deb && \
echo 'Installing powershell  ' && \
wget https://github.com/PowerShell/PowerShell/releases/download/v7.3.12/powershell_7.3.12-1.deb_amd64.deb && \
sudo dpkg -i powershell_7.3.12-1.deb_amd64.deb && \
sudo apt-get install -f && \
rm powershell_7.3.12-1.deb_amd64.deb && \
sudo apt-get clean && \
sudo rm -rf /var/lib/apt/lists/*

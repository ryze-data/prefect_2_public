# Prefect Services

## Creating Services (sudo)

```
sudo vi /etc/systemd/system/prefect-server.service
```

```bash
[Unit]
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
User=ubuntu
ExecStart=prefect server start
Restart=always
RestartSec=90

[Install]
WantedBy=multi-user.target
```

```
sudo vi /etc/systemd/system/prefect-worker-local-default.service
```

```bash 
[Unit]
Description=Prefect Worker work pool wp-local-process for work-queue default
After=prefect-server.service
StartLimitIntervalSec=0

[Service]
Type=simple
User=ubuntu
ExecStart=prefect worker start --pool "local-work-pool" --work-queue "default"
Restart=always
RestartSec=90

[Install]
WantedBy=multi-user.target
```

## Checking Status of Services

```bash
sudo systemctl status prefect-server;
```

```bash
sudo systemctl status prefect-worker-local-default;
```

## Operating Services
Enable services

```bash
sudo systemctl status prefect-server;
```

```bash
sudo systemctl start prefect-server;
```

```bash
sudo systemctl enable prefect-server;
```

```bash
sudo systemctl status prefect-server;
```

```bash
sudo systemctl status prefect-worker-local-default;
```

```bash
sudo systemctl start prefect-worker-local-default;
```

```bash
sudo systemctl enable prefect-worker-local-default;
```

```bash
sudo systemctl status prefect-worker-local-default;
```

Disable services

```bash
sudo systemctl status prefect-worker-local-default;
```

```bash
sudo systemctl stop prefect-worker-local-default;
```

```bash
sudo systemctl disable prefect-worker-local-default;
```

```bash
sudo systemctl status prefect-worker-local-default;
```

```bash
sudo systemctl status prefect-server;
```

```bash
sudo systemctl stop prefect-server;
```

```bash
sudo systemctl disable prefect-server;
```

```bash
sudo systemctl status prefect-server;
```


echo 'export PATH=$PATH:/home/ubuntu/.local/bin' >> ~/.bashrc
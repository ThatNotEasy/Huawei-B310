#!/bin/bash

# Remote SSH command to create a tar archive
ssh -p 22 root@192.168.8.1 "cd /app/webroot/WebApp/common/ && tar czf meowing.tar.gz *"

# SCP to copy the archive to the local machine (adjust the destination path as needed)
scp -P 22 root@192.168.8.1:/app/webroot/WebApp/common/meowing.tar.gz /Desktop

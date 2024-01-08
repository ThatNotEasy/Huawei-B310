#!/bin/bash

# Remote SSH command to create a tar archive
ssh -p 22 root@192.168.8.1 "cd /online/AIO_LoveTacome/GUI && tar czf archive.tar.gz *"

# SCP to copy the archive to the local machine (adjust the destination path as needed)
scp -P 22 root@192.168.8.1:/online/AIO_LoveTacome/GUI/archive.tar.gz /path/to/local/directory

# Azure Virtual Machine

## Portal exploration

1. Sign in to https://portal.azure.com/.
2. Search for **Virtual machines**.
3. Open your existing learning VM if you have one.
4. Inspect **Overview**, **Size**, **Disks**, **Networking**, and **Monitoring**.
5. Record its region, image, size, and power state. Do not publish subscription IDs or sensitive IP details.
6. If you already have an Ubuntu VM, connect using SSH and run:

```bash
uname -a
lsb_release -a
free -h
df -h
uptime
```

These commands show kernel/OS details, memory, disk capacity, and system uptime.

## Verification

Confirm that the VM is running and that SSH works. Do not create another VM just for this activity if you can reuse your existing lab VM.

## Security

Use SSH public-key authentication. Restrict inbound SSH (TCP 22) to your own current public IP where possible. Never share your private key.

## Evidence

- [ ] VM Overview screenshot with sensitive details hidden.
- [ ] Record VM size, region, OS, and power state.
- [ ] Record the Linux command outputs without sensitive information.

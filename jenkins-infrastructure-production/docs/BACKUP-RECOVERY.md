# Backup and Recovery

## Backup

Backups are performed daily via a systemd timer. The backup script is located at `scripts/backup.sh`.

The backup script will:

1.  Create a timestamped directory in the backup destination.
2.  Create a tarball of the Jenkins home directory.
3.  Create a tarball of the shared workspace.
4.  Prune backups older than 7 days.

## Recovery

To restore from a backup, run the disaster recovery script with the timestamp of the backup you want to restore:

```bash
./scripts/disaster-recovery.sh <backup_timestamp>
```

#!/bin/bash

# Backup script for ItsFyn data

# Set backup directory
BACKUP_DIR="backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

echo "Starting backup process..."

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Backup configuration
echo "Backing up configuration..."
tar -czf "$BACKUP_DIR/config_$TIMESTAMP.tar.gz" config/

# Backup logs
echo "Backing up logs..."
tar -czf "$BACKUP_DIR/logs_$TIMESTAMP.tar.gz" logs/

# Backup user data
echo "Backing up user data..."
tar -czf "$BACKUP_DIR/data_$TIMESTAMP.tar.gz" data/

echo "Backup complete! Files saved in $BACKUP_DIR"

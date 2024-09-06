
## 
## 
## Staging and Cleanup 
## 

# Stage Screen shots older than 5 weeks
# Delete Staged screen shots older than 5 weeks
0 7 * * 1 $_ws_cron/cleanup-screenshots.sh

# Delete any content in tmp older than a week
10 7 * * 1 $_ws_cron/cleanup-old-tmp.sh

# Backup workspace every week
0 8 * * 1 $_ws_cron/backup-workspace.sh
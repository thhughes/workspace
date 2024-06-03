
## 
## 
## Staging and Cleanup 
## 

# Stage any screenshots older than 1 week 
0 7 * * 1 $_ws_cron/cleanup-screenshots.sh

# Stage all tmp content older than 1 week
10 7 * * 1 $_ws_cron/cleanup-old-tmp.sh

# Purge all content older than 1 week in Staging 
0 8 * * 1 $_ws_cron/purge-staging-directory.sh
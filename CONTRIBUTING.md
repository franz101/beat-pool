python pre-processing.py
npx quartz build
cd public; find . -type f -name "*.html" -exec gzip {} \;
cd public; find . -type f -name "*.js" -exec gzip {} \;
cd public; find . -type f -name "*.json" -exec gzip {} \;
rclone copy public r2demo:beat-pool
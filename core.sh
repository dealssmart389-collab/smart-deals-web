#!/bin/bash
./evolve.sh
find . -name "*.tmp" -type f -delete
git remote set-url origin https://ghp_MGcabXzq9CopdyfsvlcwT3biTYKcfO0DDqwH@github.com/dealssmart389-collab/smart-deals-web.git
git add .
git commit -m "System Evolution: $(date)"
git push origin main
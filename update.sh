#!/bin/bash
git add .
git reset .ssh/
git commit -m "Update $(date)"
git push origin main
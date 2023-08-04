#!/bin/bash
cd /mnt/d/saves
git add -A
git commit -m "daily backup: $(date)"
git push
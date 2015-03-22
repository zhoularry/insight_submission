# !/usr/bin/bash


export PYTHONPATH=$PYTHONPATH:/zhoularry/insight_submission
python -c "import sys; print sys.path"

python wordcount_challenge.py
python median_challenge.py
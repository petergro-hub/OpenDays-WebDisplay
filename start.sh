#!/bin/bash
python app.py &
python app_latest.py &
trap 'kill $(jobs -p)' EXIT
wait

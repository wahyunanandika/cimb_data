#!/bin/bash
gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app

#!/bin/bash

cleanup $_ws_ss 35 --stage $_ws_staged/screenshots --use-case ss_migrate --log-dir $_ws_staged/logs
cleanup $_ws_staged/screenshots 35 --use-case ss_staged --log-dir $_ws_staged/logs
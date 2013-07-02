#!/usr/bin/env bash
ls -l | awk '{print $1, $3, $5}'

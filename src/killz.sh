#!/bin/sh
w -sh | awk '{print $1}' | uniq

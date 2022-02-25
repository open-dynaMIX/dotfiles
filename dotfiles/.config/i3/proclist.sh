#!/usr/bin/bash

ps axo %cpu,%mem,pid,comm --sort=-pcpu | head -n 6

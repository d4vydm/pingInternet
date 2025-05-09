#!/bin/bash

while true; do
    read -p "Enter command: " cmd
    if [[ "$cmd" == "ping internet" ]]; then
        echo "Pinging 8.8.8.8..."
        ping -c 4 8.8.8.8
    elif [[ "$cmd" == "exit" ]]; then
        echo "Exiting."
        break
    else
        echo "Unknown command. Try 'ping internet' or 'exit'."
    fi
done

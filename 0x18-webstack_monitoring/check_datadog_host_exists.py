#!/usr/bin/env bash

# Check if a Datadog host exists
# Usage: ./check_datadog_host_exists.sh <host_name>

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <host_name>"
    exit 1
fi

# Extract host name from the command line argument
host_name="$1"

# Check if the host exists in Datadog
if datadog-agent status | grep -q "$host_name"; then
    echo "Host exists"
else
    echo "Host does not exist"
fi

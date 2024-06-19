0x03. Log Parsing

This repository contains a Python script (0-stats.py) designed to parse and analyze log data streamed via standard input (stdin). The script computes various metrics based on the input log entries, including total file size and counts of HTTP status codes.
Project Overview

The script reads log entries in the following format from stdin:

php

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

It processes each line to extract the <status code> and <file size>, skipping lines that do not match the specified format. After every 10 lines or upon receiving a keyboard interrupt (CTRL + C), the script prints:

    Total file size accumulated from all processed log lines.
    Counts of each HTTP status code encountered (200, 301, 400, 401, 403, 404, 405, 500) in ascending order.

Requirements

    Python 3.4.3 or higher.
    PEP 8 coding style.
    Scripts must be executable (chmod +x).
    Utilizes standard Linux tools (sys.stdin) for input handling and data processing.
    Handles keyboard interrupts gracefully using signal handling in Python.

Usage

To run the script with log data piped from a generator (like 0-generator.py provided):

bash

./0-generator.py | ./0-stats.py

Example Output

Upon execution, the script outputs metrics after processing every 10 lines or when interrupted:

arduino

File size: <total size>
<status code>: <number>


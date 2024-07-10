Star Wars Characters Script
This script interacts with the Star Wars API to retrieve and display information about characters from a specified Star Wars movie based on the provided Movie ID. It demonstrates foundational skills in web programming, API interaction, and asynchronous programming using JavaScript in Node.js.

Overview
The "Star Wars Characters" script is designed to fetch and print a list of characters from a Star Wars movie by making HTTP requests to the Star Wars API (swapi.dev). It uses Node.js as the runtime environment and the request module for handling HTTP requests.

Key Concepts
HTTP Requests in JavaScript: Utilizes the request module to send HTTP requests to external APIs, specifically the Star Wars API, to fetch data asynchronously.
Working with APIs: Demonstrates the ability to interact with RESTful APIs, parse JSON data returned by API endpoints, and manipulate retrieved data.
Asynchronous Programming: Implements asynchronous operations using callbacks, promises, and async/await syntax to handle API responses and ensure non-blocking execution.
Command Line Arguments in Node.js: Uses process.argv to access and parse command-line arguments passed to the Node.js script, allowing dynamic input such as the Movie ID.
Array Manipulation and Iteration: Iterates over arrays retrieved from API responses to format and display character names in the required order.

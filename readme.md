# Solution to Coding Challenge
## Building and running

This Flask API is contained inside a specific Docker container.
To run this container simply execute the following command in a shell of your chosing:
```bash
docker-compose up
```

Options:
* -d : run in detached mode
* --build: force the container to rebuild itself

You can now access the API on http://localhost:5000/

*Websocket* a test page for the websocket is at http://localhost:5000/socket, this will output the data from the powerplant-post event (called when POST received on /), you can test this by executing a POST request (with Postman or a similar tool).

### docker-compose.yml

To edit port relations, networks or environment variables, feel free to edit the docker-compose.yml file.


## Tools used

- Docker for Windows
- VSCode
- Postman
- Pylinter
- PIP8 formatter
- Flask
- Flask-SocketIO

## Project References

### CO2 Allowances

References used:

- https://www.en-former.com/en/metric-ton-co2-cost/
- https://www.worldbank.org/en/results/2017/12/01/carbon-pricing

### Unit Commitment Solution

To solve the unit commitment problem, I implemented a greedy algorithm based on the cost per MWh of power generated. I ranked the power plants according to their cost per mwh (ascending). The algorithm takes the Pmin and Pmax of the current
and next power plant into account as to achieve the required load. 


The wind turbine power outputs are dependent on the wind factor (%), this
factor has been taken into account as to determine the maximum power output of a wind turbine. 


For the gasfired plants, I incorporated an additional cost of the CO2 emitted (assuming a cost of 25 euros per ton emitted), where the CO2 emission of a plant is 0.3 tons per MWh (as specified in the project description).

*Important note*: the maintenance factor has not been taken into account!

References used:

- Introduction to Computational Thinking, John V. Guttag
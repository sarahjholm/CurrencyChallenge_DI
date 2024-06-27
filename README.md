### Requirements ###

1) Install Docker
2) (For Linux only) Install Docker compose
3) (For Windows only) Install WSL2

### Starting the Services ###

Navigate to the project folder (CurrencyChallenge_DI) through the command line.

Run the following command:
`# docker compose up`

This command should download and start all the services and networks.

### Using the API ###

Once Docker is up and running, the following endpoints are made available:

1) `http://127.0.0.1:8000/currencyapi/` : To search the latest currency rate of USD against EUR
2) `http://127.0.0.1:8000/currencyapi/<str:start_date>` : To search for the currency rate of a specific date
3) `http://127.0.0.1:8000/currencyapi/<str:start_date>&<str:end_date>` : To search for the currency rate within that range of dates

Dates must be written in the following format: YYYY-MM-DD

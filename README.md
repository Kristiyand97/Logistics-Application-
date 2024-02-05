# Logistics Console Application

## Project Description

This Logistics console application is designed for a large Australian company venturing into the freight industry. 
It serves as a management tool for employees to handle package deliveries between major Australian cities efficiently. 
The application facilitates recording package details, route creation and searching, and inspecting the state of deliveries and transport vehicles.

## Functional Requirements

### Features

The application supports the following features:

- **Package Management**
  - Create a delivery package with a unique ID, start and end locations, weight (in kg), and customer contact information.

- **Route Management**
  - Create delivery routes with unique IDs and a list of locations.
    - Start location includes a departure time.
    - Subsequent locations include expected arrival times.
  - Search for a route based on a package's start and end location.
  - Update a delivery route by assigning a free truck.
  - Assign a delivery package to a route.

- **Information Display**
  - View information about routes, packages, and trucks.

- **Data Persistence**
  - Save the application state to the file system.

## Getting Started

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the application using the command line or through an IDE like PyCharm.

## Usage

- To start the application, execute the `main` method in the `LogisticsApp` class.
- Follow the on-screen prompts to interact with the application.

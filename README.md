# Logistics Application

## Project Description
This Logistics console application is tailored for a large Australian company looking to broaden its services in the freight industry. It is designed to assist company employees in managing the delivery of packages across major Australian cities.

## Functional Requirements
The application supports a variety of functions crucial to logistics management:

### Creating a Delivery Package
Add details of a delivery package, including a unique ID, start and end locations, weight, and customer contact information.

### Creating a Delivery Route
- Routes have a unique ID and a list of locations.
- The first location indicates the starting point with a departure time.
- Subsequent locations include expected arrival times.

### Searching for a Route
Locate a delivery route based on the package's origin and destination.

### Updating a Delivery Route
Assign an available truck to a route.

### Assigning a Package to a Route
Link a delivery package to a route.

### Viewing Information
Access current information on delivery packages, trucks, and routes.
## Examples

### Creating Routes
- `createroute SYD 25/05/24 02:35 MEL 25/05/24 04:35`
- `createroute MEL 25/05/24 05:00 SYD 25/05/24 07:00`
- `createroute ADL 27/07/24 03:35 PER 26/06/24 06:35`

### Creating Packages
- `createpackage SYD MEL 89.0 98435345`
- `createpackage MEL SYD 34.9 345635635`
- `createpackage ADL PER 34.2 36546546`

### Viewing Packages
- `viewpackage 1`
- `viewpackage 2`
- `viewpackage 3`

### Viewing Unassigned Packages
- `viewunassignedpackages`

### Assigning Routes to Packages
- `assignroute 1 1001`
- `assignroute 2 1002`
- `assignroute 3 1003`

### Searching for Routes
- `searchroute 1`
- `searchroute 2`
- `searchroute 3`

### Viewing Truck Information
- `viewtruck 1001`
- `viewtruck 1002`
- `viewtruck 1003`

### Assigning Packages to Trucks
- `assignpackage 1`
- `assignpackage 2`
- `assignpackage 3`

## Getting Started
To begin using the application:

1. Clone the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the application and use the provided commands to interact with it.

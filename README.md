Logistics Application
Project Description
This Logistics console application is designed for a large Australian company expanding into the freight industry. The application facilitates the management of package deliveries between major Australian cities, streamlining the process for company employees.

Functional Requirements
The application supports various operations essential for efficient logistics management:

Creating a Delivery Package: Record the details of a delivery package, including a unique ID, start and end locations, weight in kilograms, and customer contact information.

Creating a Delivery Route:

Each route has a unique ID and a list of locations (minimum of two).
The first location is the starting point with a departure time.
Subsequent locations have expected arrival times.
Searching for a Route: Find a delivery route based on the package's start and end locations.

Updating a Delivery Route: Assign a free truck to a delivery route.

Assigning a Package to a Route: Link a delivery package to a specific route.

Viewing Information: Inspect current states of delivery packages, transport vehicles, and delivery routes.

Terminal Commands
To interact with the application, use the following commands in the terminal:

createroute <StartLocation> <DepartureTime> <EndLocation> <ArrivalTime>
createpackage <StartLocation> <EndLocation> <Weight> <CustomerContact>
viewpackage <PackageID>
viewunassignedpackages
assignroute <PackageID> <RouteID>
searchroute <RouteID>
viewtruck <TruckID>
assignpackage <PackageID>
Examples
createroute SYD 25/05/24 02:35 MEL 25/05/24 02:35
createpackage SYD MEL 89.0 98435345
viewpackage 1
assignroute 1 1001
searchroute 1
viewtruck 1001
assignpackage 1
...
Getting Started
To get started with the application:

Clone the repository to your local machine.
Navigate to the project directory in your terminal.
Use the provided commands to interact with the application.
Contributing
Contributions to this project are welcome. Please adhere to the project's coding standards and submit pull requests for any new features or bug fixes.

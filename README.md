<h1>Ticketing System</h1>
<h3>Introduction</h3>
    This document provides an overview of the simple web-based ticketing system developed using Django Framework (Python). The system facilitates the creation, listing, viewing/editing, and searching of tickets.
    
<h3>Functionality</h3>
1). Creation of New Ticket :

  * Users can create new tickets with minimum required fields.

2). Listing of Tickets :

  * Open Tickets: Displays all open tickets.

  * Closed Tickets: Lists all closed tickets.

  * Users can click on a ticket to view/edit its details.

3). View/Edit Ticket :

  * Displays full ticket details.

  * Users can edit ticket details and resolve/close the ticket.

4). Search Ticket :

  * Users can search for tickets by Phone,Email,Category and Dates.

<h3>Minimum Required Fields</h3>
The minimum required fields for creating a new ticket include:

  * Demographic: Name, Phone, Email, City, State, etc.

  * Details: Ticket Description

  * Category: Technical/Billing/Service (Choose one)

  * Notes: Multiple notes can be added to the ticket as technicians work on it.

  * Status: Open (during creation)

  * Dates: Creation Date / Last Modified Date
<h3>How to Run</h3>

    Ensure Python and Django are installed on your system.
    
    Clone the repository.
    
    Navigate to the project directory.
    
    Run python manage.py runserver to start the development server.
    
    Access the application through the provided URL.
<h3>Conclusion</h3>
    This ticketing system provides a simple yet effective solution for managing tickets efficiently. It can be further extended and customized based on specific requirements.

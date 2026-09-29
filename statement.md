# Project Statement

 1. Project Title

Canteen Food Ordering System

---

 2. Problem Statement

Traditional canteen ordering require customer to do manual effort to check the available menu, calculate the quantity of desired items and the final bill

Canteen / Food Ordering System provides users a digital interface where they can see the available menu, select the food items, choose quantity, get the bill calculated along with the discount and the net amount to be paid.

---

 3. Project Scope

Canteen / Food Ordering is a simple digital platform for food ordering and billing.

The application includes the following functionalities:

* Displaying food menu

* Selecting food items

* Choosing quantity

* Calculating bill

* Giving discount

* Order validation

* Order summary

The current scope does not involve payment capture, database or real-time inventory management but it is built in a way to serve as an educational project.

---

 4. Target Users

Canteen / Food Ordering System can be used by

* Canteen customers

* Students

* College staff

* Small-scale food joints


 5.Features

# Menu display

It stores the list of food items with prices and displays to the user

# Food selection
The user can select the desired food

# Quantity selection
User chooses quantity for each item

### Bill calculation

The system calculates the amount due for the ordered items.

# Discount

A discount of 10 percent is given on the calculated amount.

# Order validation

The system ensures that the user had selected at least one item before generating the bill.



 6. Functional Requirements

1. Display the food items and their prices.

2. Allow the user to select multiple food items.

3. Allow the user to select quantity of the item desired.

4. The system shall calculate the total amount due.

5. The system shall give 10 percent discount on the total amount due.

6. The system shall calculate and display the final amount to be paid.

7. The system shall not calculate the bill if the user had not selected any item.

8. The system shall display order summary on successful calculation of the bill.



 7. Non Functional Requirements

# Usability

The interface should be simple and intuitive.

## Reliability

The system should accurately calculate the amount due based on the food items selected and the quantity.

# Maintainability

The application is divided into modules so that each functionality could be updated independently.

# Performance

The system should rapidly generate the bill for an average number of ordered items.



 8. Technology Used

* Python

* Streamlit

* Visual Studio Code

---

 9. Project Modules

# `app.py`

It defines the main streamlit user interface and controls the flow of the application.

# `menu.py`

This module stores the list of food items and their prices.

# `billing.py`

It has the functionality to calculate the bill and the discount.

# `utils.py`

This module has the function to validate the order.

---

10. Expected Workflow

```text

Start

↓

Display Menu

↓

Select Food Items

↓

Select Quantities

↓

Validate Order

↓

Calculate Total

↓

Apply 10% Discount

↓

Calculate Final Amount

↓

Display Order Summary

↓

End
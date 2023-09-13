# Food Delivery Application

## Project Overview

In these Project I created Food Delivery Application is a web-based platform that connects users with restaurants to order food items. The application consists of three main components: Admin Panel, User Panel, and Main Panel. The Admin Panel allows administrators to manage the restaurant's menu, while the User Panel enables users to register, place orders, update their profiles, and view order history. The Main Panel serves as the central interface for users to access both admin and user functionalities.

## Admin Panel

### Features
- **Login for Admin**: Secure login system for administrators.
- **Add New Food Items**: Ability to add new food items with details such as name, quantity, price, discount, and stock.
- **Edit Food Items**: Allows administrators to edit food items using their unique FoodID.
- **View Food Item List**: Displays a list of all food items on the menu.
- **Remove Food Items**: Provides the capability to remove a food item from the menu using its FoodID.
- **Storage**: JSON for storing food item data

### Code
The Admin Panel code is organized into a class called `admin_panel` and includes methods for managing food items.

## User Panel

### Features
- **User Registration**: Allows users to register by providing personal information.
- **User Login**: Registered users can log in to their accounts securely.
- **User Dashboard**: Provides options for users to place new orders, view order history, and update their profiles.
- **Place New Order**: Users can select food items from the menu, view details, and place orders.
- **Order History**: Enables users to view a list of their previous orders.
- **Update Profile**: Allows users to edit their personal information.
- **Storage**: JSON for storing user details
- **User Authentication**: Basic email and password authentication

### Code
The User Panel code is organized into a class called `user_panel` and includes methods for user registration, login, ordering, profile management, and more.

## Main Panel

### Features
- Integration of Admin and User Panels: Allows users to choose between admin and user functionalities.
- Easy Navigation: Provides a menu-driven interface for users to select desired actions.
- Clean User Experience: Ensures a smooth user experience with clear instructions and feedback.
- Language: Python

### Code
The Main Panel code integrates both Admin and User Panels, enabling users to select their roles and perform actions accordingly.

### Technology Stack
- Language: Python
- Storage: <br>
          JSON for storing food item data.<br>
          JSON for storing user details.

## Conclusion
The Food Delivery Application streamlines the process of ordering food from restaurants. It offers a user-friendly interface for both administrators and users, making it a valuable tool for restaurant owners and customers alike. The use of Python, JSON storage, and basic user authentication ensures security and scalability for the application.

This project portfolio showcases the key components and functionalities of the Food Delivery Application, making it an attractive and efficient solution for managing food delivery operations.

Restaurant Auto Cashier System
----------------------------------------------------------------
A terminal-based restaurant management system written in Python. Handles both dine-in and takeaway orders, with a password-protected admin panel for managing menus.
----------------------------------------------------------------
Features
----------------------------------------------------------------
Dine-In Ordering — customers select a meal by table number from a structured three-course menu
Takeaway Ordering — customers pick a food item and receive a unique 4-digit ticket number
Admin Panel — password-protected access to manage both menus
Input Validation — handles non-integer inputs and blank fields
Confirmation Prompts — deletion and removal require confirmation to prevent accidents
Safe Key Generation — takeaway item numbers remain unique even after deletions
----------------------------------------------------------------
Dine-In
----------------------------------------------------------------
Enter your table number.
Browse the dine-in menu (starter, main, dessert).
Enter the meal number to order.
Receive an order confirmation sent to the kitchen.
----------------------------------------------------------------
Takeaway
----------------------------------------------------------------
Browse the available takeaway items.
Enter the food number to order.
Receive a 4-digit ticket number and confirmation that your order is being prepared.
----------------------------------------------------------------
Admin Panel
----------------------------------------------------------------
Access is protected by an admin key. The default key is:
restaurant123
----------------------------------------------------------------

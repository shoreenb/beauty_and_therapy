# Testing For Beauty & Therapy

[Main README.md](README.md)

[View The Beauty & Therapy Website](https://beauty-and-therapy.herokuapp.com/)

## Table Of Contents

1. <a name="valid">Validation Services</a>
2. <a name="userStories">Testing User Stories</a>
3. <a name="manual">Manual Testing</a>

- <a name="desktop">Tests For Desktop</a>

- <a name="devices">Tests for Mobile Devices </a>

4. <a name="bugs">Bugs</a>

- <a name="solved">Solved</a>

- <a name="unsolved">Unsolved</a>

## [Validation Services](#valid)

The following validation services were used to check the validity of the website code.

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML

- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS 

  ```
  <p>
      <a href="http://jigsaw.w3.org/css-validator/check/referer">
          <img style="border:0;width:88px;height:31px"
              src="http://jigsaw.w3.org/css-validator/images/vcss"
              alt="Valid CSS!" />
      </a>
  </p>
  <p>
  <a href="http://jigsaw.w3.org/css-validator/check/referer">
      <img style="border:0;width:88px;height:31px"
          src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
          alt="Valid CSS!" />
      </a>
  </p>
  ```

- [JSHint ](https://jshint.com/) was used to validate JavaScript

## [Testing User Stories](#userStories)

**Viewing and Navigation**

| ID   | AS A/AN  | I WANT TO BE ABLE TO...                                      | SO THAT I CAN...                                             |
| ---- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | Customer | Navigate the site easily from any device: desktop, tablet or phone | Have visually appealing content to view that is also useable |
| 2    | Customer | Easily find products/services that are available to purchase | Select some to purchase                                      |
| 3    | Customer | Click on individual products to see the products/services in more detail | See product/service image, description and price             |
| 4    | Customer | Easily identify clearance items/special offers               | Make a saving on products/services i'd like to purchase      |
| 5    | Customer | See a summary of my bag                                      | Keep a track of spending                                     |
| 6    | Customer | Clearly see where to book services once purchased            | Book a treatment/service                                     |

1. The site was arranged so that its elements (navbar, icons, search, products, checkout bag) were in a place the user would be familiar with. Large headings on each page also help the user to know where they are on the site.

   The key categories (in the hamburger menu format for small devices), the user profile and the shopping bag are visible at all times on the navbar for easy access.

2.	The main feature of the landing page is the large call-to-action button, which is directing the visitors to the page that contains all products and services. The visitor can also easily find products/services via the search function on the main nav bar, via the categories list under the main heading or the category list on the nav bar.

3.	Each Category has a small description under the image with name, price, category classification and rating. If the visitor would like to know more details about that product, they can click on each image for a more in-depth description of that product.

4.	There is a separate dropdown section for special offers on the main navbar, which the user can find featured products, deals, special offers and all offers.

5.	The visitor can see a running total of their shopping bag on the navbar at all times, on any page of the site. Whenever they add an item a summary box also shows a quick breakdown of the shopping bag too.

6.	Once an order has been processed, If a service has been ordered, a button appears on the order that directs the visitor straight to the service booking form.

   

**Registration and User Accounts**

| ID   | AS A/AN        | I WANT TO BE ABLE TO...                               | SO THAT I CAN...                                             |
| ---- | -------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| 7    | Account Holder | Easily register for an account                        | Have an account and view my profile details                  |
| 8    | Account Holder | Receive email confirmation of my account registration | Have confirmation of successful registration                 |
| 9    | Account Holder | Login or logout easily                                | Have access to my personal account information               |
| 10   | Account Holder | Recover my password easily in case I forget it        | Gain access to my account                                    |
| 11   | Account Holder | Have a personalised user account                      | View my order history, subscriptions and save my personal information |
| 12   | Account Holder | Edit my account details                               | Update my information where necessary                        |

7. The visitor can register for an account by clicking on the user section in the navbar. They will also be prompted and redirected to register or login if they try to perform actions that require user authentication, such as booking a service.
8. Upon successful registration a success message alerts the user of the email the confirmation has been sent to and a message inform them that they need to verify their email to finalise sign-up.
9. By clicking on the user symbol in the navbar, the visitor can login or out easily. They will also be prompted to login during the order and booking process.
10. There is a forgotten password link so that the user can recover their password if the need to.
11. The profile section contains the user's default information and an order history list with the order number, order date, items purchased and order total.
12. The user profile form in the profile section contains the default information and an update  button should a user need to update their information.



**Sorting and Searching**

| ID   | AS A/AN  | I WANT TO BE ABLE TO...                                      | SO THAT I CAN...                                             |
| ---- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 13   | Customer | Sort the list of available products and services             | Sort products/services by category, best rated  and best price |
| 14   | Customer | Sort a specific category of product/service                  | Sort the products/services I might want to purchase without having to search through the total list of products/services |
| 15   | Customer | Sort products/services that fit into multiple categories     | Find the best-priced or best-rated products/services across broad categories such as "treatments" or "skincare" |
| 16   | Customer | Search for a product by keyword or name                      | Quickly find a specific product or serivce I want to purchase |
| 17   | Customer | See the search results easily and the number of the returned results | Identify whether the product/service that I want is available |

13. The search function allows the user to sort the products/services by category, rating, name and price in ascending or descending order.

14. The user can choose from the category list in the navbar, the categories button that shows the categories of the items currently showing on the page or the category tag under each item.

15. The user can sort products into categories by searching for keywords in the search box and then further sort those products using the 'sort by' filter.

16. If the visitor knows specifically what product or service they want to find, they can type it into the search box in the navbar and find it by name

17. The visitor can easily see a count of the returned results from a search, just above the products on the 'All Products and Services' page. The results will also be just underneath so that the visitor can identify what they require quickly.

    

**Purchasing and Checkout**

| ID   | AS A/AN  | I WANT TO BE ABLE TO...                                      | SO THAT I CAN...                                             |
| ---- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 18   | Customer | Select the quantity of products/services easily when purchasing | Verify that I don't order the wrong product/service or quantity |
| 19   | Customer | View items in my bag ready to be purchased                   | View a list of the products/services I will be purchasing and the total cost |
| 20   | Customer | Alter the quantity of individual items in my bag             | Make changes to my bag easily before checkout                |
| 21   | Customer | Feel reassured that my personal details and payment information is safe and secure | Follow the instructions to easily and confidently make a purchase |
| 22   | Customer | View an order summary before completing the purchase         | Verify that I haven't made any mistakes                      |
| 23   | Customer | View an order confirmation after making a purchase           | Verify that the purchase was successful                      |
| 24   | Customer | Receive an email confirmation after checking out             | Retain confirmtation of what I have purchased for my records |
| 25   | Customer | Be able to complete a booking form once my service has been purchased | Book a treatment/service                                     |
| 26   | Customer | Find information on how to cancel an order                   | Cancel an order                                              |

18. When a user clicks on the products, and goes through to the product/services details page, they will have the option to choose the quantity that they require.
19. Clicking on the shopping bag will show the user a list of the items that are ready to be purchased, along with the details of that item and the total cost.
20. If the user wants to change the quantity of an item that is already in the bag, they have the ability to do so, to help make the checkout process quicker.
21. The user has the option to save their details to their profile and can only perform certain activities once they are logged in for safety and security. The instructions are very straightforward and the validation fields will alert the user if there is anything that needs to be changed.
22. A summary of the items is on the checkout page so that the user can ensure that they are happy to go ahead with the purchase.
23. Once the purchase has been successful, an order confirmation and message will appear to let the customer know that the order has been processed.
24. An email will be sent to the user once the payment has been successful and if the option is checked, that information can be saved to their profile too.
25. If a service has been purchased, a button will appear on the order confirmation that will direct the user to a booking form to schedule that service. Another confirmation will appear once that booking has been confirmed.
26. Information on how to cancel an order is on the order confirmation.

## [Manual Testing](#manual)

This section is a detailed account of all the manual testing that has been done to confirm all the areas of the site work as expected.

### [Tests For Desktop](#desktop)

The following steps were repeated using Chrome, Firefox and Internet Explorer and on various screen sizes:

##### On all pages:

- Clicked on the logo to confirm it goes back to the home page.
- Clicked on the drop down list under the user icon to check it goes to the login and profile page, or logout if not logged in.
- Clicked on the shopping bag icon to check it redirects to the shopping bag.
- Clicked each category heading in the navbar to check that it works and the correct options are in the dropdown menu.
- Checked that the incentive banner is showing on all pages.
- Checked that the hover effect or point appears on each button, icon or image.
- Checked that the search box is operational and can be typed in and the icon clicked.
- Checked the heading is correct for the page and positioned centrally.

##### Individual Pages:

1. Home Page

   - Opened the site in the selected browser to verify that the landing page loads
   - Confirmed that the background image is covering the width of the screen
   - Confirmed that the placement of the logo, title, text and button is all central.
   - Checked that the buttons of the navbar are all in a line and the icons are visible 
   - Clicked each of the buttons to make sure they led to the correct page
   - Checked that the button background colour and text changes when hovering over the 'Shop Products & Services' button.

2. All Products & Services

   - Confirmed the product images are visible
   - Checked that the name, price, category and rating is visible and aligned centrally
   - Checked that the images are the same size
   - Checked that the category dropdown under the heading is functional and the buttons change when hovered over.
   - Checked the product and services count works
   - Checked that the 'sort by' field is functional and sorts the items in ascending and descending order.

3. Product Detail Page

   - Checked that the product/service image is visible 
   - Checked the product name, price, description, category tag and rating are centrally aligned
   - Checked that the quantity incrementor and decrementor works.
   - Checked that the options field appears if that item has optins and that the options are visible.
   - Checked that clicking add to bag triggers the Checkout summary toast.

4. Checkout Summary Toast

   - Checked that the message that the item has been added to the bag appears
   - Checked that the bag count works
   - Checked that the image is in the bag and the appropriate proportion
   - Checked that the total is showing and correct
   - Checked that the delivery incentive prompt appears if the total is less than the threshold
   - Checked that clicking proceed to secure checkout opens the Shopping Bag page

5. Shopping Bag

   - Confirmed that the image loads when entering the page
   - Confirmed that the Heading and subheading are correct, in the correct position and visible
   - Checked that the item name, price, quantity field and subtotal appear
   - Checked that the bag total, delivery total, grand total appear and are showing the correct amount
   - Checked that the continue shopping button leads back to the bag and the secure checkout button leads to the checkout page

6. Checkout

   - Checked that the Checkout summary is in the right column and that the image, item name and option (if selected) is visible.

   - Checked that the subtotal, order total, delivery amount and grand total are visible and calculated correctly

     6.1 - Checkout Form

     - Checked that the Form fields are visible
     - Checked that the required fields are starred
     - Checked that the checkbox to save the information to the profile is visible and functional
     - Checked that the Stripe Payment field is visible
     - Checked that the validation works for the fields if they are left blank or don't meet the validation requirements

     6.2 - Stripe Payment

     - Checked that the stripe validation is working for incorrect numbers
     - Checked that the success card number produces a successful payment in stripe events
     - Checked that the unsuccessful card number produces a failed payment in stripe events
     - Checked that the webhook works if the page isn't redirected to checkout success
     - Checked that the alert under the payment field is showing the user the correct amount that they will be charged.
     - Checked that a successful email is sent for successful payments
     - Checked that the loading overlay and spinner works while the payment is being processed
     - Checked that the success toast message appears with the order number and email confirmation of the order.

     6.3 - Checkout Success

     - Checked that a successful payment redirects the user to the checkout success page with user's email and the order information:
       - Order Number
       - Order Date
       - Item name, quantity and price and option if chosen
       - Delivery Address
       - Order Total
       - Delivery Amount
       - Grand total
       - Cancellation contact email

7. Booking Form

   - If a service is purchased, once the order has been processed, checked that the 'Book Your Services' Button appears under the service item's details

   - Checked that the hover function works and it works when clicked

   - Once the 'Book Your Services' button is clicked checked that it redirects the user to a booking form

   - Checked that the booking details appear and form fields are visible

   - Checked that the date-picker can be opened and a date selected

   - Checked that the time field can be opened and a time selected

   - Checked that when the confirm booking button is clicked another confirmation is produced with the correct information:

     - Order Number

     - Order Date

     - Item name, quantity and price and option if chosen

       Booking Details:

       - Booking Name
       - Email
       - Phone Number
       - Chosen Date
       - Chosen Time
       - Cancellation contact email

   - Checked that the success toast message appears with the order number and email confirmation for the booking

8. User Profile

   - Checked that the default delivery information is filled out in the form in the left column
   - Check that the fields are showing and labelled correctly
   - Checked that the Update information button is functional

   8.1 - Order History

   - Checked the table headings of the order history are in the correct position and visible
   - Checked that the fields are populated with the correct Order Number, Date, Item and Order total
   - Checked that the order number field is truncated but when you hover over it the full order number is visible.
   - Checked that if you click on the order number an alert message informs you that is is a past order and the correct details are on the order
   - Checked that clicking on the back to profile button redirects to the profile.

### [Mobile Devices](#devices)

The following steps were repeated on physical devices available to the developer: Oppo X2 Lite, Motorola G8, Samsung and a tablet, as well as all the simulated devices and responsive options on the Chrome Developer Tools:

##### On all pages:

- Checked the size and placement of the logo across all device screen sizes
- Confirmed that font size is legible on all screen sizes, especially small  and medium screens
- Checked that the navbar responsively collapses behind a button on small and medium screens and the search, user and bag icons are visible and functional
- Checked that the content at least fills the height of the screen with the footer at the bottom
- Checked that buttons and fields are large enough to click but still fit on the screen comfortably

##### Individual Pages:

 	1. Home Page
 	 - Checked that everything is displayed centrally and fits within the height of the screen.
 	 - Checked that the hero image covers the width of the screen, the title is not squashed or overlapping the button especially on screens with a width below 992px 
 	2. All Products
 	 - Checked that the products and services are spaced appropriately and stacked on smaller 	 screens
 	 - Checked that the buttons are aligned and do not overlap the images or text
 	3. Product Detail Page
 	 - Checked that the text, quantity field, options field and buttons are displayed 		 	centrally
 	 - Checked that the image is displayed centrally, stacked above the text
 	4. Checkout Summary Toast
 	 - Checked that the checkout summary box appears and all the text is visible
 	 - Checked that it is positioned centrally and the item image and details are present
 	5. Shopping Bag
 	 - Checked that the title, text and image are central
 	 - Checked that the bag, delivery and grand totals are at the top
 	 - Checked that the buttons are inline and do not overlap the text
 	6. Checkout
 	 - Checked that the title, text, order summary  are visible
 	 - Checked that the form and order confirmation fits centrally within the width of the 	 	screen
 	 - Checked that the buttons are aligned fits within the screen
 	 - Cheecked that the loading overlay and spinner fit within the width of the screen
 	7. Booking Form
 	 - Checked that the 'Book Your Services' button is visible
 	 - Checked that the form fits within the width of the screen
 	 - Checked that the 'Confirm Booking' button is central
 	8. User Profile
 	 - Checked that the title, text and form are central
 	 - Checked that the form and order history table fits within the width of the screen
 	 - Checked that the 'Update' button is central

## [Bugs](#bugs)

### [Unsolved](#unsolved)

1. As this was the first time I have worked with crispy forms, and dispite discussing at length with my mentor and tutors, I was unable to find the correct options to customised the date picker and time field  on my booking form. Given a bit more time, I am sure I will find the compatible datepicker so that the date can start from today, previous dates can be disabled and it can be limited to the required date range.

   

   ![Date](media/readme/features/date.png)

   

   The time field is a fixture that is loaded from the BookingTime model but the display is showing '-------' insted of a placeholder, despite my best efforts to get it working. This will also have to be researched when more time is available.

   

   ![Time](media/readme/features/time.png)








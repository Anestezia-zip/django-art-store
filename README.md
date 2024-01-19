# Artful Urbex
​
Welcome to the Artful Urbex, an exquisite online destination where art meets passion. Our store offers a diverse collection of paintings, each with its own story and beauty. From contemporary artworks to classic masterpieces, our gallery is designed to cater to the varied tastes of art enthusiasts and collectors.
  
![Am i responsive image](https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/responsive.jpg)  
​
[Click Here To Visit Live Site](https://artful-urbex-3e13a9b6e83c.herokuapp.com/)  


## Table Of Contents:
1. [Planning](#planning)
    * [User Stories](#user-stories)
    * [User Experience](#ux)
    * [Agile Methodology](#agile-methodology)

2. [Database Schema](#database-schema)
3. [Customer Acquisition](#customer-acquisition)

4. [Features](#features)
    * [Navigation](#navigation-bar)
    * [Home page](#home-page)
    * [Products page](#products-page)
    * [Products detail page](#products-detail-page)
    * [Bag page](#bag-page)
    * [Checkout page](#checkout-page)
    * [Profile page](#profile-page)
    * [Login and Register page](#login-and-register-page)
    * [Footer](#footer)
    * [Future Features](#future-features)
​
5. [Technologies Used](#technologies-used)
6. [Libraries](#libraries)
7. [Testing](#testing)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
​
# Planning:

## User Stories
### As a first time visitor:
- I want to understand the purpose of the website and easily navigate through
- I want to be able to view through a catalog of paintings, open the details of each one, and read the descriptions so that I would get quick access to relevant information and get a better understanding of the content
- Once I've added a painting to my cart, I can proceed with the purchase. This involves entering my payment details and shipping information. The process is designed to be straightforward, ensuring that I can complete my transaction easily and securely.
- I can use a contact form on the homepage. It's a direct way to communicate with the support team.
- I can sort paintings into different categories. This feature helps me easily find what I'm looking for, whether it's a particular zone, price or period of art.
- I can input any term into a search bar, and if it appears in the name or description of products, they will all be identified.
- I want to be able to register an account to have more access to the website
#### As a registered user:
-  I can rate each painting on a scale from 1 to 5 stars. This feature allows me to express my opinion about the artworks and contribute to their overall rating on the site
- I can view my order history, which is a record of all my past purchases. This feature helps me keep track of what I've bought, when I bought it, and the details of each transaction.
-  I gain access to a wishlist feature. I can add my favorite paintings to this list, making it easier to find and revisit them later or to make a purchase in the future.
- I can update or delete my painting requests or queries I submit through the contact form so that have more control over my requests in case of errors.
- I want to be able to update my profile information so that I could change contact information, password, and any other personal data associated with my account
#### Site owner
- As a site owner, I want to be able to create, update and delete paintings, ratings and users so that I can control my website content

[Back to the table](#table-of-contents)

## UX

### Intended Customers
- Art collectors searching for premium artworks for their collections.
- Connoisseurs and aficionados eager to discover the latest masterpieces from celebrated artists.
- Art lovers and those intrigued by the evolving landscape of art and design.

### Site Purposes
- Streamlining the process of locating specific art pieces.
- Enabling a swift and efficient checkout experience for art acquisitions.
- Allowing art enthusiasts to register and manage their favorite pieces and review past acquisitions.
- Simplifying the update of personal delivery details for smooth art deliveries.
- Providing a direct channel for interaction and queries with the art business.

### Project Objectives

- Construct a dynamic online platform for art commerce.
- Embed a variety of sophisticated features to simulate an upscale virtual art gallery.
- Utilize insights from previous digital projects to enhance this platform's functionality.
- Add innovative elements like a personal collection gallery and client feedback options to expand the site's interactive capabilities.
- Prioritize navigational ease and aesthetic appeal for an enriching online art shopping journey.  

[Back to the table](#table-of-contents)

  
## Agile Methodology
To effectively allocate development resources, I categorized functionalities into three tiers: Must-Have, Should-Have, and Could-Have. This stratification was crucial in assessing the significance of each component.

I used Github and Project Board using Kanban board:

[Click here to see the Project Board](https://github.com/users/Anestezia-zip/projects/6)  

[Back to the table](#table-of-contents)

# Database Schema
After the wire-frames completion, a database schema was created to understand what models need to be devoloped and what information and data should be stored on the back-end database.
![Database diagram](https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/diagram.png)

## Customer Acquisition

![Facebook](https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/fb.png)

[Back to the table](#table-of-contents)

## Features:

### Navigation Bar
- The navigation bar is located at the very top of each page, and it is a "sticky" navigation bar, i.e. if the page is longer and the user has to scroll down, the navigation bar stays at the top of the page the whole time! The logo is on the left, the navigation links are on the right.
- The logo is clickable and redirects the user to the home page.
- To the right of the logo is the search bar, inviting users to "Search our paintings," complemented by a search button with a magnifying glass icon for initiating the search.
- Across the navigation bar, we see well-defined categories: "ALL," "URBAN EXPLORATION," and "NATURE," which organize the site's content into easy-to-navigate sections.
- The user's account section is positioned on the top right, displaying an icon for "My Account" and a shopping cart. It also shows a balance, which in this case is "0.00 €," indicating the user's current available funds or points.
- The responsive design of the navigation bar adapts to different screen sizes. On tablets and mobile devices, content is spaced evenly apart and navigation links are collapsed into a hamburger menu that, when clicked, unfolds to show navigation links, providing a mobile-friendly experience.  

<details><summary>Navbar</summary>
  <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/readme-navbar.png">
</details>


### Home Page
Landing page invites you on a visual and interactive journey through our curated gallery of paintings. You'll discover a detailed guide on selecting the right canvas size, an easy-to-use contact form for personalized inquiries, and an insight into the values and artistic vision that shape our gallery. The home page has a adaptive section with a parallax effect button that lead to all products.

- <b>Hero section</b> sets the tone with a compelling proposition to bring the visitor's envisioned artwork to life.
- <b>Choose Your Perfect Canvas</b> is designed to help customers select the ideal canvas size for their space. With options ranging from compact to expansive, and the ability to visualize each size in a simulated room setting.
- <b>Painting Request Form</b> - inviting visitors to discuss their ideas for future paintings sits prominently. It offers options to describe the envisioned painting, select a size, and even opt for an artist's signature. The facility to upload examples provides a seamless way for customers to convey their vision.
- <b>Artistic Philosophy and Showcase</b>. Canvases are described as more than mere art pieces; they're stories, emotions, and memories brought to life. The artwork is presented not just as decoration but as an integral part of the home and life. The section is accentuated with examples of artwork that embody diversity, expression, and eccentricity.

<details><summary>Home page</summary>
  <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/landing-page.png">
</details>


### Products page
Product page presents a curated selection of paintings that visitors can browse through. The top of the page features a clear categorization that allows users to filter the artwork based on themes such as "Urban Exploration" and "Nature".

Each painting is accompanied by a title that hints at the scene or sentiment the painting embodies, such as "Silent separation" or "Bridging two worlds", giving a sense of story and emotion behind the work. Pricing is transparent, allowing customers to make informed decisions based on their budget.


  <details><summary>Products page</summary>
  <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/products.png">
  </details>

### Products detail page
The picture details page additionally has a description and the ability to rate the picture from 1 to 5 stars. And also the "Add to bag" button to add the painting to your cart

  <details><summary>Products detail page</summary>
  <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/detail.jpg">
  </details>

### Bag page
One of the main features of an e-commerce platform, the shopping bag shows a list of items that the user has added for purchase. In the shopping cart, the user can see information about what exactly he/she has added, as well as remove a picture from the cart.
  <details><summary>Bag page</summary>
  <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/bag.jpg">
  </details>

### Checkout page
Displays a form for the customer to complete their order, with fields for entering personal details such as full name, email, and delivery address (including phone number, country, postal code, city, and street address). There's also a section for payment information, where card details are to be entered.

On the right side of the page, there's an order summary for a single item. The bottom of the form includes buttons to adjust the bag or complete the order, with a notice that the card will be charged upon order completion. There's also an option to save the delivery information to the customer's profile.
  <details><summary>Checkout page</summary>
  <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/checkout.jpg">
  </details>

### Profile page
The profile page consists the user's current informationand two buttons with which you can change your password or email. Below is the order history and a form with the address

<details><summary>Profile page</summary>
  <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/profile.jpg">
</details>  

### Wishlist page
Paintings have a filled heart icon on some items, which signifies a feature to add or indicate interest or liking, suggesting that these are items in the user's wishlist. 
The wishlist page would allow users to keep track of their favorite items and the trash icon will allow you to remove an item from the wishlist.
<details><summary>Wishlist page</summary>
  <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/wishlist.jpg">
</details>  

### Login and Register page
- The login page is a basic django allauth form, containing 2 input fields for username and password with a "Login" button below it.
- The registration page is also a standard django form with all the required fields for user input.
- The user must enter all information (username, first name, last name, e-mail and password).

<details><summary>Login and Register page</summary>
    <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/login-register.jpg">
</details>

### Footer
- The footer has an invitation for visitors to stay in touch with the latest collections, encouraging them to follow the store on Instagram or subscribe to a newsletter. It's at the bottom of each page and it is a gradient icon with orange-blue color, responsive for tablets and mobile devices.
- Also footer has a Newsletter Subscribtions - there is a form for users to input their email and subscribe to Radical Rides news and email marketing content. All inputed emails are stored in the business' MailChimp account


<details><summary>Newsletter Subscribtions</summary>
    <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/subscription.jpg">
</details>


[Back to the table](#table-of-contents)

## Future Features
1. **Sold Indicator on Products**: my product model includes a 'sold' field which will be utilized to display a sold indicator on the product pages and detail pages once an item is successfully purchased. This feature ensures that all visitors are aware of items that are no longer available. Additionally, for any sold artwork, the "add to bag" option will be disabled, preventing further purchase attempts.

2. **Custom Artwork Request Form**: On the main page, there is a form for users to request custom artwork creations.  These requests are now stored in the user's profile for easy tracking. For logged-in users, requests are directly linked to their account. For those who are not logged in, requests are stored temporarily. 
Moving forward, you plan to eliminate the temporary model and instead bind the requests to an email provided by the user. This streamlines the process, ensuring all requests are saved and attributed correctly, regardless of user login status.

# Technologies Used
- [HTML](https://en.wikipedia.org/wiki/HTML) was used for the mark up.
- [CSS](https://en.wikipedia.org/wiki/CSS)  was used to style the site.
- [Django](https://www.djangoproject.com/) was the framework that was used.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), django is a python framework.
- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)) was also used to style the site.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for interactiveness.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) is used to host this site.
- [Github](https://en.wikipedia.org/wiki/GitHub) was used to store the code.
- [Git](https://en.wikipedia.org/wiki/Git) was used for version control.
- [AWS S3](https://aws.amazon.com/s3/?nc1=h_ls) was used to store the images.
- [ElephantSQL](https://www.elephantsql.com/) was used to store the database.

[Back to the table](#table-of-contents)

# Libraries
- coverage - Is a third-party package that helps developers measure code coverage in their Python codebase.
- dj-database-url - A Django utility to utilise the DATABASE_URL environment variable to configure the Django application. Used with PostgreSQL.
- Django - A python package for the Django framework.
- django-allauth - An integrated set of Django applications addressing user authentication, registration and account management.
- django-summernote - Is a third-party package that provides a rich text editor widget for Django web applications.
- psycopg2 - A PostgreSQL database adapter for Python.
- pytz - A Python package for world timezone definitions, modern and historical.
- Pillow - A Python Imaging Library adds image processing capabilities
- sqlparse - A non-validating SQL parser for Python.

[Back to the table](#table-of-contents)

# Testing
The testing section can be found [here](TESTING.md).

## Bugs

**Problem:**   
Products weren't displaying on the wishlist page despite having filled red hearts.


**Solution:**   
The issue here was attempting to check if `product.id` belongs to `wishlist_item_ids` directly in the template, but my template didn't have direct access to each individual `product.id`.

I needed to iterate through the products to check if their ID exists in the wishlist. Here's how you can achieve this:
```html
{% for product in products %}
    {% if product.id in wishlist_item_ids %}
        <p>{{ product.name }}</p>
    {% endif %}
{% endfor %}  
```
---
**Problem:**   
When sending a POST request to the URL `/toggle-wishlist/1/` a 404 error occurred

**Solution:**  
Added the `"/products/"` prefix to the path in the script file. This adjustment was made to ensure that the path to `toggle_wishlist` aligns with the expected URL structure in the project, where all links start with `"/products/"`.

```
fetch(`/products/toggle-wishlist/${productId}/`)
```
---
**Problem:**  
Forbidden (CSRF token missing.)

**Solution:**  
Added passing a CSRF token in a JavaScript request to ensure proper authentication when sending a request.
```
const csrfToken = "{{ csrf_token }}";
```
---
**Problem:**  
Error "Forbidden (CSRF token from the 'X-Csrftoken' HTTP header has incorrect length.)"

**Solution:**  
Added passing a CSRF token in a JavaScript request to ensure proper authentication when sending a request. The function splits the cookie string into individual elements, then searches for a cookie with the given name and retrieves its value.

```javascript
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Looking for cookies by name
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrfToken = getCookie('csrftoken');

```

# Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Create a database On ElephantSQL
- Log into the [ElephantSQL](https://www.elephantsql.com/) website and click **Create new Instance**
- Enter a **Name** and keep the plan as **Tiny Turtle Free**, then **tags** field can be left blank, Select a region closest to you, I selected **EU-West-1(Ireland)** as I'm in Ireland. Then click **Review** and afterward click **create an instance**.
- On The Dashboard click on your database instance name.
- You will see the details for your database instance, in the URL section click on the copy icon to copy the database URL.
- Head over to gitpod and create a **Database URL** environment variable in your env.py file and set it equal to the copied URL.

#### Deploying to Heroku.
- Head back over to [heroku](https://www.heroku.com/) and click on your **app** and then go to the **Settings tab**
- On the **settings page** scroll down to the **config vars** section and enter the **DATABASE_URL** which you will set equal to the elephantSQL URL, create **Secret key** this can be anything,
**CLOUDINARY_URL** this will be set to your cloudinary url and finally **Port** which will be set to 8000.
- Then scroll to the top and go to the **deploy tab** and go down to the **Deployment method** section and select **Github** and then sign into your account.
- Below that in the **search for a repository to connect to** search box enter the name of your repository that you created on **GitHub** and click **connect**
- Once it has been connected scroll down to the **Manual Deploy** and click **Deploy branch** when it has deployed you will see a **view app** button below and this will bring you to your newly deployed app.
- Please note that when deploying manually you will have to deploy after each change you make to your repository.
- - -

[Back to the table](#table-of-contents)

## Credits
- [CodeInstitute](https://learn.codeinstitute.net/) for their walkthrough project, which guided me with website build especially for publishing posts, comments and likes section which I code along with the video with few adjustments.
- [Allauth](https://django-allauth.readthedocs.io/en/latest/) for their documentation which was helpfull in creating user authentication.

[Back to the top](#volunteer-force)
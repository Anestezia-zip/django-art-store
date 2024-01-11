# Artful Urbex
​
Welcome to the Artful Urbex, an exquisite online destination where art meets passion. Our store offers a diverse collection of paintings, each with its own story and beauty. From contemporary artworks to classic masterpieces, our gallery is designed to cater to the varied tastes of art enthusiasts and collectors.
  
![Am i responsive image](https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/responsive.jpg)  
​
[Click Here To Visit Live Site](https://artful-urbex-3e13a9b6e83c.herokuapp.com/)  


## Table Of Contents:
1. [Planning](#planning)
    * [User Stories](#user-stories)
    * [Agile Methodology](#agile-methodology)

2. [Features](#features)
    * [Navigation](#navigation-bar)
    * [Footer](#footer)
    * [Home page](#home-page)
    * [Single post page](#single-post-page)
    * [Profile page](#profile-page)
    * [Login page](#profile-page)
    * [Sign up page](#signup-page)
​
3. [Technologies Used](#technologies-used)
4. [Libraries](#libraries)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
​
## Planning:

### User Stories
#### As a first time visitor:
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
  
### Agile Methodology
I used Github and Project Board using Kanban board:

![Project Board](https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/board.png)  

[Back to the table](#table-of-contents)

## Database Schema
After the wire-frames completion, a database schema was created to understand what models need to be devoloped and what information and data should be stored on the back-end database.
![Database diagram](https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/diagram.png)

## Customer Acquisition

![Facebook](https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/fb.png)

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
​

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
  <details><summary>Checkout page</summary>
  <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/checkout.jpg">
  </details>

### Profile page
- The profile page consists the user's current informationand two buttons with which you can change your password or email. Below is the order history and a form with the address


    <details><summary>Profile page</summary>
    <img src="https://artful-urbex.s3.eu-west-1.amazonaws.com/readme-artful-urbex/profile.jpg">
    </details>  

### Login and Register page
- The login page is a basic django allauth form, containing 2 input fields for username and password with a "Login" button below it.
- The registration page is also a standard django form with all the required fields for user input.
- The user must enter all information (username, first name, last name, e-mail and password).

    <details><summary>Login and Register page</summary>
    <img src="">
    </details>

### Footer
- The footer has an invitation for visitors to stay in touch with the latest collections, encouraging them to follow the store on Instagram or subscribe to a newsletter. It's at the bottom of each page and it is a gradient icon with orange-blue color, responsive for tablets and mobile devices.


[Back to the table](#table-of-contents)

## Technologies Used
- [HTML](https://en.wikipedia.org/wiki/HTML) was used for the mark up.
- [CSS](https://en.wikipedia.org/wiki/CSS)  was used to style the site.
- [Django](https://www.djangoproject.com/) was the framework that was used.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), django is a python framework.
- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)) was also used to style the site.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for interactiveness.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) is used to host this site.
- [Github](https://en.wikipedia.org/wiki/GitHub) was used to store the code.
- [Git](https://en.wikipedia.org/wiki/Git) was used for version control.
- [Cloudinary](https://cloudinary.com/) was used to store the images.
- [ElephantSQL](https://www.elephantsql.com/) was used to store the database.

[Back to the table](#table-of-contents)

## Libraries
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

## Testing
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

# Artful Urbex
​
Welcome to the 
  
![Am i responsive image]()  
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
Agile methodology was used in the planning of this project. I found it difficult to work on agile and coding in parallel as I was on team 1 and was aware of the changes, so I found it confusing. Afterwards, however, I developed the habit of adding tasks before directly doing them. 
I used Github and Project Board using Kanban board:

![Project Board](https://res.cloudinary.com/dyadwedsy/image/upload/v1700406352/volunteer/readme/board_w2emid.jpg)  

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

### Footer
- The footer is at the bottom of each page and it is a gradient icon with orange-blue color, responsive for tablets and mobile devices.

### Home Page
- The home page has a section with a parallax effect button that lead to all products. The section is adaptive: it changes the font to a smaller one.

  <details><summary>Home page</summary>
  <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700408097/volunteer/readme/hero_mldiqt.jpg">
  </details>
​

    Posts section

- There are adapted cards with user posts, which are arranged in 3 columns on large screens, in 2 columns on medium screens and full width on mobile devices.
- On this page the user have option to use "search bar" to find specific posts or he can scroll down to search for post that he would like to get more information about it
- If input on search box is not empty the user will be redirected to the new page which will eaither displayed match post or display message to the user 
- Posts are displayed in 2 columns with 3 posts per row, each post contains of: image, author, date, indicator of likes and comments and title and brief description 
- Posts card are scaling up as the user hovers over them and clickable title and ecerpt are transforming to capitalize letter
- When clicked on title/excerpt user is redirected to another page which will give a user more information about the post.  

  <details><summary>Posts section</summary>
  <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700408396/volunteer/readme/posts_cxpjto.jpg">
  </details>
​

    Map section

- Interactive map of Ukraine, where pointing at the red houses - with the help of hover effect the user sees a modal window with a description of each destruction, and clicking on the modal - will be able to see full-size photos

  <details><summary>Map of Ukraine</summary>
  <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700411956/volunteer/readme/map_dq8awy.jpg">
  </details>

### Single post page
- A user can go to this page by clicking on a photo or title and get a description of a particular post and all the necessary information about it. And also see the date when the post was created.  

  <details><summary>Post detail page</summary>
  <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700408565/volunteer/readme/posts_vs5zn9.jpg">
  </details>

### Profile page
- The profile page consists of 2 sections:
    - The first section at the top of the screen displays the user's current information, their avatar and the role they chose when registering. If we click the "Edit profile" button, we see a standard django form that allows the user to change their information about themselves, as well as add a "bio" and profile picture if they want to.


        <details><summary>Profile page - User Info</summary>
        <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700408994/volunteer/readme/posts_flncaq.jpg">
        </details>  

    - The bottom section displays the posts that belong to the registered user, as well as the "Add new post" button to add a new post.

         <details><summary>Profile page - User Posts</summary>
        <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700409043/volunteer/readme/profile_xt1i9j.jpg">
        </details>  

### Login page
- The login page is a basic django allauth form, containing 2 input fields for username and password with a "Login" button below it. There is also an option below to log in using google provider.
- The user also has a link above the form to register on the site if they don't have an account, which redirects the user to the "Register" page.

    <details><summary>Login page</summary>
    <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700409951/volunteer/readme/profile_vbvusy.jpg">
    </details>

### Signup page
- The registration page is also a standard django form with all the required fields for user input.
- The user must enter all information (username, first name, last name, e-mail and password). 
- After entering all fields and clicking the registration button, the user will be automatically logged in and redirected to the main page of the site.
- It is also possible to register with the help of Google provider

    <details><summary>Sign up page</summary>
    <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700409973/volunteer/readme/signup_vmssf6.jpg">
    </details>

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
- asgiref - A standard Python library to allow for asynchronous web apps and servers to communicate with each other.
- cachetools - Library providing caching tools and decorators for Python functions.
- cloudinary - A Python package allowing integration between the application and Cloudinary.
- coverage - Is a third-party package that helps developers measure code coverage in their Python codebase.
- debugpy - A debugger for Python that can be used to debug code during execution.
- dj-database-url - A Django utility to utilise the DATABASE_URL environment variable to configure the Django application. Used with PostgreSQL.
- dj3-cloudinary-storage - A Django package that facilitates integration with Cloudinary storage.
- Django - A python package for the Django framework.
- django-allauth - An integrated set of Django applications addressing user authentication, registration and account management.
- django-autoslug - Django library for automatically generating slugs for URL-friendly titles.
- django-ckeditor - Is a third-party package that provides a rich text editor widget for Django web applications.
- django-debug-toolbar - helps you understand how your application functions and to identify problems. It does so by providing panels that provide debug information about the current request and response.
- django-js-asset - Django integration for managing JavaScript assets.
- gunicorn - A Python WSGI HTTP Server for UNIX.
- oauthlib - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.
- psycopg2 - A PostgreSQL database adapter for Python.
- pytz - A Python package for world timezone definitions, modern and historical.
- Pillow - A Python Imaging Library adds image processing capabilities
- sqlparse - A non-validating SQL parser for Python.
- Unidecode - Transliterates Unicode characters to ASCII, useful for handling non-ASCII characters in text.

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

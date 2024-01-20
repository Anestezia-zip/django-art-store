# Artful Urbex - Testing

[Return to the README](README.md)

## Table of Contents
- [Performance](#performance)
  - [Google's Lighthouse Performance](#googles-lighthouse-performance)
- [Browser Compatibility](#browser-compatibility)
- [Responsiveness](#responsiveness)
  - [Smaller screens](#smaller-screens)
  - [Medium screens](#medium-screens)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [PEP8 Validation](#pep8-python)
  - [Javascript Validation](#javascript-validation)
- [Testing](#testing)
  - [Manual Testing](#manual-testing-bdd)
  - [Automated Testing](#automated-testing)
  - [Features Testing](#features-testing)

## Performance

### Google's Lighthouse Performance

Google Lighthouse was used to test the performance of the website.

#### Desktop Results:
<details><summary>Desktop</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1701254259/volunteer/readme/fuoyxpeaewiqtjfjr5w8.png">
</details>

#### Mobile Results:
<details><summary>Mobile</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1701254263/volunteer/readme/oss8x4sb7180cakd2ejq.png">
</details>

## Browser Compatibility
|  Browser | Links  | Pages  | Responsivnes  | Form fields  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Microsoft Edge  | Works as expected| Loading pages no issue  |  Responsivness works as expected |  Works as expected |
|  Chrome | Works as expected  |  Loading pages no issue | Responsivness works as expected  | Works as expected  |
| Opera  |  Works as expected | Loading pages no issue  | Responsivness works as expected  |  Works as expected |

[Back to the table](#table-of-contents)

## Responsiveness
|   | Galaxy Fold  | Iphone SE   | iPhone12 Pro  | iPad mini  | desktop 1024px  |  desktop > 1200px | notes  |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
|  site is responsive >= 700px |  n/a | n/a  |  n/a | Good  | Good  | Good  |   |
| site is responsive < 700px  |  Good | Good  | Good  |  n/a | n/a  |  n/a |   |
| Links/URLs work  | Yes  | Yes   | Yes   |  Yes  | Yes   | Yes   |   |
|  Images work |  Yes  |  Yes  |  Yes  | Yes   | Yes   | Yes   |   |
| Forms work  |  Yes  |  Yes  | Yes   | Yes   | Yes   | Yes   |   |  

# Code validation
## HTML

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartful-urbex-3e13a9b6e83c.herokuapp.com%2F) | ![screenshot](documentation/home.jpg) | No Errors |
| All Products | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartful-urbex-3e13a9b6e83c.herokuapp.com%2Fproducts%2F) | ![screenshot](documentation/all-products.jpg) | No Errors |
| Product Detail | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartful-urbex-3e13a9b6e83c.herokuapp.com%2Fproducts%2F3) | ![screenshot](documentation/product-detail.jpg) | No Errors |
| Search | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartful-urbex-3e13a9b6e83c.herokuapp.com%2Fproducts%2F%3Fq%3Dsunset) | ![screenshot](documentation/search.jpg) | Pass: No Errors |
| Bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartful-urbex-3e13a9b6e83c.herokuapp.com%2Fbag%2F) | ![screenshot](documentation/bag-w3c.jpg) | No Errors |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartful-urbex-3e13a9b6e83c.herokuapp.com%2Fcheckout%2F) | ![screenshot](documentation/checkout-w3c.jpg) | No Errors|
| Checkout Success | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartful-urbex-3e13a9b6e83c.herokuapp.com%2Fcheckout%2Fcheckout_success%2F958179) | ![screenshot](documentation/checkout-success.jpg) | No Errors |
| Profile | n/a | ![screenshot](documentation/profile-w3c.jpg)| No Errors |
| Edit painting request | n/a | ![screenshot](documentation/edit-painting.jpg) | No Errors |
| Wishlist | n/a | ![screenshot](documentation/wishlist-w3c.jpg) | No Errors |



[Back to the table](#table-of-contents)

## CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| base.css | n/a  | ![screenshot](documentation/css.jpg) | No Errors |
| checkout.css | n/a | ![screenshot](documentation/css.jpg) | No Errors |
| profile.css | n/a | ![screenshot](documentation/css.jpg) | No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| index.html (postloadjs) | ![screenshot](documentation/js-home.jpg)| No Errors |
| products/script.js | ![screenshot](documentation/js-products.jpg) | No Errors |
| products-detail.html (postloadjs) | ![screenshot](documentation/js-pr-detail.jpg) | No Errors |
| bag.html (postloadjs) | ![screenshot](documentation/js-bag.jpg) | No Errors |
| stripe_elements.js | ![screenshot](documentation/js-stripe.jpg) | Undefined Stripe variable |


## Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Bag contexts.py | n/a | ![screenshot](documentation/bag-linter.jpg) | No Errors |
| Bag urls.py | n/a | ![screenshot](documentation/bag-urls-linter.jpg) | No Errors |
| Bag views.py | n/a | ![screenshot](documentation/bag-view-linter.jpg) | No Errors |
| Checkout admin.py | n/a  | ![screenshot](documentation//checkout-admin.jpg) | No Errors |
| Checkout forms.py | n/a | ![screenshot](documentation/checkout-forms.jpg) | No Errors |
| Checkout models.py | n/a  | ![screenshot](documentation/checkout-models.jpg) | No Errors |
| Checkout signals.py | n/a | ![screenshot](documentation/checkout-signals.jpg) | No Errors |
| Checkout urls.py | n/a | ![screenshot](documentation/checkout-urls.jpg) | No Errors |
| Checkout views.py | n/a  | ![screenshot](documentation/checkout-views.jpg) | No Errors |
| Checkout webhook_handler.py | n/a | ![screenshot](documentation/webhook.jpg) | No Errors |
| Checkout webhooks.py | n/a | ![screenshot](documentation/webhooks.jpg)| No Errors |
| Home urls.py | n/a | ![screenshot](documentation/home-urls.jpg) | No Errors |
| Home views.py | n/a | ![screenshot](documentation/home-views.jpg) | No Errors |
| Home forms.py | n/a | ![screenshot](documentation/home-forms.jpg) | No Errors |
| Home models.py | n/a | ![screenshot](documentation/home-models.jpg) | No Errors |
| Home admin.py | n/a | ![screenshot](documentation/home-admin.jpg) | No Errors |
| Products admin.py |  n/a | ![screenshot](documentation) | No Errors |
| Products forms.py | n/a | ![screenshot](documentation/image-127.png) | Pass: No Errors |
| Products models.py |  n/a | ![screenshot](documentation/image-128.png) | Pass: No Errors |
| Products urls.py | n/a  | ![screenshot](documentation/image-129.png) | Pass: No Errors |
| Products views.py | n/a  | ![screenshot](documentation/image-130.png) | Pass: No Errors |
| Products widgets.py | n/a | ![screenshot](documentation/image-131.png)| Pass: No Errors |
| Profiles forms.py | n/a  | ![screenshot](documentation/image-132.png) | Pass: No Errors |
| Profiles models.py | n/a| ![screenshot](documentation/image-133.png) | Pass: No Errors |
| Profiles urls.py | n/a | ![screenshot](documentation/image-134.png) | Pass: No Errors |
| Profiles views.py | n/a | ![screenshot](documentation/image-135.png) | Pass: No Errors |
| Wishlist admin.py | n/a  | ![screenshot](documentation/image-136.png) | Pass: No Errors |
| Wishlist models.py | n/a| ![screenshot](documentation/image-137.png) | Pass: No Errors |
| Wishlist urls.py | n/a | ![screenshot](documentation/image-138.png) | Pass: No Errors |
| Wishlist views.py | n/a | ![screenshot](documentation/image-139.png) | Pass: No Errors |
| Base settings.py | n/a  | ![screenshot]![Alt text](documentation/image-140.png)| Pass: No Errors |
| Base urls.py | n/a | ![screenshot](documentation/image-141.png) | Pass: No Errors |
| Base views.py | n/a | ![screenshot](documentation/image-142.png) | Pass: No Errors |
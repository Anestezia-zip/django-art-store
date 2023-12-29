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

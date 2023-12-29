
$('.btt-link').click(function (e) {
    e.preventDefault();
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
})

// Getting CSRF token from a cookie
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

document.querySelectorAll('.toggle-wishlist').forEach((heart) => {
    heart.addEventListener('click', async (e) => {
        try {
            const productId = e.target.dataset.productId;

            const response = await fetch(`/products/toggle-wishlist/${productId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP Error! Status: ${response.status}`);
            }

            const data = await response.json();

            if (data.added) {
                e.target.classList.add('active');
            } else {
                e.target.classList.remove('active');
            }
        } catch (error) {
            console.error('An error occurred:', error);
            alert('An error occurred while processing the request');
        }
    });
});


document.querySelectorAll('.remove-from-wishlist').forEach((trashIcon) => {
    trashIcon.addEventListener('click', async (e) => {
        const productId = e.target.dataset.productId;

        try {
            const response = await fetch(`/products/remove_from_wishlist/${productId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();

            if (data.removed) {
                // Traverse up the DOM to find the parent card element and remove it
                const card = e.target.closest('.card');
                if (card) {
                    card.remove(); // Remove the entire card
                }
            } else {
                console.error('An error occurred when removing a painting from the wishlist.');
            }
        } catch (error) {
            console.error('An error occurred:', error);
            alert('An error occurred while processing the request');

        }
    });
});
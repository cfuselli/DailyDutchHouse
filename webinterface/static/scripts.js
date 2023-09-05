    document.addEventListener('DOMContentLoaded', function () {
        const form = document.getElementById('filter-form');
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            
            const minPrice = parseFloat(document.getElementById('min-price').value);
            const maxPrice = parseFloat(document.getElementById('max-price').value);
            
            // Filter the house listings based on price
            const filteredHouses = houses.filter(function (house) {
                const price = parseFloat(house.price.replace('€', '').replace(',', '').trim());
                return isNaN(price) || (minPrice <= price && price <= maxPrice);
            });
            
            // Update the displayed house listings
            updateHouseListings(filteredHouses);
        });
        
        // Function to update the displayed house listings
        function updateHouseListings(houseListings) {
            const container = document.querySelector('.container');
            
            // Clear existing house listings
            while (container.firstChild) {
                container.removeChild(container.firstChild);
            }
            
            // Add filtered house listings
            for (const house of houseListings) {
                const houseContainer = createHouseContainer(house);
                container.appendChild(houseContainer);
            }
        }
        
        // Function to create a house container (you may need to modify this function)
        function createHouseContainer(house) {
            // Your code to create a house container here
            // You can reuse your existing HTML structure for each house
        }
    });



    // Function to calculate and format the time difference
    function formatTimeDifference(dateString) {
        const currentDate = new Date();
        const postDate = new Date(dateString);
        const timeDifference = currentDate - postDate;

        const rtf = new Intl.RelativeTimeFormat('en', { numeric: 'auto' });
        let formattedTime;

        if (timeDifference < 60000) {
            formattedTime = rtf.format(-Math.floor(timeDifference / 1000), 'second');
        } else if (timeDifference < 3600000) {
            formattedTime = rtf.format(-Math.floor(timeDifference / 60000), 'minute');
        } else if (timeDifference < 86400000) {
            formattedTime = rtf.format(-Math.floor(timeDifference / 3600000), 'hour');
        } else {
            formattedTime = rtf.format(-Math.floor(timeDifference / 86400000), 'day');
        }

        return formattedTime;
    }

    // Loop through all house boxes and update the time difference
    const timeDifferenceElements = document.querySelectorAll('.time-difference');
    timeDifferenceElements.forEach(function (element) {
        const dateString = element.textContent; // Get the date string
        const formattedTime = formatTimeDifference(dateString);
        element.textContent = formattedTime;
    });

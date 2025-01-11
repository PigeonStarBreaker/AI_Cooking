const ingredientInput = document.getElementById('ingredientInput');
const addButton = document.getElementById('addButton');
const deleteButton = document.getElementById('deleteButton');
const doneButton = document.getElementById('doneButton');
const ingredientsList = document.getElementById('ingredientsList');
const submitButton = document.getElementById('submitButton');
const responseTextarea = document.getElementById('responseTextarea');

// Array to store ingredients
const ingredients = [];
let deleteMode = false;

// Add ingredient to the list
addButton.addEventListener('click', () => {
    const ingredient = ingredientInput.value.trim();
    if (ingredient) {
        ingredients.push(ingredient); // Add to array

        // Add to the UI list
        const listItem = document.createElement('li');
        listItem.className = 'ingredient-item';
        listItem.textContent = ingredient;

        // Add delete button to each item
        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = 'X';
        deleteBtn.addEventListener('click', () => {
            // Remove ingredient from array and UI
            const index = ingredients.indexOf(ingredient);
            if (index > -1) ingredients.splice(index, 1);
            listItem.remove();
        });

        listItem.appendChild(deleteBtn);
        ingredientsList.appendChild(listItem);

        // Clear the input field
        ingredientInput.value = '';
        ingredientInput.focus();
    }
});

// Enable delete mode
deleteButton.addEventListener('click', () => {
    deleteMode = true;
    ingredientsList.classList.add('delete-mode');
    deleteButton.style.display = 'none';
    doneButton.style.display = 'inline-block';
});

// Disable delete mode
doneButton.addEventListener('click', () => {
    deleteMode = false;
    ingredientsList.classList.remove('delete-mode');
    doneButton.style.display = 'none';
    deleteButton.style.display = 'inline-block';
});

// Handle submit button click
submitButton.addEventListener('click', async () => {
    if (ingredients.length === 0) {
        responseTextarea.value = "No ingredient";
        return;
    }

    try {
        responseTextarea.value = "Connecting to the server...";
        const response = await fetch('http://127.0.0.1:5000/find_recipes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ingredients }),
        });

        if (response.ok) {
            const data = await response.json();
            responseTextarea.value = data.message || "Food successfully generated";
        } else {
            responseTextarea.value = "Error connecting to the server";
        }
    } catch (error) {
        responseTextarea.value = "Unable to connect to the server. Please try again.";
        console.error('Error:', error); // Logs the error for debugging
    }
});
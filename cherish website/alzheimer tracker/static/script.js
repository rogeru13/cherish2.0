const memoryForm = document.getElementById("memory-form");
const memoryList = document.getElementById("memory-list");

// Handle form submission to save memory
memoryForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(memoryForm);

    // Send data to the backend
    fetch("/save_memory", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            console.log("Memory saved:", data);

            // Add memory to the list
            const memoryCard = document.createElement("div");
            memoryCard.classList.add("col-md-4");
            memoryCard.innerHTML = `
                <div class="card shadow-sm">
                    <div class="card-body">
                        <p>${data.text}</p>
                        ${data.image ? `<img src="${data.image}" class="img-fluid mt-2" alt="Memory Image">` : ""}
                    </div>
                </div>
            `;
            memoryList.appendChild(memoryCard);

            // Reset the form
            memoryForm.reset();
        })
        .catch((error) => {
            console.error("Error saving memory:", error);
        });
});

// Fetch existing memories from the backend when the page loads
fetch("/get_memories")
    .then((response) => response.json())
    .then((memories) => {
        memories.forEach((memory) => {
            const memoryCard = document.createElement("div");
            memoryCard.classList.add("col-md-4");
            memoryCard.innerHTML = `
                <div class="card shadow-sm">
                    <div class="card-body">
                        <p>${memory.text}</p>
                        ${memory.image ? `<img src="${memory.image}" class="img-fluid mt-2" alt="Memory Image">` : ""}
                    </div>
                </div>
            `;
            memoryList.appendChild(memoryCard);
        });
    })
    .catch((error) => {
        console.error("Error fetching memories:", error);
    });

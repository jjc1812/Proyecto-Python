document.addEventListener("DOMContentLoaded", function() {
    const ul = document.getElementById("contacts");
    axios.get("https://jsonplaceholder.typicode.com/users")
    .then(response => {
        response.data.forEach(item => {
            const div = document.createElement("div");
            div.className ="preview";
            const image = document.createElement("img");
            image.src = "./static/img/undefined-person.webp";
            const li = document.createElement("li");
            const user = document.createElement("p");
            user.className = "subtitle";
            user.textContent = item.name;
            div.appendChild(image);
            div.appendChild(user);
            li.appendChild(div);
            ul.appendChild(li);
        });
    }).catch(error => {
        console.error("Error fetching data:", error);
    });
});
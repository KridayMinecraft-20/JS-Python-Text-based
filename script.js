var MyForm = document.getElementById("MyForm");
var MyItem = document.getElementById("myItem");
var MyInput = document.getElementById("MyInput");

MyForm.addEventListener("submit", function (event) {

    event.preventDefault();
    createItem(MyInput.value)
});

function createItem(inputItems)  {

    var destinations = `<li>${inputItems} <button onclick="deleteElement(this)">Delete</button></li>`
    MyItem.insertAdjacentHTML("beforeend", destinations);

    MyInput.value = "";
    MyInput.focus();
}

function deleteElement(ElementToDelete) {

    ElementToDelete.parentElement.remove()
}
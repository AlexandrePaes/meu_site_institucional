function translateToEnglish() {
  // Get the text of the page.
  const text = document.querySelector("body").textContent;

  // Translate the text to English.
  const translatedText = translate(text, "pt-BR", "en");

  // Replace the text of the page with the translated text.
  document.querySelector("body").textContent = translatedText;
}

// Add an event listener to the translation icon.
document.querySelector(".flag").addEventListener("click", translateToEnglish);



// function translateToEnglish() {
//   // Get the form data.
//   const name = document.getElementById("name").value;
//   const email = document.getElementById("email").value;
//   const phone = document.getElementById("phone").value;

//   // Translate the form data to English.
//   const translatedData = translate(name, email, phone);

//   // Display the translated data on the page.
//   document.querySelector(".translated-data").innerText = translatedData;
// }

// // Add an event listener to the translation icon.
// document.querySelector("a").addEventListener("click", translateToEnglish);



// function saveFormData() {
//     // Get the data from each element on the form.
//     const name = document.getElementById("name").value;
//     const email = document.getElementById("email").value;
//     const phone = document.getElementById("phone").value;
  
//     // Create a JavaScript object to store the data.
//     const data = {
//       name: name,
//       email: email,
//       phone: phone,
//     };
  
//     // Save the data to a text file.
//     const textFile = new File("data.txt", {
//       type: "text/plain",
//     });
//     textFile.write(JSON.stringify(data));
  
//     // Redirect the user to a confirmation page.
//     window.location.href = "confirm.html";
//   }
  
//   // Add an event listener to the submit button.
//   document.getElementById("submit").addEventListener("click", saveFormData);
  
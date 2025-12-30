console.log("Die Seite wurde geladen!");
alert("Willkommen auf meiner Website!");

document.getElementById("button001").addEventListener("click", () => {
    alert("Du hast geklickt!");
});

document.getElementById("button003_dyn_text").addEventListener("click", () => {
    document.getElementById("dynText").innerText = "Der Text wurde geändert!";
});

document.getElementById("button004_toggle_secret").addEventListener("click", () => {
    const text = document.getElementById("secretText"); 
    text.classList.toggle("hidden");
});


let count_var = 0;

document.getElementById("plusButton").addEventListener("click", () => {
    count_var++;
    document.getElementById("counter").textContent = count_var;
});

document.getElementById("minusButton").addEventListener("click", () => {
    count_var--;
    document.getElementById("counter").textContent = count_var;
});

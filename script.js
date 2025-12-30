window.onload = () => {
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

    document.getElementById("fetch_rand").addEventListener("click", () => {
        fetch("https://democracy1434.pythonanywhere.com/api/random")
            .then(res => res.json())
            .then(data => {
                console.log("DATA VOM SERVER:", data); 
                console.log("TYP:", typeof data.number);
                document.getElementById("rand_num").textContent = data.number;
            });
    });

    async function fetchEntries() {
        const response = await fetch("https://democracy1434.pythonanywhere.com/api/entries");
        const data = await response.json();
        return data;
    }

    function transformEntriesToChartData(entries) {
        return entries.map(entry => ({
            x: entry.created_at,   // should be an ISO date string from your API
            y: entry.mood          // integer
        }));
    }

    async function renderMoodChart() {
        const entries = await fetchEntries();
        const dataPoints = transformEntriesToChartData(entries);

        const ctx = document.getElementById("moodChart").getContext("2d");

        const labels = dataPoints.map(p => p.x);
        const values = dataPoints.map(p => p.y);

        new Chart(ctx, {
            type: "line",
            data: {
                labels: labels,
                datasets: [{
                    label: "Mood over time",
                    data: values,
                    borderColor: "rgb(75, 192, 192)",
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    tension: 0.2,
                    pointRadius: 3,
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: "Date"
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: "Mood"
                        },
                        ticks: {
                            stepSize: 1
                        }
                    }
                }
            }
        });
    }


    document.getElementById("button_render_chart").addEventListener("click", () => {
        alert("Du hast den Plot gerendert!");
        renderMoodChart();
    });

        



};
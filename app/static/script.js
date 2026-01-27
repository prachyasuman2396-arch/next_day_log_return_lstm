async function predict() {
    const ticker = document.getElementById("ticker").value || "AAPL";
    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "⏳ Predicting...";

    try {
        const response = await fetch(`/predict?ticker=${ticker}`);

        if (!response.ok) {
            throw new Error("API error");
        }

        const data = await response.json();

        resultDiv.innerHTML = `
            <strong>Ticker:</strong> ${data.ticker}<br/>
            <strong>Next-day log return:</strong> ${data.next_day_log_return.toFixed(6)}
        `;
    } catch (error) {
        resultDiv.innerHTML = "❌ Error while predicting";
    }
}

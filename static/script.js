function updateData() {
    fetch('/data')
        .then(res => res.json())
        .then(data => {
            document.getElementById('rpm').textContent = data.rpm + " RPM";
            document.getElementById('speed').textContent = data.speed + " km/h";
            document.getElementById('tire').textContent = data.tire_pressure.join(" | ") + " psi";
            document.getElementById('temp').textContent = data.engine_temp + " °C";
        });
}

setInterval(updateData, 1000);

document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/data')
    .then(response => response.json())
    .then(data => {
        const map = L.map('map').setView([-23.55052, -46.633308], 4);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        data.forEach(record => {
            const marker = L.marker([record.point_of_sale.lat, record.point_of_sale.lon]).addTo(map);
            marker.bindPopup(`
                <b>Vehicle:</b> ${record.vehicle}<br>
                <b>Time:</b> ${record.transaction_date}<br>
                <b>Location:</b> ${record.point_of_sale.name}<br>
                <b>City:</b> ${record.point_of_sale.city}, ${record.point_of_sale.state}<br>
                <b>Product:</b> ${record.product}<br>
                <b>Quantity:</b> ${record.quantity.toFixed(2)} L<br>
                <b>Unit Price:</b> R$${record.unit_price.toFixed(2)}<br>
                <b>Total Price:</b> R$${record.total_price.toFixed(2)}
            `);

            // Função para formatar a data/hora no formato dd/mm/yyyy 00:00:00
            function formatDateTime(dateTime) {
                const date = new Date(dateTime);
                const day = String(date.getDate()).padStart(2, '0');
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const year = date.getFullYear();
                const hours = String(date.getHours()).padStart(2, '0');
                const minutes = String(date.getMinutes()).padStart(2, '0');
                const seconds = String(date.getSeconds()).padStart(2, '0');
                return `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;
            }

            // Adicionar dados ao relatório
            const tbody = document.querySelector('#report-table tbody');
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${record.vehicle}</td>
                <td>${formatDateTime(record.transaction_date)}</td>
                <td>${record.odometer}</td>
                <td>${record.point_of_sale.name}</td>
                <td>${record.point_of_sale.city}, ${record.point_of_sale.state}</td>
                <td>${record.product}</td>
                <td>${record.quantity.toFixed(2)}</td>
                <td>R$${record.unit_price.toFixed(2)}</td>
                <td>R$${record.total_price.toFixed(2)}</td>
            `;
            tbody.appendChild(row);
        });
    });
});

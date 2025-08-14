// Placeholder for system stats (would be replaced with real data later)
document.addEventListener('DOMContentLoaded', function() {
    // System page - simulate data
    if (document.getElementById('cpu-usage')) {
        setInterval(() => {
            const cpuUsage = Math.floor(Math.random() * 100);
            document.getElementById('cpu-usage').style.width = `${cpuUsage}%`;
            document.getElementById('cpu-usage').textContent = `${cpuUsage}%`;
            
            const memUsage = Math.floor(Math.random() * 100);
            document.getElementById('memory-usage').style.width = `${memUsage}%`;
            document.getElementById('memory-usage').textContent = `${memUsage}%`;
            
            document.getElementById('temperature').textContent = `${Math.floor(Math.random() * 50 + 30)}°C`;
            document.getElementById('uptime').textContent = `${Math.floor(Math.random() * 10)} days`;
        }, 2000);
    }
    
    // Finance page - placeholder chart
    if (document.getElementById('finance-chart')) {
        const ctx = document.getElementById('finance-chart').getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Housing', 'Food', 'Transport', 'Entertainment', 'Savings'],
                datasets: [{
                    data: [30, 20, 15, 10, 25],
                    backgroundColor: [
                        '#0d6efd',
                        '#198754',
                        '#ffc107',
                        '#dc3545',
                        '#6c757d'
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    }
});
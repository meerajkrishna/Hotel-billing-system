const API = "http://127.0.0.1:8000";
let menuItems = [];
let lastOrderId = null;

async function loadMenu() {
    const res = await fetch(`${API}/items/`);
    menuItems = await res.json();

    const menuDiv = document.getElementById("menu");
    menuDiv.innerHTML = "";

    menuItems.forEach(item => {
        const div = document.createElement("div");
        div.innerHTML = `
            ${item.name} - ₹${item.price}
            Qty:
            <input type="number" id="qty-${item.id}" min="0" value="0">
        `;
        menuDiv.appendChild(div);
    });
}

async function createOrder() {
    const items = [];

    menuItems.forEach(item => {
        const qty = parseInt(document.getElementById(`qty-${item.id}`).value);
        if (qty > 0) {
            items.push({ item_id: item.id, quantity: qty });
        }
    });

    if (items.length === 0) {
        alert("Select at least one item");
        return;
    }

    const res = await fetch(`${API}/orders/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ items })
    });

    const order = await res.json();
    lastOrderId = order.id;
    loadBill(order.id);
}

async function loadBill(orderId) {
    const res = await fetch(`${API}/bill/${orderId}`);
    const bill = await res.json();

    const tbody = document.querySelector("#bill-table tbody");
    tbody.innerHTML = "";

    bill.items.forEach(item => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${item.name}</td>
            <td>₹${item.price}</td>
            <td>${item.quantity}</td>
            <td>₹${item.subtotal}</td>
        `;
        tbody.appendChild(row);
    });

    document.getElementById("total").innerText =
        `Total Amount: ₹${bill.total_amount}`;
}

function downloadPDF() {
    if (!lastOrderId) {
        alert("Generate bill first");
        return;
    }
    window.open(`${API}/bill/pdf/${lastOrderId}`);
}

loadMenu();

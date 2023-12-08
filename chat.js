// Определение функций для взаимодействия с элементами страницы
function showCheckout() {
    // Здесь может быть ваш код для оформления заказа
    alert('Оформление заказа!');
}

function buyProduct(productId) {
    // Здесь может быть ваш код для покупки товара
    alert('Покупка товара ' + productId);
}

function sendMessage() {
    // Здесь может быть ваш код для отправки сообщения в чат
    var messageInput = document.getElementById('messageInput');
    var chatMessages = document.getElementById('chatMessages');
    
    var message = messageInput.value;
    if (message.trim() !== '') {
        // Добавление сообщения в чат
        chatMessages.innerHTML += '<div>' + message + '</div>';
        // Очистка поля ввода
        messageInput.value = '';
    }
}

// Показать или скрыть выдвигающую панель с чатом
document.getElementById('chatPanel').addEventListener('mouseover', function() {
    this.style.left = '0';
});

document.getElementById('chatPanel').addEventListener('mouseout', function() {
    this.style.left = '-300px';
});

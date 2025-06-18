function deleteTodoItem(itemId) {
    fetch(`/todo/${itemId}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),  // 获取 CSRF token
        },
    })
    .then(response => {
        if (response.ok) {
            console.log(`Item ${itemId} 删除成功`);
            // 找到对应的行，删除它
            const row = document.querySelector(`tr[data-id="${itemId}"]`);
            if (row) {
                row.remove();
            }
        } else {
            console.error(`删除失败，状态码: ${response.status}`);
        }
    })
    .catch(error => {
        console.error('请求失败:', error);
    });
}

function updateItemPrompt(itemId) {
    const newText = prompt(`请输入 item${itemId} 的新内容：`);
    if (newText !== null && newText.trim() !== "") {
        const data = {
            item: newText,  //item 这个字段很重要，要不然后台对应的视图函数读取不到
        };
        // data 是一个 JavaScript 对象，包含要更新的内容
        updateTodoItem(itemId, data);
    }
}

function updateTodoItem(itemId, data) {
    fetch(`/todo/${itemId}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),  // 获取 CSRF token
        },
        body: JSON.stringify(data)  // 将 data 从 JavaScript 对象转化为 JSON 字符串
    })
    .then(response => response.json())
    .then(result => {
        // result 是一个 JavaScript 对象，从后端获取
        if (result.success) {
            console.log(`Item ${itemId} 更新成功`);
            // 更新页面对应的td显示内容
            const row = document.querySelector(`tr[data-id="${itemId}"]`);
            if (row) {
                // 更新第二列，即 item 的内容
                row.cells[1].textContent = data.item;

                // 更新第六列，即 item 的更新时间
                row.cells[5].textContent = result.updated_at;
            }
        } else {
            console.error(`更新失败，状态码: ${response.status}`);
        }
    })
    .catch(error => {
        console.error('更新失败:', error);
    });
}

function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        const [key, value] = cookie.trim().split('=');
        if (key === name) {
            return decodeURIComponent(value);
        }
    }
    return null;
}

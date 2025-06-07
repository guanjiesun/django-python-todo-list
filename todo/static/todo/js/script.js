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
            location.reload();
        } else {
            console.error(`删除失败，状态码: ${response.status}`);
        }
    })
    .catch(error => {
        console.error('请求失败:', error);
    });
}

function updateTodoItem(itemId, data) {
    fetch(`/todo/${itemId}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),  // 获取 CSRF token
        },
        body: JSON.stringify(data)  // 将 data 从 json 对象转化为 json 字符串
    })
    .then(response => {
        if (response.ok) {
            console.log(`Item ${itemId} 更新成功`);
            location.reload();
        } else {
            console.error(`更新失败，状态码: ${response.status}`);
        }
    })
    .catch(error => {
        console.error('更新失败:', error);
    });
}

function updateItemPrompt(itemId) {
    const newText = prompt(`请输入 item${itemId} 的新内容：`);
    if (newText !== null && newText.trim() !== "") {
        const data = {
            item: newText,  //item 这个字段很重要，要不然后台对应的视图函数读取不到
        };
        updateTodoItem(itemId, data);
    }
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

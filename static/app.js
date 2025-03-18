new Vue({
    el: '#orders_app',
    data: {
        orders: [],
        loading: true
    },
    created: function (){
        console.log("Vue компонент создан");  // Лог
        const vm = this;
        axios.get('/api/orders/')
        .then(function (response){
            console.log("Данные получены:", response.data);  // Лог
            vm.orders = response.data;
        })
        .catch(function (error) {
            console.error("Ошибка при загрузке заказов:", error);  // Лог
        })
        .finally(function () {
            console.log("Загрузка завершена");  // Лог
            vm.loading = false;
        });
    }
})
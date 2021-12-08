//#при нажатии на количество для увелич или уменш запускается скрипт отрабатывать комманду,
//путь идет через url:"/baskets/edit/" контроллеру.

window.onload = function () {
    $('.basket_list').on('click','input[type="number"]',function (){
        let t_href = event.target
        $.ajax()
            {
                url:"/baskets/edit/" + t_href.name + '/' + t_href.value + '/',
                succes : function(data){
                    $('.basket_list').hrml(data.result)

                 }

            });
         event.preventDefoult()


    })

    $('.card_add_basket').on('click','button[type="nbutton"]',function (){
        let t_href = event.target.value
        $.ajax()
            {
                url:"/baskets/add/"  + t_href + '/',
                succes : function(data){
                    $('.card_add_baskett').hrml(data.result)
                    alert('Товар добавлен в корзину')

                 }

            });
         event.preventDefoult()

}
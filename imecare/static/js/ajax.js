/**
 * Created by avale on 22/11/15.
 */

$(document).ready(function(){
    $('body').on('click.modal.data-api', '[data-toggle="collapse"]', function ( e ) {
        $this = $(this)
        if ($($(this).attr('href')).hasClass('in')) {
            $this.children().first().attr('src', "/static/imagem/fechado.png");
        }
        else {
            $this.children().first().attr('src', "/static/imagem/aberto.png");
        }
    });
});
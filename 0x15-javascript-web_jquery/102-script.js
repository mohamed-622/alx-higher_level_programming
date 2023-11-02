$(document).ready(function () {
  $('#btn_translate').click(function () {
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + $('input#language_code').val(),
      type: 'GET',
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  });
});

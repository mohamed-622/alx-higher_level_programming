$(document).ready(function () {
  $('#btn_translate').click(function () {
    translate();
  });
  $('#language_code').keydown(function (e) {
    if (e.keyCode === 13) {
      translate();
    }
  });
  function translate () {
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + $('input#language_code').val(),
      type: 'GET',
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  }
});

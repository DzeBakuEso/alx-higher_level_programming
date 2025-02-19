$(document).ready(function () {
  function translateHello() {
    const langCode = $("#language_code").val().trim();
    if (langCode !== "") {
      $.get(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function (data) {
        $("#hello").text(data.hello);
      });
    }
  }

  // Fetch translation on button click
  $("#btn_translate").click(translateHello);

  // Fetch translation when pressing Enter in the input field
  $("#language_code").keypress(function (event) {
    if (event.which === 13) { // 13 = Enter key
      translateHello();
    }
  });
});

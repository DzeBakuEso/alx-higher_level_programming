$(document).ready(function () {
  $("#btn_translate").click(function () {
    const langCode = $("#language_code").val().trim();
    if (langCode !== "") {
      const url = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;
      
      $.get(url, function (data) {
        $("#hello").text(data.hello);
      });
    }
  });
});

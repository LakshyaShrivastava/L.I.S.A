$(document).ready(function () {
    
    // Displays the message that was spoken by user 
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".lisa-message li:first").text(message);
        $('.lisa-message').textillate('start')
    }

    // Display Hood
    eel.expose(ShowBlob)
    function ShowBlob() {
        $("#Oval").attr("hidden", false);
        $("#LisaWave").attr("hidden", true);
      }
});
$("#getRecommendations").click(function() {
    var mode = $("#mode").val();
    var genres = [];
    $('#genres input:checked').each(function() {
        genres.push($(this).attr('value'));
    });
    // Convert the array of genres to a comma-separated string
    var genreString = genres.join(",");
    // Display the selected genres
    $("#selectedGenres").html("Выбранные жанры: " + genreString);
    $.ajax({
        url: "http://127.0.0.1:8000" + mode, // Change this to the appropriate API endpoint
        type: "GET",
        data: { genres: genreString },
        success: function(response) {
            var recommendations = response.data;
            var html = "<ul>";
            for (var i = 0; i < recommendations.length; i++) {
                html += "<li>" + recommendations[i] + "</li>";
            }
            html += "</ul>";
            $("#recommendations").html(html);
        }
    });
});
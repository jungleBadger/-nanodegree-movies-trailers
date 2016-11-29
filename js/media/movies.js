/**
 * Created by danielabrao on 11/29/16.
 */
(function () {
    "use strict";

    var Parent = require("./media");

    module.exports = function (attributes) {
        return (function Init() {

            var movie = Parent({
                "media_title": attributes.movie_title,
                "media_storyline": attributes.movie_storyline,
                "media_poster_url": attributes.poster_image,
                "media_youtube_url": attributes.trailer_youtube
            });

            Object.freeze(movie);

            return movie.methods;

        }());
    };

}());
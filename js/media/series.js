/**
 * Created by danielabrao on 11/29/16.
 */
(function () {
    "use strict";

    var Parent = require("./media");

    module.exports = function (attributes) {
        return (function Init() {

            var serie = Parent({
                "media_title": attributes.serie_title,
                "media_storyline": attributes.serie_storyline,
                "media_poster_url": attributes.poster_image,
                "media_youtube_url": attributes.trailer_youtube
            });

            serie.properties.seasons = attributes.serie_seasons;

            Object.freeze(serie);

            return serie.methods;

        }());
    };

}());
/**
 * Created by danielabrao on 11/27/16.
 */
(function () {
    "use strict";

    var youtubeURLPrep = require("./../helpers/youtube_url_prep"),
        openBrowser = require("./../helpers/openBrowser");

    module.exports = function (attributes) {
        return (function Init() {
            var properties = {
                "title": attributes.media_title,
                "storyline": attributes.media_storyline,
                "poster_image_url": attributes.media_poster_url,
                "trailer_youtube_url": attributes.media_youtube_url,
                "trailer_youtube_id": youtubeURLPrep(attributes.media_youtube_url)
            };

            var methods = {
                "getProperty": function (prop) {
                    return properties[prop];
                },
                "getMediaData": function () {
                    return properties;
                },
                "openMediaTrailer": function () {
                    openBrowser(this.getProperty("trailer_youtube_url"));
                }
            };

            return {
                properties: properties,
                methods: methods
            };

        }());
    };
}());
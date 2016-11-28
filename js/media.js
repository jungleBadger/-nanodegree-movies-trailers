/**
 * Created by danielabrao on 11/27/16.
 */
(function () {
    "use strict";

        var childProcess = require("child_process"),
            youtubeURLPrep = require("./youtube_url_prep");

        module.exports = function (attributes) {
        return (function Init() {
            var properties = {
                "title": attributes.movie_title,
                "storyline": attributes.movie_storyline,
                "poster_image_url": attributes.poster_image,
                "trailer_youtube_url": attributes.trailer_youtube,
                "trailer_youtube_id": youtubeURLPrep(attributes.trailer_youtube)
            };

            Object.freeze(properties);

            var methods = {
                "getProperty": function (prop) {
                    return properties[prop];
                },
                "getMovieData": function () {
                    return properties;
                },
                "openMovieTrailer": function () {
                    if (process.platform === "win32") {
                        childProcess.exec(["start chrome", this.getProperty("trailer_youtube_url")].join(" "), function () {
                            console.log("Google chrome opened");
                        });
                    } else {
                        childProcess.exec(["open -a 'Google Chrome'", this.getProperty("trailer_youtube_url")].join(" "), function () {
                            console.log("Google chrome opened");
                        });
                    }
                }
            };

            return methods;

        }());
    };

}());
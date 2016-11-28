/**
 * Created by danielabrao on 11/28/16.
 */
(function () {
    "use strict";
    module.exports = function (youtube_url) {
        if (!youtube_url) {
            return "None";
        } else {
            return youtube_url.slice(youtube_url.search("v=") + 2, youtube_url.length);
        }
    };
}());
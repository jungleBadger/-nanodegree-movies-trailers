/**
 * Created by danielabrao on 11/29/16.
 */
(function () {
    "use strict";
    var childProcess = require("child_process");
    module.exports = function (url) {
        if (process.platform === "win32") {
            childProcess.exec(["start chrome", url].join(" "), function () {
                console.log("Google chrome opened");
            });
        } else {
            childProcess.exec(["open -a 'Google Chrome'", url].join(" "), function () {
                console.log("Google chrome opened");
            });
        }
    };
}());
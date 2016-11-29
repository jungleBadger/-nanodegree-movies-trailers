/**
 * Created by danielabrao on 11/27/16.
 */
(function () {
    "use strict";
    var express = require("express"),
        app = express(),
        engines = require("consolidate"),
        ejs = require("ejs"),
        fs = require("fs"),
        openBrowser = require("./helpers/openBrowser"),
        server = require("http").createServer(app);


    app.engine("html", engines.ejs);
    app.set("view engine", "html");

    (function buildEnv(moviesList, seriesList) {
        var moviesCreator = require("./media/movies"),
            seriesCreator = require("./media/series"),
            moviesArr = [],
            seriesArr = [];

        moviesList.forEach(function (movie) {
            moviesArr.push(moviesCreator(movie));
        });

        seriesList.forEach(function (serie) {
            seriesArr.push(seriesCreator(serie));
        });

        console.log(seriesArr.length);

        ejs.renderFile("./views/movies.view.ejs", {
            "movies": moviesArr,
            "series": seriesArr
        }, function (err, str) {
            if (!err) {
                fs.writeFile("./views/movies.view.html", str, function (err) {
                    if (!err) {
                        console.log("saved");
                    }
                });
            }
        });

    }(require("./model/movies"), require("./model/series")));

    app.get("/", function (req, res) {
        return res.status(200).render("movies.view.html");
    });

    server.listen(3500, function () {
        console.log("HTTP server running on: localhost:3500");
        openBrowser("http://localhost:3500");
    });

}());
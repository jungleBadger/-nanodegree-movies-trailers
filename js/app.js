/**
 * Created by danielabrao on 11/27/16.
 */
(function () {
    "use strict";
    var express = require('express'),
        app = express(),
        engines = require('consolidate'),
        ejs = require('ejs'),
        fs = require("fs"),
        server = require('http').createServer(app);


    app.engine('html', engines.ejs);
    app.set('view engine', 'html');

    var media = require("./media"),
        moviesList = require("./model/movies"),
        moviesArr = [];


    moviesList.forEach(function (movie) {
        moviesArr.push(media(movie));
    });

    ejs.renderFile('./views/movies.view.ejs', {
        movies: moviesArr
    }, function (err, str) {
        if (!err) {
            fs.writeFile("./views/movies.view.html", str, function (err) {
                if (!err) {
                    console.log("saved");
                }
            });
        }
    });

    app.get("/", function (req, res) {
        return res.status(200).render("movies.view.html");
    });

    server.listen(3500, function () {
        console.log(3500);
    });

}());
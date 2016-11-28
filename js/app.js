/**
 * Created by danielabrao on 11/27/16.
 */
(function () {
    "use strict";
    var express = require('express'),
        app = express(),
        engines = require('consolidate'),
        ejs = require('ejs'),
        server = require('http').createServer(app);


    app.set('views', '../views');
    app.engine('html', engines.ejs);
    app.set('view engine', 'html');

    var media = require("./media"),
        moviesList = require("./model/movies"),
        moviesArr = [];


    moviesList.forEach(function (movie) {
        moviesArr.push(media(movie));
    });

    app.get("/", function (req, res) {
        return res.status(200).render('movies.view.ejs', {
            movies: moviesArr
        });
    });

    server.listen(3500, function () {
        console.log(3500);
    });

}());
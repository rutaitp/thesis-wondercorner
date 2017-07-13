var https = require('http');
// var http = require('http');
var fs = require('fs');
var url = require('url');

var privateKey = fs.readFileSync('my-key.pem');
var certificate = fs.readFileSync('my-cert.pem');

var credentials = {key: privateKey, cert: certificate };

var express = require('express');
//Create an app
var app = express();

//Set up the server
var httpsServer = https.createServer(app);
// var httpServer = http.createServer(credentials, app);

app.use(express.static("website"));

app.get("/about", sayHello);

function sayHello(req,res) {
	res.sendFile("/root/Website/website/about.html");
}

app.get("/questions", getQuestions);

function getQuestions(req,res) {
	res.sendFile("/root/Website/website/questions.html");
}

app.get("/answers", getAnswers);

function getAnswers(req,res) {
	res.sendFile("/root/Website/website/answers.html");
}

//WEBSOCKET PORTION
// WebSockets work with the HTTPS server
var io = require('socket.io').listen(httpsServer);

httpsServer.listen(80, function() {
	console.log("App listening on port 80!");
});

// httpServer.listen(8084, function() {
// 	console.log("App listening on port 8084!");
// });

var questionFile;
var textFile = [];

io.sockets.on('connection', function (socket){
	console.log("Working!");

	// var questionFiles = fs.readdirSync('/root/Website/website/data/questions/');
	var questionFiles = fs.readdirSync('/CODE/questions_text/');
	var answerFiles = fs.readdirSync('/CODE/answers_text/');

	for (var i=0; i<questionFiles.length; i++) {
		
		// questionFile = fs.readFileSync("/root/Website/website/data/questions/" + questionFiles[i], "utf8");
		questionFile = fs.readFileSync("/CODE/questions_text/" + questionFiles[i], "utf8");

		console.log(questionFile);

		io.sockets.emit("sending_questions", questionFile);
	}

	for (var i=0; i<answerFiles.length; i++) {
		
		answerFile = fs.readFileSync("/CODE/answers_text/" + answerFiles[i], "utf8");

		console.log(answerFile);

		io.sockets.emit("sending_answers", answerFile);
	}

});